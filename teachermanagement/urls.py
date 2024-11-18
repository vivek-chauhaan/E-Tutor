from django.urls import path
from teachermanagement import views

urlpatterns=[
    
    path("save",views.saverecord),
    path("log", views.login1),
    path("tdashboard/",views.tdashboard),
    path("tclass/",views.tclass),
    path("loadsub/",views.loadsub),
    path("savesub/",views.savesub),
    path("loadtsub/",views.loadtsub),
    path("logout/",views.logout)
]