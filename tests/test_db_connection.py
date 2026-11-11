import pytest
from unittest.mock import patch

from sqlalchemy.engine import URL

from src import db_connection as dc


def set_database_environment(monkeypatch):
    monkeypatch.setenv("DB_USER", "test_user")
    monkeypatch.setenv("DB_PASSWORD", "test_password")
    monkeypatch.setenv("DB_HOST", "localhost")
    monkeypatch.setenv("DB_PORT", "5432")
    monkeypatch.setenv("DB_NAME", "test_database")


def test_get_engine_uses_environment_variables(monkeypatch):
    set_database_environment(monkeypatch)

    with patch.object(dc, "create_engine") as mock_create_engine:
        dc.get_engine()

        mock_create_engine.assert_called_once()

        connection_url = mock_create_engine.call_args.args[0]
        options = mock_create_engine.call_args.kwargs

        assert isinstance(connection_url, URL)
        assert connection_url.drivername == "postgresql+psycopg"
        assert connection_url.username == "test_user"
        assert connection_url.password == "test_password"
        assert connection_url.host == "localhost"
        assert connection_url.port == 5432
        assert connection_url.database == "test_database"
        assert options["pool_pre_ping"] is True


def test_get_engine_uses_default_port(monkeypatch):
    set_database_environment(monkeypatch)
    monkeypatch.delenv("DB_PORT")

    with patch.object(dc, "create_engine") as mock_create_engine:
        dc.get_engine()

        connection_url = mock_create_engine.call_args.args[0]

        assert connection_url.port == 5432


def test_get_engine_rejects_invalid_port(monkeypatch):
    set_database_environment(monkeypatch)
    monkeypatch.setenv("DB_PORT", "invalid")

    with pytest.raises(ValueError):
        dc.get_engine()


def test_get_engine_handles_missing_credentials(monkeypatch):
    for variable in [
        "DB_USER",
        "DB_PASSWORD",
        "DB_HOST",
        "DB_NAME",
    ]:
        monkeypatch.delenv(variable, raising=False)

    with patch.object(dc, "create_engine") as mock_create_engine:
        dc.get_engine()

        connection_url = mock_create_engine.call_args.args[0]

        assert connection_url.username is None
        assert connection_url.password is None
        assert connection_url.host is None
        assert connection_url.database is None
