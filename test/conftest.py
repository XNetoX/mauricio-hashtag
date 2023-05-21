import pytest


@pytest.fixture(scope="session")
def api_test_config(database_uri):
    class APITestConfig:
        SECRET_KEY = "test"
        SQLALCHEMY_DATABASE_URI = database_uri
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        PROPAGATE_EXCEPTIONS = True
        DEBUG = True
        TESTING = True
        ENV = "test"
        WTF_CSRF_ENABLED = False
        BCRYPT_LOG_ROUNDS = 4
        SWAGGER = {}
        CACHE_TYPE = "SimpleCache"
        CACHE_DEFAULT_TIMEOUT = 300
        DEBUG_TB_ENABLED = True
        DEBUG_TB_INTERCEPT_REDIRECTS = False
        DEBUG_TB_PROFILER_ENABLED = True

    return APITestConfig()


@pytest.fixture(scope="session")
def api(api_test_config):
    api = create_api(api_test_config)
    api_context = api.app_context()
    api_context.push()
    yield api
    api_context.pop()


@pytest.fixture(scope="session")
def database(api):
    api.db.create_all()
    yield api.db
    api.db.drop_all()


@pytest.fixture(scope="function", autouse=True)
def cleanup_tables(database):
    yield
    database.session.query(MovingCompany).delete()
    database.session.commit()


@pytest.fixture
def session(database):
    session = database.session
    yield session
    session.rollback()
    session.expunge_all()
    session.close()


@pytest.fixture
def api_client(api):
    api_client = api.test_client()
    api_client.testing = True
    yield api_client
