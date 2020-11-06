"""towardsBookEra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from accounts import views as account_view
from . import views as master_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "TowardsBookEra Administration"
admin.site.site_title = "TowardsBookEra - Welcome new era with knowledge"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='loginPath'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logoutPath'),
    path('', master_view.index, name='homePath'),
    path('register/', account_view.register, name="registerPath"),
    path('accounts/', include('accounts.urls')),
    path('books/', include("bookApp.urls"), name="bookshopPath"),
    path('blog/', include('blog.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)