from random import randrange
import random


def random_select_sample(array, amount):
    sample = []

    s = random.sample(array, amount) # 'amount' samples without replacement
    sample.extend(s)
    # sample.append(s)

    return sample


def extract_sample(sample, array):
    for s in sample:
        array.remove(s)


def random_extract_sample(array, amount):
    count = 0

    while count < amount:
        random_index = randrange(0, len(array))
        random_item = array[random_index]
        array.remove(random_item)
        count += 1