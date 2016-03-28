# -*- coding: utf-8 -*-
from collections import OrderedDict
from pacific.seed import Seed
from branch_office.models import BranchOffice
from utils.models import GoogleMapApi
from commons.models import Commune, State


class Command(Seed):
    help = 'Pobla la BD con la posicion de las sucursales'

    def _position_branch_offices(self):
        instance = GoogleMapApi()
        for elem in BranchOffice.objects.all():
            data = instance.get_coords(
                elem.direction.street,
                elem.direction.number
            )
            try:
                data = data[0]
                street, commune, city, state, country = map(
                    lambda elem: elem.strip(),
                    data['formatted_address'].split(',')
                )

                state_obj, created = State.objects.get_or_create(name=state)
                commune, created = Commune.objects.get_or_create(
                    name=commune,
                    state=state_obj
                )
                elem.direction.lat = data['geometry']['location']['lat']
                elem.direction.lng = data['geometry']['location']['lng']
                elem.direction.commune = commune
            except:
                elem.is_active = False

            elem.direction.save()

    def _init(self, **options):
        self.funs = OrderedDict()
        self._position_branch_offices()
        self.noimg = options['noimg']
        self.clearimg = options['clearimg']
