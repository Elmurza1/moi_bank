from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from users.models import CustomUser


# Create your views here.

class LoginView(TemplateView):
    template_name = 'login-page.html'


class RegisterView(TemplateView):
    template_name = 'registration-page.html'


class MakeRegistrationView(View):
    """ вьшка для регистрации пользователя """
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
        return render(request, 'profile-page.html', {'message': 'Регистрация прошла успешно'})