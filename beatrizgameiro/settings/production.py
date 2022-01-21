from .base import *

DEBUG = int(os.environ.get("DEBUG", default=1))
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = os.environ.get("DJANG_ALLOWED_HOSTS").split(" ")

try:
    from .local import *
except ImportError:
    pass
