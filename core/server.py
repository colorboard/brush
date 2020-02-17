from packages.manager import Manager


class Server:
    def __init__(self, start_app=None):
        self.manager = Manager()

        self.running_package = None
        if start_app: self.open(start_app)

    def open(self, package):
        if self.running_package: self.running_package.stop()

        self.running_package = \
            [package_object for package_object in self.manager.installed if package_object.package == package][0]
        self.running_package.run(threaded=True)
