#-*-coding:utf-8 -*-

"""
Django settings for blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c&tj@x7%__4x^+f3ho+l52tfol+1@#bnw&7vsm7_k3t83sam*g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


#diretorio dos templates

TEMPLATE_DIRS = (
os.path.join(BASE_DIR, 'templates'),

)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	#'djando.contrib.staticfiles.storage.StaticFileStorage',
	
	'artigo',
	'agenda',
	#'gallery',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'blog.urls'

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#====================================================
##Padrão charset a ser usado para todos os objetos HttpResponse, 
#se um tipo MIME não for especificado manualmente
#Usado com DEFAULT_CONTENT_TYPE para 
#construir o cabeçalho Content-Type.
DEFAULT_CHARSET = 'utf-8'

#Default content type to use for all HttpResponse objects, 
#if a MIME type isn’t manually specified. 
DEFAULT_CONTENT_TYPE = 'text/html'

#=================================================

#media files

MEDIA_ROOT =os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'  #URL para usar ao se referir a arquivos estáticos localizados no STATIC_ROOT.

'''
Este deve ser um (inicialmente vazio) diretório de 
destino para coletar seus arquivos estáticos de 
seus locais permanentes em um diretório para 
facilidade de implantação; não é um lugar para 
armazenar seus arquivos estáticos permanentemente. 
Você deve fazer isso em diretórios que serão 
encontrados por localizadores de staticfiles, que 
por padrão, são '/' estáticos sub-diretórios de 
aplicativos e todos os diretórios que você 
incluir em STATICFILES_DIRS).
'''

'''
O caminho absoluto para o diretório onde collectstatic irá coletar arquivos estáticos para a implantação
Se o aplicativo staticfiles contrib está ativado (padrão), o comando de gerenciamento collectstatic irá 
coletar arquivos estáticos para este diretório. Veja o howto sobre gerenciamento de arquivos estáticos para 
obter mais detalhes sobre o uso.
'''
#STATIC_ROOT = '' #os.path.join(BASE_DIR, 'static')


'''
Esta configuração define os locais adicionais que o aplicativo 
staticfiles irá percorrer, se o localizador FileSystemFinder estiver 
ativada, por exemplo, se você usar o comando de gerenciamento collectstatic ou findstatic 
ou usar o arquivo estático que serve views.

Isso deve ser definido como uma lista ou tupla de strings que 
contêm caminhos completos para o seu diretório de arquivos adicionais (s)
'''
STATICFILES_DIRS = (
	os.path.join(BASE_DIR, "static")
		
),
