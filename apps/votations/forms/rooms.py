from votations.models import Room
from django import forms

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('__all__')
