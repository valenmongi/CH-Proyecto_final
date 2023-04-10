from django import forms

class UsersForm(forms.Form):
    user_name = forms.EmailField()
    password = forms.CharField(max_length=10)
    name = forms.CharField(max_length=10)
    surname = forms.CharField(max_length=10)


class PublicationsForm(forms.Form):
    user_name = forms.EmailField()
    date_publication = forms.DateField()
    publication = forms.CharField(max_length=50)
    price_publication = forms.IntegerField()
    publication_sell = forms.BooleanField()