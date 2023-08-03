from django.contrib import sitemaps
from django.urls import reverse


class PrivacySitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return ["privacy"]

    def location(self, item):
        return reverse(item)


class CookieSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return ["cookie"]

    def location(self, item):
        return reverse(item)
