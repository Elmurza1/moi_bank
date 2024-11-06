from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    """кастомный менеджер для модели CustomUser"""
    def create_user(self, phone_number, password, **extra_fields):
        """создает и сохраняет нового пользователя с паролем"""
        if not phone_number:
            raise ValueError("Пожалуйста, введите номер телефона.")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        """создает и сохраняет нового суперпользователя с паролем"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(phone_number, password, **extra_fields)
