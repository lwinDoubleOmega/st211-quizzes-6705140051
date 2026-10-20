from unittest.mock import patch
from weater import describe_weather

def test_hot_weather():
    with patch('weater.get_temperature', return_value=30):
        assert describe_weather() == "Hot"

def test_freezing_weather():
    with patch('weater.get_temperature', return_value=-5):
        assert describe_weather() == "Freezing"

def test_cold_weather():
    with patch('weater.get_temperature', return_value=10):
        assert describe_weather() == "Cold"

def test_warm_weather():
    with patch('weater.get_temperature', return_value=20):
        assert describe_weather() == "Warm"