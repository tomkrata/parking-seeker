# Parking seeker

## Description
The app consists of several pages. Few of them are for auth purposes (Login, Logout, Sign Up). With these pages user can control their session. Profile tab
serves as a session control. Whenever there is a name shown, user is logged in. Without the session parking API is not available.
Parking API is a combination of three APIs.
1) Google Maps API:
    This API is responsible for getting the latitude and longtitude of given string. It works exactly the same as typical google maps search. Any given text results in lat and lon.
    https://maps.googleapis.com/maps/api/place/findplacefromtext
2) Parking API:
    Parking API returns 100 closest parking spaces (blue/purple... lines) for a given latitude and longtitude. The parking spaces are sorted by their price. Since there might be
    different prices on the weekend or on holiday, there is another API which solves just that.
    https://api.golemio.cz/v2/parkingzones
3) Holiday API:
    Personal API which returns whether there is a national holiday in Czech Republic or not.
    request.url_root+"utils/isholiday"

Together they create the core of the app. The documentation of those APIs can be seen in Swagger tab.

## Maps API
Getting latitude and longtitude of certain place given. Works the same as google maps search. Therefore any string given, lat lon will be retrieved.

## Parking API
For a given coordinates gets 'n' closest parking zones.

API gets 100 closest parking spaces and sorts them by their price.

## Holiday API
Personal API which on any day returns true if it is a national holiday in CZE or false otherwise.

## User Interface
Simple web UI created

## Login
Login, logout, sign up and session created. User can use the api only when logged in.

## Deployed
URL of final dockerized product:
https://parking-seeker.herokuapp.com/park
