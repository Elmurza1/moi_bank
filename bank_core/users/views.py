
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from users.models import CustomUser


# Create your views here.

class LoginView(TemplateView):
    template_name = 'login-page.html'


class RegisterView(TemplateView):
    template_name = 'registration-page.html'

# Create your views here.
class TransactionView(TemplateView):
    """вьюшка для переводов и транзакции"""
    template_name = 'transaction-page.html'


class ProfileView(TemplateView):
    """вьюшка для профиля пользователя"""
    template_name = 'profile-page.html'
    def get_context_data(self, **kwargs):
        user = self.request.user
        context = {
            'user': user
         }
        return context



class MakeMoneyView(TemplateView):
    """вьюшка для добавления денег к счету"""
    template_name = 'add-money-page.html'



from django.contrib.auth import login
from django.shortcuts import redirect

class MakeRegistrationView(View):
    """ Вью для регистрации пользователя """
    def post(self, request, *args, **kwargs):
        data = request.POST
        password = data['password']
        phone_number = data['phone']
        username = data['name']


        user = CustomUser.objects.create_user(
            first_name=username,
            password=password,
            phone_number=phone_number
        )
        user.save()

        login(request, user)
        return redirect('profile-url')
# TODO: сделана показ данных в профиль штмл сделай кнопку так же логин и выход и дороботай мелочи перевод между пользователями
