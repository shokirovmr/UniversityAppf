from django import forms
from django.forms import ModelForm

from bookshop.models import Publisher, Store


class PublisherCreateForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ["name", "is_active"]


class StoreCreateForm(ModelForm):
    class Meta:
        model = Store
        fields = ["name", "books"]
