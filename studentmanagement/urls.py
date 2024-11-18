from django.urls import path
from studentmanagement import views

urlpatterns=[
    
    path("save1",views.saverecord),
    path("log1", views.login2),
    path("sdashboard/",views.sdashboard),
    path("treq/",views.treq),
    path("savereq/",views.savereq),
    path("loadsreq/",views.loadsreq),
    path("logout/",views.logout)
    
]