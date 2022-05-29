import random
import string
import urllib


def ran_num():
    random_number = random.randint(1, 20)
    nums_list = random.sample(range(0, random_number), random_number)
    return nums_list


def ran_let():
    letters = [i for i in string.ascii_letters]
    ran_letters = random.sample(letters, random.randint(10, 52))
    return ran_letters


def shuffle_list():
    combine_lists = ran_num() + ran_let()
    ran_list = random.sample(combine_lists, len(combine_lists))
    return ran_list


def urls_list():
    list_of_urls = []
    listing = shuffle_list()
    list_of_urls.append(listing)
    return "".join(map(str, *list_of_urls))


def run_urls():
    urls = input('Enter amount of Urls: ')
    for i in range(int(urls)):
        ran_num()
        ran_let()
        shuffle_list()
        print("http://", urls_list(), ".onion", sep='')

