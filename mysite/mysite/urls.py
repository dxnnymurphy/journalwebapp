"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from journal_app import views

urlpatterns = [
        path('admin/', admin.site.urls),
        re_path(r'^api/journals/$', views.journals_list),
        path('dj-rest-auth/', include('dj_rest_auth.urls')),
        path('api/journals/<int:pk>/', views.journals_detail),
        path('api/journals/<str:filter>/', views.journals_filter),
        path('rest-auth/google/', views.GoogleLogin.as_view(), name='google_login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
