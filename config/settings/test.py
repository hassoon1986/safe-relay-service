"""
With these settings, tests run faster.
"""

from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env("DJANGO_SECRET_KEY", default="q8lVkJGsIiHcTSQKaWIBsMVPOGnCnF6f7NDGup8KdDNmviSaZVhP0Nq3q3MolmFU")
# https://docs.djangoproject.com/en/dev/ref/settings/#test-runner
TEST_RUNNER = "django.test.runner.DiscoverRunner"

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache", "LOCATION": ""
    }
}

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = "localhost"
# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 1025

# CELERY
CELERY_ALWAYS_EAGER = True

# Test using ganache account 9
ETHEREUM_TEST_PRIVATE_KEY = 'b0057716d5917badaf911b193b12b910811c1497b5bada8d7711f758981c3773'

# SAFE
# Ganache #1 and #2 private keys
SAFE_FUNDER_PRIVATE_KEY = '0x6cbed15c793ce57650b9877cf6fa156fbef513c4e6134f022a85b1ffdd59b2a1'
SAFE_TX_SENDER_PRIVATE_KEY = '0x6370fd033278c143179d81c5526140625662b8daa446c22ee2d73db3707e620c'
SAFE_FUNDING_CONFIRMATIONS = 0
FIXED_GAS_PRICE = 1
SAFE_CONTRACT_ADDRESS = '0x2727D69C0BD14B1dDd28371B8D97e808aDc1C2f7'
SAFE_OLD_CONTRACT_ADDRESS = '0x8942595A2dC5181Df0465AF0D7be08c8f23C93af'
SAFE_PROXY_FACTORY_ADDRESS = '0x3327d69c0bd14B1DDD28371B8D97E808Adc1c2F7'
