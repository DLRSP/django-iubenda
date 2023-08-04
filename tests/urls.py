"""Test's urls view for django-iubenda"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path("", include("iubenda.urls")),
    path("admin/", admin.site.urls),
]

urlpatterns += i18n_patterns(
    re_path(r"^jsi18n/$", JavaScriptCatalog.as_view(), name="javascript-catalog"),
    path("", include("iubenda.urls")),
)
