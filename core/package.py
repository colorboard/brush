from importlib import import_module
from threading import Thread


class DictClass:
    def __init__(self, dict):
        self.__dict__ = dict


class Package:
    """Class that represents a package

    That class has information about installed or cloud package.
    """

    def __init__(self, json):
        self.title = json['title']
        self.description = json['description']
        self.identifier = json['identifier']
        self.version = json['version']
        self.icon = json['icon']
        self.raw = json
        self.__running = self.__instance = False

        self.developer = DictClass(dict=json['developer'])

    @property
    def instance(self):
        if not self.__instance: self.__instance = import_module(
            'packages.' + self.identifier)
        return self.__instance

    def run(self, threaded=True):
        self.__running = True

        if threaded:
            Thread(target=self.run, args=(False,)).start()
            return

        self.instance.setup()
        while self.__running:
            self.instance.frame()

    def stop(self):
        self.__running = False

    def __str__(self):
        return f'{self.title} ({self.version})'
