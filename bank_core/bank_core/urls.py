"""
URL configuration for bank_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import LoginView, RegisterView, MakeRegistrationView, TransactionView, MakeMoneyView, ProfileView, \
    AddMoneyView, MakeLogoutView, MakeTransfersView, MakeLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProfileView.as_view(), name='profile-url'),
    path('transactions-list/', TransactionView.as_view(), name='transactions-url'),
    path('make-transfers/', MakeTransfersView.as_view(), name='make-transfers-url'),
    path('mining-money-list/', MakeMoneyView.as_view(), name='mining-money-url'),
    path('add-money-list/', AddMoneyView.as_view(), name='add-money-url'),
    path('login-list/', LoginView.as_view(), name='login-url'),
    path('make-login/', MakeLoginView.as_view(), name='make-login-url'),
    path('make-logaut/', MakeLogoutView.as_view(), name='logout-url'),
    path('register-list/', RegisterView.as_view(), name='register-url'),
    path('make-registration/', MakeRegistrationView.as_view(), name='make-register-url')
]
