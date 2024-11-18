from django.shortcuts import render,HttpResponse,redirect
from studentmanagement.models import MyUser1
from admincourse.models import adcourse    
from studentmanagement.models import StuRequest 
def saverecord(request):
    email=request.POST["email"]
    password=request.POST["password"]
    name=request.POST["name"]
    mobile=request.POST["mobile"]
    gender=request.POST["gender"]
    address=request.POST["address"]
    class1=request.POST["class1"]
    
    Ob=MyUser1(StEmail=email,StPassword=password,StName=name,StMobile=mobile,StGender=gender,StAddress=address,SClass=class1)
    Ob.save()
    return HttpResponse("Record Saved")


def login2(request):
    email=request.POST["email"]
    password=request.POST["password"]
    ob=MyUser1.objects.filter(StEmail=email,StPassword=password)
    if ob:
        request.session['em1']=ob[0].id
        return HttpResponse("Valid User")
    else:
        return HttpResponse("Invalid user")


def sdashboard(request):
    id=request.session["em1"]
    ob=MyUser1.objects.filter(id=id)
    return render(request,'sdashboard.html',{'ob':ob[0].StName})
    
def treq(request):
    id=request.session["em1"]
    ob1=MyUser1.objects.filter(id=id)
    ob=adcourse.objects.all()
    return render(request,'treq.html',{'dt':ob,'ob':ob1[0].StName})

def savereq(request):
    cid=request.POST["cid"]
    id=request.session["em1"]
    Ob=StuRequest(courseid_id=cid,studentid_id=id)
    Ob.save()
    return HttpResponse("Tution Request Saved")

def loadsreq(request):
    id=request.session["em1"]
    ob=StuRequest.objects.raw("select sr.id,ac.course from student_request sr,admincourse ac where sr.courseid_id=ac.id and sr.studentid_id="+str(id))
	#ob1=TSubJect.objects.filter(teacherid_id=id)
    return render(request,'ajax/loadscourse.html',{'dt':ob})
def logout(request):
    del request.session['em1']
    return redirect("/")