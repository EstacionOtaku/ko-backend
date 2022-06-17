from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
from roles.models import Role


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    role = models.ForeignKey(
        Role,
        on_delete=models.RESTRICT,
        related_name='role'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'role_id']

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email

    def create_user(self, **kwargs):
        user = self.model(
            username=kwargs['username'],
            email=self.normalize_email(kwargs['email'])
        )
        user.set_password(kwargs['password'])
        user.save()
        return user

    def tokens(self):
        token = RefreshToken.for_user(self)
        return {
            'refresh_token': str(token),
            'access_token': str(token.access_token)
        }
