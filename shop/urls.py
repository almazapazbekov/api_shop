"""shop URL Configuration

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
from django.urls import path

from rest_framework.routers import DefaultRouter
from api import views


from api import serializers

# router = DefaultRouter()
# router.register('category', views.CategoryListCreate)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/', views.CategoryListCreate.as_view(), name='category'),
    path('category/<int:pk>', views.CategoryRetrieveUpdateDestroy.as_view(), name='category_detail'),
    path('item/', views.ItemListCreate.as_view(), name='item'),
    path('item/<int:pk>', views.ItemRetrieveUpdateDestroy.as_view(), name='item_detail'),

]
