from django.shortcuts import render,HttpResponse,redirect
from admincourse.models import adcourse
from subject.models import adsubject
from studentmanagement.models import StuRequest
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def service(request):
    return render(request,'service.html')
def funsign(request):
    return render(request,'signup.html')
def funstutor(request):
    ob=adcourse.objects.all()
    return render(request,'searchtutor.html',{'dt':ob})
def funsstu(request):
    ob=adcourse.objects.all()
    return render(request,'searchstudent.html',{'dt':ob})
def loadsub(request):
    cid=request.POST["cid"]
    ob=adsubject.objects.filter(id=cid)
    return render(request,'ajax/loadsub.html',{'dt':ob})
def funavtut(request):
    cid=request.POST["cid"]
    ob=adsubject.objects.raw("select t.* from teacher_signup t where t.id in(select teacherid_id from teacher_subject where subjectid_id in(select id from adminsubject where courseid_id="+str(cid) +"))")
    return render(request,'ajax/loadavtut.html',{'dt':ob})
def funavstu(request):
    cid=request.POST["cid"]
    ob=StuRequest.objects.raw("select t.* from student_signup t where t.id in(select studentid_id from student_request where courseid_id="+str(cid) +")")
    return render(request,'ajax/loadavstu.html',{'dt':ob})