from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models
import uuid


class User(AbstractUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(verbose_name='First name', max_length=255, null=False)
    last_name = models.CharField(verbose_name='Last name', max_length=255, null=False)
    phone = models.CharField(verbose_name='Phone', max_length=255, null=False)
    telegram = models.CharField(verbose_name='Telegramm', max_length=255, null=False)
    avatar = models.ImageField(verbose_name='Profile photo', null=True, blank=True, upload_to='avatars')
    last_time_visit = models.DateTimeField(verbose_name='Last visit', default=timezone.now)
    volume_PV = models.FloatField(verbose_name='Personal volume', max_length=255, default=0.00)
    volume_APV = models.FloatField(verbose_name='All time Personal volume', max_length=255, default=0.00)
    volume_GV = models.FloatField(verbose_name='Group volume', max_length=255, default=0.00)
    volume_AGV = models.FloatField(verbose_name='All time group volume', max_length=255, default=0.00)
    volume_NV = models.FloatField(verbose_name='Network volume', max_length=255, default=0.00)
    volume_ANV = models.FloatField(verbose_name='All time network volume', max_length=255, default=0.00)
    volume_QV = models.FloatField(verbose_name='Quatification volume', max_length=255, default=0.00)
    rang = models.CharField(verbose_name='Rang', max_length=255, default='Client')
    cashback = models.FloatField(verbose_name='Cashback', max_length=255, default=0.00)
    client_bonus = models.FloatField(verbose_name='Client bonus', max_length=255, default=0.00)
    team_bonus = models.FloatField(verbose_name='Team bonus', max_length=255, default=0.00)
    ref_link = models.UUIDField(verbose_name='Referal link', default=uuid.uuid4)
    partner_balance = models.FloatField(verbose_name='Partner balance', max_length=255, default=0.00)
    personal_balance = models.FloatField(verbose_name='Personal balance', max_length=255, default=0.00)
    personalID = models.IntegerField(verbose_name='Personal ID', default=1)
    clients_count = models.IntegerField(verbose_name='Clients count', default=0)
    partners_count = models.IntegerField(verbose_name='Partners count', default=0)
    clicks = models.IntegerField(verbose_name='Clicks', default=0)
    partner_reward = models.FloatField(verbose_name='Partner rewards', max_length=255, default=0.00)
    wallet_usdt = models.CharField(verbose_name='USDT Wallet', max_length=255, blank=True,default="Write your USDT wallet")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class UserToken(models.Model):
    user_id = models.IntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()


class Reset(models.Model):
    email = models.EmailField(max_length=255)
    token = models.CharField(max_length=255, unique=True)