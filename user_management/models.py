from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
import uuid
from base.models import pyrl_company
# Create your models here.



# Custom user manager
class PyrlUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email must be set')
        if not password:
            raise ValueError('Password must be set')
        
        uuid_generator = uuid.uuid5(namespace=uuid.NAMESPACE_URL, name=email)
        user = self.model(email=self.normalize_email(email=email), uuid=uuid_generator)
        user.set_password(password)
        user.save(using=self._db)

    def create_superuser(self, email, password):
        if not email:
            raise ValueError('Email must be set')
        if not password:
            raise ValueError('Password must be set')
        
        uuid_generator = uuid.uuid5(namespace=uuid.NAMESPACE_URL, name=email)
        user = self.model(email=self.normalize_email(email=email), uuid=uuid_generator)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.mfa_enabled = False
        user.mfa_type = 'sm'
        user.mfa_code = 0
        user.company_id = 1
        user.save(using=self._db)



# Custom user model
class PyrlUser(AbstractBaseUser):
    # Meta class
    class Meta:
        db_table = 'users'

    # Unique identifiers for the user
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    # Login information
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=120, unique=True)

    # Password for authentication
    password = models.CharField(max_length=120)

    # User permissions
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_root = models.BooleanField(default=False)
    company = models.ForeignKey(pyrl_company, on_delete=models.CASCADE)

    # Model-specific metadata
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    # Extra fields
    first_name = models.CharField(max_length=100)
    middle_names = models.CharField(max_length=200)
    last_name = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=100)

    mfa_enabled = models.BooleanField(default=False, verbose_name="MFA Enabled", null=True, blank=True)
    mfa_type = models.CharField(max_length=2, verbose_name="MFA Type", choices=[('sm', 'sms'), ('em', 'email')], null=True, blank=True)
    mfa_code = models.IntegerField(verbose_name="MFA Code", null=True, blank=True)

    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    objects = PyrlUserManager()

    # Authentication functions
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    # Misc functions

    # Special functions
    def __str__(self):
        return f'User {self.primary_key} {self.email}'