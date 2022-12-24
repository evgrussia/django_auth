from django import forms
from .models import *


class ItemAdminForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))

    class Meta:
        model = Item
        fields = "__all__"