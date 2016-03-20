# -*- coding: utf-8 -*-
import urllib2
import re
from bs4 import BeautifulSoup
from collections import OrderedDict
from pacific.seed import Seed
from branch_office.models import BranchOffice
from commons.models import Direction


class Command(Seed):
    help = 'Pobla la BD con la sucursales'
    PREFIX = 'http://www.gimnasiopacific.cl/'
    URL = PREFIX + 'sucursales.html'

    def replace_all(self, stg, dict_obj):
        for elem in dict_obj:
            stg = stg.replace(elem.keys()[0], elem.values()[0])
        return stg

    def _proccess_direction(self, direction):
        patron = re.match(r"[\w|\xf3]+: (?P<name>[\w\ \.\-]*)[\xb0|\#|\ ]*(?P<number>[\d]+)[\,|\ |\-|\n]*[\w\.\d\ \-\/]*", direction)

        name = patron.groupdict()['name'].strip()
        number = int(patron.groupdict()['number'].strip())
        direction = Direction.objects.create(
            street=name,
            number=number
        )
        return direction

    def _create_branch_office(self, url):
        req_branch_office = urllib2.Request(
            Command.PREFIX + url
        )
        the_page = BeautifulSoup(
            urllib2.urlopen(req_branch_office).read(),
            "html.parser"
        )
        direction, fono, mail, schedule = the_page.find_all('td')
        if not direction.get_text():
            print "no hay direction"
        try:
            direction_obj = self._proccess_direction(direction.get_text())
            BranchOffice.objects.create(
                name=the_page.find('h3').string,
                direction=direction_obj
            )
        except:
            print direction.get_text()

    def _create_branch_offices(self):
        req = urllib2.Request(Command.URL)
        response = urllib2.urlopen(req)
        the_page = BeautifulSoup(response.read(), "html.parser")
        for link in the_page.find_all('a'):
            if link.get('onclick'):
                self._create_branch_office(link.get('href'))

    def _init(self, **options):
        self.funs = OrderedDict()
        self.funs['branchoffice'] = self._create_branch_offices
        self.noimg = options['noimg']
        self.clearimg = options['clearimg']
