"""
URL configuration for chatbot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.urls import path
from slackbot import views  # 방금 작성한 slackbot 앱의 views를 불러와주고,

urlpatterns = [
    path("admin/", admin.site.urls),
    path("attend", views.Attend.as_view()),  # attend 경로를 추가해줍니다.
]

urlpatterns = [
    path('admin/', admin.site.urls),
]
