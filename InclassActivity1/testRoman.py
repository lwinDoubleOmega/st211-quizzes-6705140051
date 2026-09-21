from romanNumeral import convertfromRoman

def test_convert_mcmxciv():
    converter = convertfromRoman("MCMXCIV")
    assert converter.convert() == 1994


def test_convert_xiv():
    converter = convertfromRoman("XIV")
    assert converter.convert() == 14


def test_convert_iv():
    converter = convertfromRoman("IV")
    assert converter.convert() == 4
