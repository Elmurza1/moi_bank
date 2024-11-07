
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from users.models import CustomUser


# Create your views here.

class LoginView(TemplateView):
    template_name = 'login-page.html'


from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib import messages
from django.views import View
from .models import CustomUser

class MakeLoginView(View):
    """Вьюшка для логина"""
    def post(self, request, *args, **kwargs):
        data = request.POST
        phone_number = data.get('phone')
        password = data.get('password')

        try:
            user = CustomUser.objects.get(phone_number=phone_number)
        except CustomUser.DoesNotExist:
            messages.error(request, "Пользователь с таким номером телефона не найден.")
            return redirect('login-url')

        if user.check_password(password):
            login(request, user)
            return redirect('profile-url')
        else:
            messages.error(request, "Неверный пароль.")
            return redirect('login-url')



class RegisterView(TemplateView):
    template_name = 'registration-page.html'

# Create your views here.
class TransactionView(TemplateView):
    """вьюшка для отброжение страницы транзакции"""
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



from django.contrib.auth import login, logout
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

class AddMoneyView(View):
    """Вьюшка для добавления денег к счету"""
    template_name = 'add-money-page.html'
    def post(self, request, *args, **kwargs):
        user = self.request.user
        user.balance  += 100
        user.save()
        context = {'user': user}

        return render(request, self.template_name, context)


class MakeLogoutView(View):
    """Вьюшка для выхода из аккаунта"""
    def post(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'login-page.html', {})


class MakeTransfersView(View):
    """Вьюшка для перевода денег между пользователями"""
    def post(self, request, *args, **kwargs):
        current_useer = self.request.user
        data = request.POST
        phone_number = data['phone']

        try:
            receiver = CustomUser.objects.get(phone_number=phone_number)
        except CustomUser.DoesNotExist:
            return redirect('transactions-url')

        amount = int(data['amount'])


        if amount > current_useer.balance or amount <= 0:
            return redirect('transactions-url')


        current_useer.balance -= amount
        receiver.balance += amount

        current_useer.save()
        receiver.save()

        return redirect('profile-url')


