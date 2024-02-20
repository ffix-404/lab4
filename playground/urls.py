from django.urls import path
from . import views

urlpatterns=[
    path("anyNumber/<str:price>",views.anyNumber,name="anyNumber"),
    path("",views.Defult_path,name="Defult_path"),
    path("taxrate/<str:taxrate1>",views.taxrate,name="taxrate")
]