from __future__ import unicode_literals

from django.apps import AppConfig


class ShortLinksConfig(AppConfig):
    name = 'short_links'

    def ready(self):
        import short_links.signals
