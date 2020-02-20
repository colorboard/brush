from packages.manager import Manager

from flask import Flask, jsonify

app = Flask(__name__)
manager = Manager()
manager.running_package = False


class Screen:
    @app.route('/packages/open/<string:identifier>')
    def open(identifier):
        if manager.running_package:
            manager.running_package.stop()
        manager.running_package = [details for details in manager.installed if details.identifier == identifier][0]
        manager.running_package.run(threaded=True)
        return dict(status=1, message='Application is started.')

    @app.route('/packages/installed')
    def get_installed_packages():
        return jsonify([details.raw for details in manager.installed])

    @app.route('/packages/repository')
    def get_repository_packages():
        return jsonify([details.raw for details in manager.repository.packages])

    @app.route('/packages/install/<string:identifier>')
    def install_package(identifier):
        result = manager.install(identifier)
        return dict(status=result.status, message=result.message)

    @app.route('/packages/delete/<string:identifier>')
    def delete_package(identifier):
        if manager.running_package:
            manager.running_package.stop()
        result = manager.delete(identifier)
        return dict(status=result.status, message=result.message)

    @app.route('/packages/running')
    def running_package():
        return manager.running_package.identifier if manager.running_package else ''

    def start(self):
        app.run(debug=True, port=5000, host='192.168.1.25')
