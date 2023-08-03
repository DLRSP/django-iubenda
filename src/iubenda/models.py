from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import gettext_lazy as _


class Iubenda(models.Model):
    site = models.ForeignKey(
        Site, verbose_name=_("Django Site"), on_delete=models.CASCADE
    )
    iub_site_id = models.IntegerField(verbose_name=_("Iubenda Site ID"), unique=True)
    iub_policy_id = models.IntegerField(
        verbose_name=_("Iubenda Policy ID"), unique=True
    )
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Iubenda Policy")
        verbose_name_plural = _("Iubenda Policies")
