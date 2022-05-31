import random
import string
import requests


def http_or_https():
    num = random.randint(0, 1)
    if num == 0:
        return 's'
    else:
        return ''


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


def test_url():
    # return "http://s4k4ceiapwwgcm3mkb6e4diqecpo7kvdnfr5gg7sph7jjppqkvwwqtyd.onion/"
    return "http://A1017QWV16FSDYXrymxIsz81LZhBf2R18711M50n13w619U914N15412a3Ej.onion"


def tor_url_response():
    try:
        session = requests.session()
        session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}
        r = session.get(f'http{http_or_https()}://{urls_list()}.onion/')
        # r = session.get(f'{urls_list()}')
        return r.status_code
    except requests.exceptions.RequestException:
        return None


def active_list():
    print(tor_url_response())
    if tor_url_response() == 200:
        list_of_urls = []
        listing = urls_list()
        list_of_urls.append(listing)
        return print("".join(map(str, *list_of_urls)))


def tor_content(site_content):
    try:
        session = requests.session()
        session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}
        r = session.get(site_content)
        print(r.content)
    except Exception as err:
        print("No Content")


def tor_headers(site_headers):
    try:
        session = requests.session()
        session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}
        r = session.get(site_headers)
        print(r.headers)
    except Exception as err:
        print("No Headers")


def run_urls():
    urls = input('Enter amount of Urls: ')
    for i in range(int(urls)):
        active_list()
        # print(f"https://{urls_list()}.onion", sep='')

