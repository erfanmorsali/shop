from django import forms


class UserFavouriteProductForm(forms.Form):
    productId = forms.IntegerField(
        widget=forms.HiddenInput(),
    )
