def city_country(city, country):
    return city.title() + ", " + country.title()


city = city_country("santiago", "chile")
print(city)
city = city_country("paris", "france")
print(city)
city = city_country("tokyo", "japan")
print(city)