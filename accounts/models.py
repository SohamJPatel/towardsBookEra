from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import (
    AbstractUser
)


class Member(AbstractUser):
    contact_no = models.CharField(max_length=10, validators=[RegexValidator(regex='^.{10}$', message='Contact number must be of length 10', code='nomatch')])








    
