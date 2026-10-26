from unittest.mock import Mock
def test_side_effect_list():
    mock = Mock()
    mock.get_data.return_value = [ 1,2
    ]
    assert mock.get_data() == "A"
    assert mock.get_data() == "B"
    assert mock.get_data() == "C"
