from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from . import validators


class UserManager(BaseUserManager):

    def create_user(self, first_name, last_name, username, email, password=None):
        """
        Creates and saves a user with given first name, last name,
        username, email and password.
        """
        if not first_name:
            raise ValueError(_("Users must have a first name."))
        if not last_name:
            raise ValueError(_("Users must have a last name."))
        if not username:
            raise ValueError(_("User must have an username."))
        if not email:
            raise ValueError(_("User must have an email address."))

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        """
        Creates and saves a superuser with the given first name, last name,
        username, email and password.
        """
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
        )

        user.is_active = True
        user.is_staff = True
        user.is_admin = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    first_name = models.CharField(verbose_name=_("First Name"), max_length=255)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=255)
    username = models.CharField(verbose_name=_("Username"), max_length=255, unique=True)
    slug = models.CharField(
        verbose_name=_("Slug"), max_length=255, blank=True, unique=True
    )
    email = models.EmailField(verbose_name=_("Email"), max_length=255, unique=True)
    phone_number = models.CharField(
        verbose_name=_("Phone Number"),
        max_length=11,
        blank=True,
        null=True,
        validators=[validators.validate_phone_number],
        unique=True,
    )
    image = models.ImageField(verbose_name=_("Image"), upload_to="image/user")

    created_at = models.DateTimeField(
        verbose_name=_("Creation Date"), auto_now_add=True
    )
    updated_at = models.DateTimeField(verbose_name=_("Modified Date"), auto_now=True)
    is_active = models.BooleanField(verbose_name=_("Is Active"), default=False)
    is_staff = models.BooleanField(verbose_name=_("Is Staff"), default=False)
    is_admin = models.BooleanField(verbose_name=_("Is Admin"), default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name", "email"]

    objects = UserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        # create slug based on username when creating new user
        if not self.id:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
