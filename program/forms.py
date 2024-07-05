from django import forms
from .models import *


class UserOrderForm(forms.ModelForm):
    card_number = forms.CharField(max_length=16, label='Card number', widget=forms.TextInput(attrs={'class': 'full-width', 'placeholder': '**** **** **** ****'}))
    expiration_date = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'class': 'right-width', 'placeholder': 'MM/YY'}))
    cvv = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class': 'left-width', "placeholder": "XXX"}))
    owner_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'full-width'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'right-width', "placeholder": "+375"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'left-width', "placeholder": "example@gmail.com"}))

    class Meta:
        model = UserOrderModel
        fields = ['card_number', 'expiration_date', 'cvv', 'owner_name', 'phone_number', 'email']

    def clean(self):
        cleaned_data = super().clean()
        card_number = cleaned_data.get('card_number')
        expiration_date = cleaned_data.get('expiration_date')
        cvv = cleaned_data.get('cvv')
        phone_number = cleaned_data.get('phone_number')

        if not card_number or len(card_number) != 16:
            self.add_error('card_number', 'Неверный номер карты. Номер карты должен содержать 16 цифр.')

        if not expiration_date or len(expiration_date) != 5:
            self.add_error('expiration_date', 'Введите корректную дату окончания срока действия карты.')

        if not cvv or len(cvv) != 3:
            self.add_error('cvv', 'CVV-код должен содержать 3 цифры.')

        if not phone_number or len(phone_number) < 10 or len(phone_number) > 15:
            self.add_error('phone_number', 'Введите корректный номер телефона.')

        return cleaned_data

