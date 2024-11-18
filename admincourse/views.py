from django.shortcuts import render,HttpResponse
from admincourse.models import adcourse

def admin1(request):
    return render(request,'admindas.html')

def course(request):
    course=request.POST["course"]
    
    ob=adcourse(course=course)
    ob.save()
    return HttpResponse("record saved")

