import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '6x$h&=^k!^3(t7*#e$a166ner+bl15evghybyicd7=6!jvq7o@'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SENDGRID_SANDBOX_MODE_IN_DEBUG = False
SENDGRID_API_KEY = "fake.api.key"

EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
EMAIL_HOST = "smtp.sendgrid.net"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "fake_user"
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
PUBLIC_ID_LENGTH = 10

FIREBASE_CREDENTIALS_PATH = os.path.join(BASE_DIR, "Techfesia2019", "fake_creds.json")

PAYTM_PRODUCTION = False

PAYTM_MERCHANT_ID = 'JlLJuL45031399299246'

PAYTM_SECRET_KEY = 's_yo0x1u_bow5toi'

PAYTM_WEBSITE = 'WEBSTAGING'

PAYTM_CHANNEL_ID = 'WEB'

PAYTM_INDUSTRY_TYPE_ID = 'Retail'

if PAYTM_PRODUCTION:
    PAYTM_PAYMENT_URL = "https://securegw.paytm.in/order/process/"
else:
    PAYTM_PAYMENT_URL = "https://securegw-stage.paytm.in/order/process/"

