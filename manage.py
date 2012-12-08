#!/usr/bin/env python
from flask.ext.script import Manager, Server
from app import app

# Create the manager
manager = Manager(app)

# This automatically adds the option `runserver`
manager.add_command('runserver', Server(host='0.0.0.0'))

if __name__ == '__main__':
    manager.run()