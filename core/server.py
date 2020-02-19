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
        manager.running_package = [details for details in manager.installed if details.package == identifier][0]
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
        result = manager.delete(identifier)
        return dict(status=result.status, message=result.message)

    def start(self):
        app.run(debug=True, port=5000)
