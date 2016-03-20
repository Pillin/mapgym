# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify


class State(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=u'Nombre'
    )
    slug = models.SlugField()

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = u'Región'
        verbose_name_plural = u'Regiones'

    def save(self, *args, **kwargs):
        """
        Sobreescrito para generar el slug
        """
        if not self.id:
            self.slug = slugify(self.name)

        super(State, self).save(*args, **kwargs)


class Commune(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=u'Nombre'
    )
    state = models.ForeignKey(
        State,
        verbose_name=u'Región'
    )
    slug = models.SlugField()

    def __unicode__(self):
        return "%s %s" % (self.street, self.number)

    class Meta:
        verbose_name = u'Comuna'
        verbose_name_plural = u'Comunas'

    def save(self, *args, **kwargs):
        """
        Sobreescrito para generar el slug
        """
        if not self.id:
            self.slug = slugify(self.name)

        super(Commune, self).save(*args, **kwargs)


class Direction(models.Model):
    street = models.CharField(
        max_length=200,
        verbose_name=u'Calle'
    )
    number = models.PositiveIntegerField(
        default=0,
        verbose_name=u'Número'
    )
    commune = models.ForeignKey(
        Commune,
        null=True,
        blank=True,
        verbose_name=u'Comuna'
    )
    slug = models.SlugField()

    def __unicode__(self):
        return "%s %s" % (self.street, self.number)

    class Meta:
        verbose_name = u'Dirección'
        verbose_name_plural = u'Direcciones'

    def save(self, *args, **kwargs):
        """
        Sobreescrito para generar el slug
        """
        if not self.id:
            self.slug = slugify("%s_%s" % (self.street, self.number))

        super(Direction, self).save(*args, **kwargs)
