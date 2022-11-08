import requests
import json

from service.maps_service import getLatLon


def getParkingZonesNearby(latlon, limit=10):
    url = f'https://api.golemio.cz/v2/parkingzones/?latlng={"%2C".join([str(x) for x in latlon])}&limit={limit}'

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

    return [(x['properties']['id'], list(reversed(x['properties']['midpoint']))) for x in obj['features']]


if __name__ == "__main__":
    place, coords = getLatLon('Bowling dejvice')
    parking_ids = getParkingZonesNearby(coords, 2)
    print(parking_ids)
