# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.text import slugify

# Custom
from commons.models import Direction


class BranchOffice(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name=u'Nombre'
    )
    direction = models.ForeignKey(
        Direction,
        verbose_name=u'Dirección'
    )
    order = models.IntegerField(
        default=0,
        verbose_name=u'Orden'
    )
    slug = models.SlugField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-order"]
        verbose_name = u'Sucursal'
        verbose_name_plural = u'Sucursales'

    def save(self, *args, **kwargs):
        """
        Sobreescrito para generar el slug
        """
        if not self.id:
            self.slug = slugify(self.name)

        super(BranchOffice, self).save(*args, **kwargs)
