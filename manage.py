import os

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db

<<<<<<< HEAD
# app = create_app(os.environ.get('CONFIG_OPTION'))
app = create_app("development")
=======
<<<<<<< HEAD
app = create_app(os.environ.get('APP_SETTINGS'))
=======
# app = create_app(os.environ.get('CONFIG_OPTION'))
app = create_app('development')
>>>>>>> ba86ec7ade79a936b81e04ee8b80a97cf8f97770

>>>>>>> c6210a6f03e451f1b89fc05be33219256516393a
manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db)


if __name__ == '__main__':
    manager.run()