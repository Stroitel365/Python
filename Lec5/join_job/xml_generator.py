from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view


def create(device=1):
    xml = '<xml>\n'
    xml += '   <temperature units = "c">{}<Temperature>\n' \
        .format(temperature_view(device))
    xml += '   <wind_speed units = "m/s">{}<Wind speed >\n' \
        .format(wind_speed_view(device))
    xml += '   <pressure units = "mmHg">{}<Pressure>\n' \
        .format(pressure_view(device))
    xml += '<xml>'

    with open('data.xml', 'w') as page:
        page.write(xml)

    return xml


def new_create(data, device=1):
    t, p, w = data
    t = t * 1.8 + 32
    xml = '<xml>\n'
    xml += '   <temperature units = "f">{}<Temperature>\n' \
        .format(t)
    xml += '   <wind_speed units = "m/s">{}<Wind speed >\n' \
        .format(w)
    xml += '   <pressure units = "mmHg">{}<Pressure>\n' \
        .format(p)
    xml += '<xml>'

    with open('new_data.xml', 'w') as page:
        page.write(xml)

    return data
