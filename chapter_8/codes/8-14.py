def car_info(manufacturer, model, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model

    return kwargs

car = car_info('subaru', 'outback', color='blue', tow_package=True)

print(car)