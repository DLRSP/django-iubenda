from modeltranslation.translator import TranslationOptions, register

from .models import Iubenda


@register(Iubenda)
class IubendaTranslationOptions(TranslationOptions):
    fields = ("iub_policy_id",)
