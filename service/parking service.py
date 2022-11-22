import calendar
import datetime

import requests
import json
from workalendar.europe import CzechRepublic
import holidays

from service.maps_service import getLatLon


def getParkingZonesNearby(latlon, limit=10, range=200):
    url = f'https://api.golemio.cz/v2/parkingzones/?latlng={"%2C".join([str(x) for x in latlon])}&limit={limit}&range={range}'

    payload = {}
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'x-access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.'
                          'eyJlbWFpbCI6ImtyYXRvY2h2aWx0b20wMEBnb'
                          'WFpbC5jb20iLCJpZCI6MTQ3NCwibmFtZSI6bn'
                          'VsbCwic3VybmFtZSI6bnVsbCwiaWF0IjoxNjY'
                          '1Njg5MTYwLCJleHAiOjExNjY1Njg5MTYwLCJp'
                          'c3MiOiJnb2xlbWlvIiwianRpIjoiODZkZmZiM'
                          'WYtYWM2OS00YWM3LTllZmYtZDQwNjA1OWE2Ym'
                          'Q4In0.4KnxAsvpB2fC9vesF5lSJy4joatEouBjVsWvQG0FDmY'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    obj = json.loads(response.text)

    holiday = isHoliday()
    hours = datetime.datetime.today().hour
    minutes = datetime.datetime.today().minute
    for feature in obj['features']:
        addPriceForTariff(feature['properties'], holiday=False, t=(hours, minutes))
    obj['features'] = sorted(obj['features'], key=lambda item: item['properties']['price'])

    return [(x['properties']['id'], list(reversed(x['properties']['midpoint'])), x['properties']['price'],
             x['properties']['tariffs_text']) for x in obj['features']]


def addPriceForTariff(properties, holiday, t):
    tariff_text = properties['tariffs_text']
    if holiday:
        text = tariff_text.split(';')[-1]
        properties['price'] = int(text.split('Kč')[0].split(' ')[-2])
    else:
        text = tariff_text.split(';')[:-1]
        if len(text) == 1:
            properties['price'] = int(text[0].split('Kč')[0].split(' ')[-2])
        elif len(text) == 2:
            properties['price'] = int(text[0].split('Kč')[0].split(' ')[-2])
        else:
            print('WHAAT')

def isHoliday():
    today = datetime.datetime.today()
    return any(x for x in holidays.Czechia(years=[today.year]) if today.date() == x)


if __name__ == "__main__":
    isHoliday()
    place, coords = getLatLon('Narodni muzeum')
    #coords = [50.0789482, 14.4309209]
    parking_ids = getParkingZonesNearby(coords, limit=100, range=1000)
    print("\n".join([f"{i+1}: {str(x)}" for i, x in enumerate(parking_ids)]))
