from city_functions import format_city

def test_formatted_cities():
    result = format_city('santiago', 'chile')
    assert result == 'Santiago, Chile'