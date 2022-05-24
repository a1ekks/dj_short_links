# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django import forms
from models import ShortLink


class ShortUrlForm(ModelForm):
    """
    Form class for validate url
    """

    link_orig = forms.URLField(
        label=u'Url', max_length=200,
        error_messages={'required': u'Укажите url'},
        widget=forms.TextInput(
            attrs={'placeholder': 'http://example.com'}
        )
    )

    class Meta:
        model = ShortLink
        fields = ("link_orig",)
