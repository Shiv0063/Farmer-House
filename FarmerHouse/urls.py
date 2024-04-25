"""
URL configuration for FarmerHouse project.

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
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('PurchaseEntry',views.PurchaseEntry,name="Purchase Entry"),
    path('AddPurchaseEntry',views.AddPurchaseEntry,name="Add Purchase Entry"),
    path('AddPurchaseReturnEntry',views.AddPurchaseReturnEntry,name="Add Purchase Return Entry"),
    path('SalesEntry',views.SalesEntry,name="Sales Entry"),
    path('AddSalesEntry',views.AddSalesEntry,name="Add Sales Entry"),
    path('AddSalesReturnEntry',views.AddSalesReturnEntry,name="Add Sales Return Entry"),
    path('Party',views.Party,name="Party"),
    path('AddParty',views.AddParty,name="Add Party"),
    path('Product',views.Product,name='Product'),
    path('AddProduct',views.AddProduct,name="Add Product"),
    path('EditProducts',views.EditProducts,name="Edit stock Product"),
    path('SProducts/<str:PN>/<int:id>/<str:type>',views.SProducts,name='SProducts'),
    path('ProductsDelete',views.ProductsDelete,name='ProductsDelete'),
    path('Unit',views.Unit,name='Unit'),
    path('DeliveryBoy',views.DeliveryBoy,name='Delivery Boy'),
    path('AddDeliveryBoy',views.AddDeliveryBoy,name='Add Delivery Boy'),
    path('EditDeliveryBoy/<int:pk>',views.EditDeliveryBoy,name='Edit Delivery Boy'),
    path('DeleteDeliveryBoy/<int:pk>',views.DeleteDeliveryBoy,name='Delete Delivery Boy'),
    path('DeliveryBoyDetails/<int:pk>',views.DeliveryBoyDetails,name='Delivery Boy Details'),
    path('UserAccount',views.UserAccount,name='User Account'),
    path('AddUserAccount',views.AddUserAccount,name='Add User Account'),
    path('Category',views.Category,name='Category'),
    path('AddCategory',views.AddCategory,name='Add Category'),
    path('Expanse',views.Expanse,name='Expanse'),
    path('AllDelete',views.AllDelete,name='AllDelete'),
    path('login',views.Login,name='Login'),
    path('logout',views.Logout,name='Logout'),
    # path('Category',views.Category,name='Category'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)