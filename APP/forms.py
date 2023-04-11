from django import forms
from .models import *

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = [ 'user_name', 'password', 'name', 'surname']
        widgets = {'password': forms.PasswordInput()}



class PublicationsForm(forms.Form):
    user_name = forms.EmailField()
    date_publication = forms.DateField()
    publication = forms.CharField(max_length=50)
    price_publication = forms.IntegerField()
    publication_sell = forms.BooleanField()


class PurchasesForm(forms.Form):
    user_name = forms.EmailField()
    date_purchase = forms.DateField()
    purchase = forms.CharField(max_length=50)
    price_purchase = forms.IntegerField()


