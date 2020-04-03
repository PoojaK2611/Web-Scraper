from django import forms
"""
Purpose: To fetch URL and count of sites to scrape
"""


class SimpleForm(forms.Form):
    url = forms.URLField()
    NumOfSites = forms.IntegerField(label="Number of sites", min_value=1)
