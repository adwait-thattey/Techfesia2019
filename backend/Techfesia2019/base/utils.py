import random


def generate_random_string(length = 10):
    choices = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    selected_arr = [random.choice(choices) for _ in range(length)]

    rand_string = "".join(selected_arr)

    return rand_string
