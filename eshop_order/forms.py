from django import forms
from eshop_products_attrebute.models import ProductAttribute
from eshop_products.models import Product

colors = [('قرمز', 'قرمز'), ('آبی', 'آبی'), ('زرد', 'زرذ'), ('صورتی', 'صورتی')]
sizes = [("X", "X"), ("XL", "XL"), ("XXL", "XXL"), ("XXXL", "XXXL"), ("L", "L")]


class UserAddOrder(forms.Form):
    productId = forms.IntegerField(
        widget=forms.HiddenInput(),
    )

    color = forms.ChoiceField(
        widget=forms.Select, choices=colors)

    size = forms.ChoiceField(
        widget=forms.Select, choices=sizes
    )

    count = forms.IntegerField(
        widget=forms.NumberInput(),
        initial=1
    )