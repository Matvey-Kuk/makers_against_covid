from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    CITIES = [
        ('moscow', "Москва"),
        ('spb', "Санкт Петербург"),
    ]

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('Имя'), max_length=30, blank=True)
    last_name = models.CharField(_('Фамилия'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'),default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    city = models.TextField(
        choices=CITIES,
        default=CITIES[0][0],
        verbose_name="Город",
    )

    address = models.TextField(
        verbose_name="Адрес или район",
    )

    contact_data = models.TextField(
        verbose_name="Контактные данные (телефон, телеграм)",
    )

    organization = models.TextField(
        verbose_name="Организация, которую Вы представляете (обязательно для врачей).",
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def is_medic_account_full(self):
        return self.is_maker_account_full and self.organization is not None and self.organization != ""

    def is_maker_account_full(self):
        return None not in (
            self.first_name,
            self.last_name,
            self.city,
            self.contact_data,
            self.address,
        ) and "" not in (
            self.first_name,
            self.last_name,
            self.city,
            self.contact_data,
            self.address,
        )
