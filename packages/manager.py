from json import loads
from os import listdir
from os.path import join
from shutil import rmtree
from urllib.parse import urljoin
from urllib.request import urlretrieve
from zipfile import ZipFile

from requests import get

from core.package import Package
from core.result import Result


class Repository:
    """Class that represents package repository

    Repository contains information about packages in the cloud
    you can install or update.
    """

    def __init__(self, url='https://colorboard.github.io/repository/'):
        self.url = url

    @property
    def packages(self):
        json_list = get(urljoin(self.url, 'packages.json')).json()
        return [Package(json=json) for json in json_list]

    def download_url(self, package):
        return urljoin(self.url, 'assets/' + package + '.zip')


class Manager:
    """Class that represents packages manager

    Manager was made to delete and install packages.
    """

    def __init__(self, exclude=['manager.py', '__init__.py', '__pycache__', '.DS_Store'], repository=Repository()):
        self.exclude, self.repository = exclude, repository

    @property
    def installed(self):
        files = listdir('packages')
        for file in files.copy():
            if file in self.exclude or file.endswith('.py'):
                files.remove(file)

        return [Package(
            loads(open(join('packages', package, 'manifest.json'), 'r').read())
        ) for package in files]

    def install(self, package):
        """Method that installs the latest version of package

        :param package: str – Package identifier
        :return: Result – Result of installation
        """

        if package in [package.package for package in self.installed]:
            return Result(0, 'Package already installed.')

        try:
            details = [details for details in self.repository.packages if details.package == package][0]
            url = self.repository.download_url(package)
            binary = urlretrieve(url)[0]

            ZipFile(binary).extractall(join('packages', package))
        except Exception as exception:
            return Result(2, f'Exception occurred: {exception}')

        return Result(1, f'Package {details.package} at version {details.version} installed successfully.')

    def delete(self, package):
        """Method that deletes installed package

        :param package: str – Package identifier
        :return: Result – Result of deletion
        """
        if package not in [package.package for package in self.installed]:
            return Result(0, 'Package not installed.')

        rmtree(join('packages', package))
        return Result(1, f'Package {package} was successfully deleted.')
