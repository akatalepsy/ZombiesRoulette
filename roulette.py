import random


def choose_random(num_set, number_of_choices, number_of_cycles, dictionary):
    for player in range(number_of_cycles):
        random_selections = []
        random_numbers = []
        for random_number in random.sample(num_set, number_of_choices):
            random_numbers += [random_number]
        for number in random_numbers:
            random_selections += [dictionary[number]]
        return random_selections


def choose_upgrade_status(random_selections):
    random_selections