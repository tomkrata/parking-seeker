import requests
import json


def getLatLon(search_query):
    search_query = search_query.replace(' ', '%20')
    url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" \
          f"{search_query}" \
          f"&inputtype=textquery&fields=formatted_address%2Cname%2Crating%2Copening_hours%2Cgeometry&key=" \
          f"AIzaSyAxqtpGpVxUcIzrsHjYL07IgIyijBPE_8Q"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    obj = json.loads(response.text)
    if obj['status'] != 'OK' or len(obj['candidates']) == 0:
        return None, None
    addr = obj['candidates'][0]
    return addr['formatted_address'], [val for (key, val) in addr['geometry']['location'].items()]


if __name__ == "__main__":
    place, coords = getLatLon('Okruzni 484')
    print(f'place: "{place}" is located at {coords[0]},{coords[1]}')
