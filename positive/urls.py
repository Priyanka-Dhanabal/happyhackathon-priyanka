"""
URL configuration for positive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from affirmation.views import home, note
from profiles.views import view_profile

from accounts.views import (
    login_view, 
    logout_view,
    register_view,
    view_profile,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('note/', note, name='note'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),

    path('profile/', view_profile, name='view_profile'),
    path('', include('affirmation.urls')),
]

