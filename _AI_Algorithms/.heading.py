import copy
import random
from collections import defaultdict
from statistics import stdev

from utils import *
import warnings
warnings.filterwarnings("ignore")


class DataSet:
    """
    A data set for a machine learning problem. It has the following fields:

    d.examples   A list of examples. Each one is a list of attribute values.
    d.attrs      A list of integers to index into an example, so example[attr]
                 gives a value. Normally the same as range(len(d.examples[0])).
    d.attr_names Optional list of mnemonic names for corresponding attrs.
    d.target     The attribute that a learning algorithm will try to predict.
                 By default the final attribute.
    d.inputs     The list of attrs without the target.
    d.values     A list of lists: each sublist is the set of possible
                 values for the corresponding attribute. If initially None,
                 it is computed from the known examples by self.set_problem.
                 If not None, an erroneous value raises ValueError.
    d.distance   A function from a pair of examples to a non-negative number.
                 Should be symmetric, etc. Defaults to mean_boolean_error
                 since that can handle any field types.
    d.name       Name of the data set (for output display only).
    d.source     URL or other source where the data came from.
    d.exclude    A list of attribute indexes to exclude from d.inputs. Elements
                 of this list can either be integers (attrs) or attr_names.

    Normally, you call the constructor and you're done; then you just
    access fields like d.examples and d.target and d.inputs.
    """

    def __init__(self, examples=None, attrs=None, attr_names=None, target=-1, inputs=None,
                 values=None, distance=mean_boolean_error, name='', source='', exclude=()):
        """
        Accepts any of DataSet's fields. Examples can also be a
        string or file from which to parse examples using parse_csv.
        Optional parameter: exclude, as documented in .set_problem().
        >>> DataSet(examples='1, 2, 3')
        <DataSet(): 1 examples, 3 attributes>
        """
        self.name = name
        self.source = source
        self.values = values
        self.distance = distance
        self.got_values_flag = bool(values)

        # initialize .examples from string or list or data directory
        if isinstance(examples, str):
            self.examples = parse_csv(examples)
        elif examples is None:
            self.examples = parse_csv(open_data(name + '.csv').read())
        else:
            self.examples = examples

        # attrs are the indices of examples, unless otherwise stated.
        if self.examples is not None and attrs is None:
            attrs = list(range(len(self.examples[0])))

        self.attrs = attrs

        # initialize .attr_names from string, list, or by default
        if isinstance(attr_names, str):
            self.attr_names = attr_names.split()
        else:
            self.attr_names = attr_names or attrs
        self.set_problem(target, inputs=inputs, exclude=exclude)

    def set_problem(self, target, inputs=None, exclude=()):
        """
        Set (or change) the target and/or inputs.
        This way, one DataSet can be used multiple ways. inputs, if specified,
        is a list of attributes, or specify exclude as a list of attributes
        to not use in inputs. Attributes can be -n .. n, or an attr_name.
        Also computes the list of possible values, if that wasn't done yet.
        """
        self.target = self.attr_num(target)
        exclude = list(map(self.attr_num, exclude))
        if inputs:
            self.inputs = remove_all(self.target, inputs)
        else:
            self.inputs = [a for a in self.attrs if a != self.target and a not in exclude]
        if not self.values:
            self.update_values()
        self.check_me()

    def check_me(self):
        """Check that my fields make sense."""
        assert len(self.attr_names) == len(self.attrs)
        assert self.target in self.attrs
        assert self.target not in self.inputs
        assert set(self.inputs).issubset(set(self.attrs))
        if self.got_values_flag:
            # only check if values are provided while initializing DataSet
            list(map(self.check_example, self.examples))

    def add_example(self, example):
        """Add an example to the list of examples, checking it first."""
        self.check_example(example)
        self.examples.append(example)

    def check_example(self, example):
        """Raise ValueError if example has any invalid values."""
        if self.values:
            for a in self.attrs:
                if example[a] not in self.values[a]:
                    raise ValueError('Bad value {} for attribute {} in {}'
                                     .format(example[a], self.attr_names[a], example))

    def attr_num(self, attr):
        """Returns the number used for attr, which can be a name, or -n .. n-1."""
        if isinstance(attr, str):
            return self.attr_names.index(attr)
        elif attr < 0:
            return len(self.attrs) + attr
        else:
            return attr

    def update_values(self):
        self.values = list(map(unique, zip(*self.examples)))

    def sanitize(self, example):
        """Return a copy of example, with non-input attributes replaced by None."""
        return [attr_i if i in self.inputs else None for i, attr_i in enumerate(example)]

    def classes_to_numbers(self, classes=None):
        """Converts class names to numbers."""
        if not classes:
            # if classes were not given, extract them from values
            classes = sorted(self.values[self.target])
        for item in self.examples:
            item[self.target] = classes.index(item[self.target])

    def remove_examples(self, value=''):
        """Remove examples that contain given value."""
        self.examples = [x for x in self.examples if value not in x]
        self.update_values()

    def split_values_by_classes(self):
        """Split values into buckets according to their class."""
        buckets = defaultdict(lambda: [])
        target_names = self.values[self.target]

        for v in self.examples:
            item = [a for a in v if a not in target_names]  # remove target from item
            buckets[v[self.target]].append(item)  # add item to bucket of its class

        return buckets

    def find_means_and_deviations(self):
        """
        Finds the means and standard deviations of self.dataset.
        means     : a dictionary for each class/target. Holds a list of the means
                    of the features for the class.
        deviations: a dictionary for each class/target. Holds a list of the sample
                    standard deviations of the features for the class.
        """
        target_names = self.values[self.target]
        feature_numbers = len(self.inputs)

        item_buckets = self.split_values_by_classes()

        means = defaultdict(lambda: [0] * feature_numbers)
        deviations = defaultdict(lambda: [0] * feature_numbers)

        for t in target_names:
            # find all the item feature values for item in class t
            features = [[] for _ in range(feature_numbers)]
            for item in item_buckets[t]:
                for i in range(feature_numbers):
                    features[i].append(item[i])

            # calculate means and deviations fo the class
            for i in range(feature_numbers):
                means[t][i] = mean(features[i])
                deviations[t][i] = stdev(features[i])

        return means, deviations

    def __repr__(self):
        return '<DataSet({}): {:d} examples, {:d} attributes>'.format(self.name, len(self.examples), len(self.attrs))


def parse_csv(input, delim=','):
    r"""
    Input is a string consisting of lines, each line has comma-delimited
    fields. Convert this into a list of lists. Blank lines are skipped.
    Fields that look like numbers are converted to numbers.
    The delim defaults to ',' but '\t' and None are also reasonable values.
    >>> parse_csv('1, 2, 3 \n 0, 2, na')
    [[1, 2, 3], [0, 2, 'na']]
    """
    lines = [line for line in input.splitlines() if line.strip()]
    return [list(map(num_or_str, line.split(delim))) for line in lines]


def err_ratio(predict, dataset, examples=None):
    """
    Return the proportion of the examples that are NOT correctly predicted.
    verbose - 0: No output; 1: Output wrong; 2 (or greater): Output correct
    """
    examples = examples or dataset.examples
    if len(examples) == 0:
        return 0.0
    right = 0
    for example in examples:
        desired = example[dataset.target]
        output = predict(dataset.sanitize(example))
        if output == desired:
            right += 1
    return 1 - (right / len(examples))

def create_cross_validation_data(dataset, num_groups = 10, start_row = 0):
    num_of_data = len(dataset)
    num_of_sub_group = int(num_of_data / num_groups)
    datasets = []
    for i in dataset:
        datasets.append(i[start_row:])
    random.shuffle(datasets)
    train_data = []
    train_label = []
    for i in range(num_groups):
        group_data = []
        group_label = []
        for j in range(num_of_sub_group):
            x = random.randint(0, len(datasets)-1)
            group_data.append(datasets[x][:-1])
            group_label.append(datasets[x][-1])
            del datasets[x]
        train_data.append(group_data)
        train_label.append(group_label)

    return train_data, train_label

def cross_validation( classifier,datasets, start_row = 0, num_groups = 10):
    data, label = create_cross_validation_data(datasets, num_groups, start_row)
    accuracy = []
    for i in range(num_groups):
        combined_data = []
        combined_label = []
        for j in range(num_groups):
            if i != j:
                combined_data += data[j]
                combined_label += label[j]
        classifier.fit(combined_data, combined_label)
        solution = classifier.predict(data[i])
        acc = test_accuracy(solution, label[i])
        accuracy.append(acc)
    print ('Mean Accuracy: {}'.format(np.mean(accuracy) * 100.0) + '%')


def test_accuracy(test_data, test_label):
    initial_score = 0
    for i in range(len(test_data)):
        if test_data[i] == test_label[i]:
            initial_score += 1
    accuracy = initial_score / len(test_label)
    print('Accuracy: {}'.format(accuracy * 100.0) + '%')
    return accuracy

def calculate_accuracy(test_data, test_label, target_list,classifier):
    count = 0
    for i,data in list(enumerate(test_data)):
        label = 0
        target = 0
        if isinstance(test_label[i], str):
            label = test_label[i]
        else: 
            label = target_list[test_label[i]]

        if isinstance(classifier(data), str):
            target = classifier(data)
        else: 
            target = target_list[classifier(data)]
        
        if target == label:
            count += 1
    accuracy = count/len(test_data)
    print ('Accuarcy: {}'.format(accuracy * 100.0) + '%')

def seperate_train_and_test_data(dataset, num_of_test_data, start_row = 0, end_row = 0):
    all_data = dataset[:]
    test_data_list = []
    test_data = []
    test_label = []
    train_data = []
    train_label = []
    while len(test_data_list) < num_of_test_data:
        x = random.randint(0, len(dataset) - 1)
        if x not in test_data_list:
            test_data_list.append(x)
    for i in range(len(all_data)):
        if i in test_data_list:
            test_data.append(np.array(all_data[i][start_row : -1]))
            test_label.append(np.array(all_data[i][-1]))
        else:
            train_data.append(np.array(all_data[i][start_row : -1]))
            train_label.append(np.array(all_data[i][-1]))
    test_data_list.sort()
    test_data_list.reverse()
    for i in test_data_list:
        del dataset[i]
    return np.array(train_data), np.array(train_label), np.array(test_data), np.array(test_label)


def generate_train_and_target_data(num_features, data, start_row = 0):
    return (np.array([x[start_row:num_features] for x in data]), np.array([x[-1] for x in data]))

def convert_train_label(train_label, target_list):
    convert_label = []
    for i in train_label:
        x = [ z*0 for z in range(len(target_list))]
        convert_label.append(x)
    return convert_label

def generate_train_and_test_dataset(dataset, num_of_test_data = 30, start_row = 0, end_row = 0):
    all_data = dataset[:]
    test_data_list = []
    train_data = []
    train_label = []
    test_data = []
    test_label = []
    while len(test_data_list) < num_of_test_data:
        x = random.randint(0, len(dataset)-1)
        if x not in test_data_list:
            test_data_list.append(x)
    for i in range(len(all_data)):
        if i in test_data_list:
            test_data.append(np.array(all_data[i][start_row : -1]))
            test_label.append(np.array(all_data[i][-1]))
        else:
            train_data.append(np.array(all_data[i][start_row : -1]))
            train_label.append(np.array(all_data[i][-1]))
    return np.array(train_data), np.array(train_label), np.array(test_data), np.array(test_label)

