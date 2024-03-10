import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_phone_number(value):
    phone_regex = r"^09[0-9]{9}$"

    if not re.match(phone_regex, value):
        raise ValidationError(_("Invalid phone number."))
