from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import (
    AbstractUser
)


class Member(AbstractUser):
    contact_no = models.CharField(max_length=10, validators=[
        RegexValidator(regex='^.{10}$', message='Contact number must be of length 10', code='nomatch')])


class MemberProfile(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
     #address = models.CharField(max_length=500)
    date_of_birth = models.DateField(null=True, default=None)
    profile_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.member.first_name} Profile'



