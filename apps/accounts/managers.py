from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    '''Override create_user and create_superuser methods'''

    def create_user(self, email, password, **kwargs):

        if not email:
            raise ValueError("Email field is required")

        if not password:
            raise ValueError("Password field is required")

        email = self.normalize_email(email)

        user = self.model(email= email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        return self.create_user(email=email, password=password,
                                    is_superuser=True, is_staff= True, is_active= True)