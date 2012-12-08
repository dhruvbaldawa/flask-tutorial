#!/usr/bin/env python
from flask.ext.script import Manager, Server
from app import app
from db import db

# Create the manager
manager = Manager(app)

# This automatically adds the option `runserver`
manager.add_command('runserver', Server(host='0.0.0.0'))

@manager.command
def init_db():
    print('Building models.')
    db.create_all()
    print('Done.')
    # Create some sample users
    from models import User
    user1 = User(username='foo', password='bar', name='Foo Bar')
    user2 = User(username='admin', password='password', name='Admin')
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

@manager.command
def drop_db():
    print('Dropping models.')
    db.drop_all()
    print('Done.')

@manager.command
def reload_db():
    print('Dropping models.')
    db.drop_all()
    print('Creating models.')
    db.create_all()
    print('Done.')

if __name__ == '__main__':
    manager.run()