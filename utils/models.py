from __future__ import unicode_literals

import googlemaps
from django.conf import settings


class GoogleMapApi:
    class __GoogleMapApi:
        def __init__(self):
            self.gmaps = googlemaps.Client(key=settings.API_KEY_GOOGLE)

        def __str__(self):
            return repr(self)

        def get_coords(self, street, number):
            return self.gmaps.geocode("%s %s" % (street, number))

    instance = None

    def __init__(self):
        if not GoogleMapApi.instance:
            GoogleMapApi.instance = GoogleMapApi.__GoogleMapApi()

    def __getattr__(self, name):
        return getattr(self.instance, name)
