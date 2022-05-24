# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class ShortLink(models.Model):
    """
    Модель для хранения данных по коротким ссылкам
    """

    link_orig = models.CharField(u'Original Link', max_length=1024)
    link_short = models.CharField(u'Short Link', max_length=1024)
    created = models.DateTimeField(u'Date', auto_now_add=True)
    use = models.IntegerField(u'CntIntUse', default=0)

    def __unicode__(self):
        return u'{}->{}'.format(self.link_orig, self.link_short)

    class Meta:
        verbose_name = u'Short Url'
        verbose_name_plural = u'Short Urls'
