import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2)7uie8rx$co!=7yfiw6yeprk%^ow-z9oj62+zc^ih9v6l-y1#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'player',
    'report',
    'user_auth',
    'article',
    'scout',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'draft_preview.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'draft_preview.wsgi.application'

# PAYMENTS_PLANS = {
#     "monthly": {
#         "stripe_plan_id": "pro_monthly",
#         "name": "Membership",
#         "description": "Monthly subscription to ITP",
#         "price": 20,
#         "interval": "month"
#     }
# }

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },

    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'itp',
    #     'USER': 'itp',
    #     'PASSWORD': 'Supervisor123!dragonRE',
    #     # 'HOST': '10.40.2.201',
    #     'HOST': '163.182.170.171',
    #     'PORT': '5432'
    # }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STRIPE_PUBLIC_KEY = 'pk_test_hgRJMtynoIUxQNn1JPzpj6jT'
STRIPE_SECRET_KEY = 'sk_test_i26a5CCLPSFVf4BkdmwEscEU'
# PINAX_STRIPE_API_VERSION = '2015-10-16'
# PINAX_STRIPE_INVOICE_FROM_EMAIL = 'billing@itp.com'
# PINAX_STRIPE_DEFAULT_PLAN = None
# PINAX_STRIPE_SEND_EMAIL_RECIEPTS = True
# PINAX_STRIPE_SUBSCRIPTION_REQUIRED_EXCEPTION_URLS = []
# PINAX_STRIPE_SUBSCRIPTION_REQUIRED_REDIRECT = None
# PINAX_STRIPE_SUBSCRIPTION_TAX_PERCENT =
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
SITE_ID = 1
STATIC_URL = '/static/'
STATIC_PATH = os.path.join(BASE_DIR, 'static')
LOGIN_SUCCESS_URL = '/'
