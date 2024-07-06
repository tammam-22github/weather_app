from django.contrib.sitemaps import Sitemap


class SiteMap(Sitemap):
    change_freq='weekly'
    priority=0.9