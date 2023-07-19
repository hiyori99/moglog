from django import forms
from .models import Shop
from .models import Menu

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('name', 'address', 'visit_count', 'rating')
        labels = {
            'name': 'お店の名前',
            'address': '住所',
            'visit_count': '行った回数',
            'rating': '評価',
        }

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('name', 'menu', 'price', 'description')
        labels = {
            'name': 'メニュー名',
            'menu': '詳細',
            'price': '価格',
            'description': '説明',
        }