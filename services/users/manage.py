
import sys 
import unittest
import coverage

from flask.cli import FlaskGroup

#from project import app, db
from project import create_app, db   # nuevo
from project.api.models import User  # nuevo

COV = coverage.coverage(
    branch=True,
    include='project/*',
    omit=[
        'project/tests/*',
        'project/config.py',
    ]
)
COV.start()

app = create_app()  # new
cli = FlaskGroup(create_app=create_app)  # nuevo


#cli = FlaskGroup(app)

# new
@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def test():
    """Ejecuta las pruebas sin cobertura de código"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)

@cli.command("seed_db")
def seed_db():
    """Sembrar la base de datos"""
    db.session.add(User(               # nuevo
        username='juan.gonzales',
        email='juan.gonzales@upeu.edu.pe',
        password='greaterthaneight')
    )
    db.session.add(User(               # nuevo
        username='juangon',
        email='juangon@gmail.com',
        password='greaterthaneight')
    )
    db.session.commit()

@cli.command()
def cov():
    """Ejecuta las pruebas unitarias con cobertura."""
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    sys.exit(result)

if __name__ == '__main__':
    cli()

