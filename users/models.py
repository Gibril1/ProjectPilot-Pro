from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email:str, password:str, **other_fields) -> 'User':
        if not email:
            raise ValueError('User must have email')
        if not password:
            raise ValueError('User must have password')
        
        print('Printing other fields')
        print(other_fields)
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    
    def create_superuser(self,  email:str, password:str, **other_fields) -> 'User':
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True'
            )
        if other_fields.get('is_active') is not True:
            raise ValueError(
                'Superuser must be assigned to is_active=True'
            )
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True'
            )

        user = self.create_user(
            email=email,
            password=password,
            # role=role
            **other_fields
        )

        return user

class User(AbstractUser):
    ROLE_CHOICES = [
        ('HOD', 'HOD'),
        ('Worker', 'Worker')
    ]
    username = None
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100, null=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    other_names = models.CharField(max_length=255, null=True)
    dob = models.DateField(null=True)
    
    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']


