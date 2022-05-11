"""myProject URL Configuration

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

from Toll import views

urlpatterns = [
    path('',views.indexPage,name='indexPage'),
    path('home/', views.homePage,name='home'),
    path('save/',views.saveCustomer,name='Save'),
    path('login/',views.login,name='login'),
    path('validate/',views.validate,name='validate'),
    path('custDashboard/',views.custDashboard,name='custDashboard'),
    path('viewAllCustomerDetail/',views.viewAllCustomerDetail,name='viewAllCustomerDetail'),
    path('adminAll/',views.adminAll,name='adminAll'),
    path('update_account/',views.update_account,name='update_account'),
    path('wallet/',views.wallet,name='wallet'),
    path("amount/",views.amount,name='amount'),
    path("empRegistration/",views.empRegistration,name='empRegistration'),
    path("save_emp/",views.save_emp,name='save_emp'),
    path("adminLogin/",views.adminLogin,name='adminLogin'),
    path("dashPage/",views.dashPage,name='dashPage'),
    path("adminDashPage/",views.adminDashPage,name='adminDashPage'),
    path("allCustomersAdmin/",views.allCustomersAdmin,name='allCustomersAdmin'),
    path("allTranscation/",views.allTranscation,name='allTranscation'),
    path("admingEmpAll/",views.admingEmpAll,name='admingEmpAll'),

]
