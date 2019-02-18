from django import forms

from .models import Nums

class CalcForm(forms.ModelForm):
   class Meta:
      model = Nums
      fields = ('nums',)

