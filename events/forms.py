from django import forms
from .models import *


class EventsAdminForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))

    class Meta:
        model = Events
        fields = "__all__"