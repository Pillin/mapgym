# -*- coding: utf-8 -*-
from optparse import make_option
from termcolor import colored
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType


class Seed(BaseCommand):
    help = 'Pobla la BD'
    option_list = BaseCommand.option_list + (
        make_option('--noimg',
                    action='store_true',
                    dest='noimg',
                    default=False,
                    help='Ignora la creacion de imagenes de productos'),

        make_option('--clearimg',
                    action='store_true',
                    dest='clearimg',
                    default=False,
                    help='Limpia carpeta items de uploads previo a la importacion de items'),
    )

    def clean(self, model_name):
        log_text = '{model}{spaces}limpiando... '.format(
            model=colored(
                model_name,
                'blue',
                attrs=['bold']
            ),
            spaces=" "*(30-len(model_name))
        )
        self.stdout.write(u'' + log_text, ending='')
        self.stdout.write(' ' * (30 - len(log_text)), ending='')
        self.stdout.flush()

        filters = {'model': model_name}
        model = ContentType.objects.get(**filters).model_class()
        count = model.objects.count()
        while model.objects.count():
            objs = model.objects.all()[:10]
            model.objects.filter(pk__in=[obj.pk for obj in objs]).delete()

        self.stdout.write('({}){}{} '.format(
            count,
            ' ' * (6-len(str(count))),
            colored('OK', 'green', attrs=['bold'])))

    def create(self, model):
        log_text = '{model}{spaces}creando...   '.format(
            model=colored(
                model,
                'blue',
                attrs=['bold']
            ),
            spaces=" " * (30-len(model))
        )
        self.stdout.write(u'' + log_text, ending='')
        self.stdout.write(' ' * (30 - len(log_text)), ending='')
        self.stdout.flush()
        self.funs[model]()

        filters = {'model': model}
        model = ContentType.objects.get(**filters).model_class()
        count = model.objects.count()
        self.stdout.write('({}){}{} '.format(
            count,
            ' ' * (6-len(str(count))),
            colored('OK', 'green', attrs=['bold']))
        )

    def handle(self, *args, **options):
        self._init(**options)
        for model in sorted(self.funs.keys(), reverse=True):
            self.clean(model)

        for model in self.funs.keys():
            self.create(model)
