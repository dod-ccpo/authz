import pytest

from authz.make_app import make_app, make_config


@pytest.fixture
def app():
    app = make_app(make_config())

    context = app.app_context()
    context.push()

    db = app.extensions["sqlalchemy"].db

    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    yield app

    transaction.rollback()
    connection.close()
    session.remove()
    context.pop()
