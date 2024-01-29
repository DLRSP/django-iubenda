"""Test's urls view for django-iubenda"""

from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from django.views.i18n import JavaScriptCatalog

from iubenda.sitemaps import CookieSitemap, PrivacySitemap

sitemaps = {
    "privacy": PrivacySitemap,
    "cookie": CookieSitemap,
}

urlpatterns = [
    path("", include("iubenda.urls")),
    path("admin/", admin.site.urls),
]

urlpatterns += i18n_patterns(
    re_path(r"^jsi18n/$", JavaScriptCatalog.as_view(), name="javascript-catalog"),
    path("", include("iubenda.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
)
