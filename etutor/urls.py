
from django.contrib import admin
from django.urls import path,include
from etutor import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about),
    path('contact/',views.contact),
    path('service/',views.service),
    path('signup/',views.funsign),
    path('searchtutor/',views.funstutor),
    path('searchstudent/',views.funsstu),
    path('loadavtut/',views.funavtut),
    path('loadavstu/',views.funavstu),
    
    
    #path('admindas/',views.admin),
    path('user/',include('teachermanagement.urls')),
    path('student/',include('studentmanagement.urls')),
    path('admindas/',include('admincourse.urls'))
]
