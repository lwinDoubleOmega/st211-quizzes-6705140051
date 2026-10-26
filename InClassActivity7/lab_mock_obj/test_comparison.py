from unittest.mock import Mock


def test_comparison():
    mock = Mock()

    def fetch(value):
        return value.upper()

    mock.fetch.side_effect = fetch
    print(mock.fetch("hello"))
    assert mock.fetch("hello") == "HELLO"