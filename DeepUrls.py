import random
import string
import requests

# initialize variables
class DU:
    def __init__(self):
        self.num = None
        self.random_number = None
        self.nums_list = None
        self.letters = None
        self.ran_letters = None
        self.combine_lists = None
        self.ran_list = None
        self.dark_url = None
        self.list_of_urls = None
        self.listing = None
        self.test_url = None
        self.session = None
        self.r = None
        self.urls = None
        self.active_urls = None
        self.scrapping_session = None
        self.scrapping_r = None

# Find and search dark web urls script
    def http_or_https(self):
        self.num = random.randint(0, 1)
        if self.num == 0:
            return 's'
        else:
            return ''

    def ran_num(self):
        self.random_number = random.randint(1, 20)
        self.nums_list = random.sample(range(0, self.random_number), self.random_number)
        return self.nums_list

    def ran_let(self):
        self.letters = [i for i in string.ascii_letters]
        self.ran_letters = random.sample(self.letters, random.randint(5, 33))
        return self.ran_letters

    def shuffle_list(self):
        self.combine_lists = self.ran_num() + self.ran_let()
        self.ran_list = random.sample(self.combine_lists, len(self.combine_lists))
        return self.ran_list

    def urls_list(self):
        self.dark_url = ''
        self.list_of_urls = []
        self.listing = self.shuffle_list()
        self.list_of_urls.append(self.listing)
        self.dark_url = f'http{self.http_or_https()}://{"".join(map(str, *self.list_of_urls))}.onion'
        return self.dark_url
        # return "http://s4k4ceiapwwgcm3mkb6e4diqecpo7kvdnfr5gg7sph7jjppqkvwwqtyd.onion/"

    def test_url(self):
        self.test_url = "http://s4k4ceiapwwgcm3mkb6e4diqecpo7kvdnfr5gg7sph7jjppqkvwwqtyd.onion/"
        # self.test_url = "http://A1017QWV16FSDYXrymxIsz81LZhBf2R18711M50n13w619U914N15412a3Ej.onion"
        return self.test_url

    def tor_url_response(self):
        try:
            self.session = requests.session()
            self.session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}
            # print(urls_list.dark_url)
            self.r = self.session.get(str(self.urls_list()))
            # self.r = self.session.get(f'{self.urls_list()}')
            # tor_url_response.r = session.get(test_url())
            return self.r.status_code
        except requests.exceptions.RequestException:
            return print('Not a Website')

    def active_list(self):
        print(self.tor_url_response())
        if self.tor_url_response() == 200:
            self.active_urls = []
            self.listing = self.urls_list()
            self.active_urls.append(self.listing)
            return print("".join(map(str, *self.active_urls)))

    def run_urls(self):
        self.urls = input('Enter amount of Urls: ')
        for i in range(int(self.urls)):
            self.active_list()
            # print(f"https://{urls_list()}.onion", sep='')

# Web scrapping script
    def tor_content(self, site_content):
        try:
            self.scrapping_session = requests.session()
            self.scrapping_session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}
            self.scrapping_r = self.scrapping_session.get(site_content)
            print(self.scrapping_r.content)
        except Exception as err:
            print("No Content")

    def tor_headers(self, site_headers):
        try:
            self.scrapping_session = requests.session()
            self.scrapping_session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}
            self.scrapping_r = self.scrapping_session.get(site_headers)
            print(self.scrapping_r.headers)
        except Exception as err:
            print("No Headers")