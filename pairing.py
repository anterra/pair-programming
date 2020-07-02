# Pairing, ideally, is good for both participants and for the work they produce.
# We would like to have everyone do some morning pairing with everyone else.
# Specifically, we need to determine a schedule of pairings so that everyone has a pair every day,
# and everyone eventually pairs with everyone else.
# Write a function that takes a list of names and returns a list of lists of tuples representing pairs.
# (Assume an even number of names, all distinct.) For example:

import numpy as np


def pairing(list_of_names):
    list_of_pairs = []
    list_of_days = []
    while list_of_names:
        name1 = np.random.choice(list_of_names, replace=False)
        name2 = np.random.choice(list_of_names, replace=False)
        pair = (name1, name2)
        list_of_pairs.append(pair)
        list_of_names.remove(name1)
        list_of_names.remove(name2)
    list_of_days.append(list_of_pairs)
    return list_of_days


def pairing2(list_of_names):
    list_of_unique_pairs = []
    # list_of_daily_pairs = []
    for name in list_of_names:
        for partner_name in list_of_names:
            if name != partner_name:
                if (partner_name, name) not in list_of_unique_pairs:
                    pair = (name, partner_name)
                    list_of_unique_pairs.append(pair)

    return list_of_unique_pairs


def pairing3(list_of_names):
    for name in list_of_names:
        copy_list = list_of_names
        pair_list = []
        for partner_name in copy_list:
            if name != partner_name:
                if (partner_name, name) not in copy_list:
                    pair = (name, partner_name)
                    pair_list.append(pair)
                    copy_list.remove(name)
                    copy_list.remove(partner_name)
        return pair_list


#print(pairing(["Andrea", "Bob", "Cassandra", "Doug"]))
print(pairing2(["Andrea", "Bob", "Cassandra", "Doug"]))

