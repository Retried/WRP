import re


class Framework:
    def __init__(self):
        self.slownik = {}

    def route(self, url):
        def impl(function):
            nonlocal url
            self.slownik[function.__name__] = (url, function)
            return function

        return impl

    def url_for(self, name):
        return self.slownik[name][0]

    def routes(self):
        return self.slownik.values()

    def run(self):
        while True:
            user_url = input("GET ")
            for url, fn in self.routes():
                match = re.fullmatch(url, user_url)
                if match:
                    fn()
                    print(match)
                    break
            if not match:
                print("Error 404")
