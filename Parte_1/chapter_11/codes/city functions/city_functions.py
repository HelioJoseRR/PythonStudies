def format_city(city, country, population=''):
    """Return a formatted string"""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"