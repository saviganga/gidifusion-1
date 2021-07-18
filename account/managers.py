from django.contrib.auth.models import BaseUserManager

'''
manager for MyUser model
'''

class MyUserManager(BaseUserManager):

    def _create_users(self, email, password=None, **extra_fields):

        ''' internal function for creating users '''

        # validate email
        if not email:
            raise ValueError('email field is required')

        # normalize email
        email = self.normalize_email(email)

        # create user
        user = self.model(email=email, **extra_fields)

        # set password
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_user(self, email, password=None, **extra_fields):

        ''' function to create normal users '''

        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_users(email, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):

        ''' function to create superusers '''
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('unauthorized access')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('unauthorized access')

        return self._create_users(email, password, **extra_fields)
        
