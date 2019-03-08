from django import forms
from .models import GarageSellModel


class GarageSellForm(forms.ModelForm):
    class Meta:
        model = GarageSellModel
        fields = "__all__"
