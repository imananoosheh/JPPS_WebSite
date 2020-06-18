import os




BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 'r9s)9!)c_30jlf=h6-!4fosn02r=z#+n32o*wmm-+p6ud+@iyl'

DEBUG = False

ALLOWED_HOSTS = ['www.javid.school','localhost','javid.school']
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
SECURE_BROWSER_XSS_FILTER = True

ADMINS = (('Webmaster','yazdanpanah.aly@gmail.com'))
MANAGERS = ADMINS

GOOGLE_RECAPTCHA_SECRET_KEY = '6LdtVFUUAAAAALXJ6LnrZRK6QD8vblZbOn59XdRo'

# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'ckeditor_uploader',
    'landing',
    'contactUs',
    'galleryApp',
    'newsApp',
    'staffApp',
    'facilities',
    'achievements',
    'vision',
    'registration',
    'onlineLearning',
]




MIDDLEWARE_CLASSES = [
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware'
    
]

CKEDITOR_UPLOAD_PATH = "CKuploads/"


SITE_ID = 1

ROOT_URLCONF = 'jpps.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'jpps.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Jpps2',
        'USER': 'root',
        'PASSWORD': 'Ay19961375',
        'HOST' : 'localhost',
        'PORT': '3306', 
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'fa-ir'
#LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

COUNTERVID = 0

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,"static_in_env", "static_root")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'templates'),
    #'/var/www/static/',
]
MEDIA_URL = '/media/'
MEDIA_ROOT = '/opt/jpps_media/'
CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': 'Custom',
            'toolbar_Custom': [
                [ 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates' ],
                [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ],
                [ 'Find', 'Replace', '-', 'SelectAll', '-', 'Scayt' ],
                [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl'],
                [ 'Link', 'Unlink', 'Anchor', 'Image'],
                [  'Table', 'HorizontalRule', 'Smiley', 'SpecialChar' ],
                [ 'Styles', 'Format', 'FontSize' ],
                [ 'TextColor', 'BGColor','-','Maximize', 'uploadimage', 'source'],
            ],
        'extraPlugins' : ','.join(
            [
                'image2',
            ]),
        
    },
}

