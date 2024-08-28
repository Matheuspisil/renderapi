from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, username=None, **extra_fields):
        if not email:
            raise ValueError('O email deve ser definido')

        email = self.normalize_email(email)
        username = username or self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, username=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        username = username or self.normalize_email(email)
        return self.create_user(email, password, username=username, **extra_fields)


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'aluno'),
        (2, 'mentor'),
        (3, 'empresa'),
        (4, 'gestor')
    )
    email = models.EmailField(unique=True)
    user_type = models.PositiveSmallIntegerField(
        choices=USER_TYPE_CHOICES, null=True, blank=True)
    planejamento_preenchido = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.email

# Assuming you have a foreign key relation to another model, e.g. Profile
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField()

# Query optimization example using select_related:
queryset = Profile.objects.select_related('user').all()
