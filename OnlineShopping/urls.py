"""
URL configuration for OnlineShopping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from shopapp.views import About,ProductView,CategoryView,CustomerView,OrderView,PaymentView,OfferView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',About.as_view()),
    path('products/',ProductView.as_view()),
    path('categories/',CategoryView.as_view()),
    path('customers/',CustomerView.as_view()),
    path('orders/',OrderView.as_view()),
    path('payments/',PaymentView.as_view()),
    path('offers/',OfferView.as_view())
]

