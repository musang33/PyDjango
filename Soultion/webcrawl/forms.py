from django import forms

class RssAddressForm(forms.Form):
    rss_address = forms.CharField(label='Rss Address', max_length=100)