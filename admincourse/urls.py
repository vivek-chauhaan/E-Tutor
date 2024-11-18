from django.urls import path
from admincourse import views
urlpatterns = [
    
path("save",views.course),
path('',views.admin1)
]

    