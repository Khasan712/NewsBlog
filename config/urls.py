"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from config.settings import MEDIA_ROOT, MEDIA_URL

bot_name = settings.TELEGRAM_BOT_NAME
bot_token = settings.TELEGRAM_BOT_TOKEN
redirect_url = settings.TELEGRAM_LOGIN_REDIRECT_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('mainapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('comments/', include('commentsUser.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),

]+static(settings.MEDIA_URL, document_root=MEDIA_ROOT)


