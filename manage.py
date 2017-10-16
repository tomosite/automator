#!/usr/bin/env python3.5
import os

from flask_assets import ManageAssets, Environment
from app import create_app

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from datetime import datetime, timedelta
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command("assets", ManageAssets(app.jinja_env.assets_environment))

if __name__ == '__main__':
    manager.run()

