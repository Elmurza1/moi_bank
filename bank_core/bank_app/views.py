from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class TransactionView(TemplateView):
    """вьюшка для переводов и транзакции"""
    template_name = 'transaction-page.html'


class ProfileView(TemplateView):
    """вьюшка для профиля пользователя"""
    template_name = 'profile-page.html'


class MakeMoneyView(TemplateView):
    """вьюшка для добавления денег к счету"""
    template_name = 'add-money-page.html'
