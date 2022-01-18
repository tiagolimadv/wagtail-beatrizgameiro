from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-2&!h!1dqu#013#b5c^xe$r*4cwvl9^r_aw2h#rqlk!5y@cc41t"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

RECAPTCHA_PUBLIC_KEY = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
RECAPTCHA_PRIVATE_KEY = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"
NOCAPTCHA = True
SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]

try:
    from .local import *
except ImportError:
    pass
