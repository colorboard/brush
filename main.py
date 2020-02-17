from core.server import Server

screen = Server()
apps = screen.manager.installed
for app in apps:
    print(app.developer.id)
