from django.shortcuts import render,HttpResponse
from teachermanagement.models import MyUser
from admincourse.models import adcourse
from subject.models import adsubject
from django.shortcuts import render,redirect
from teachermanagement.models import TSubJect
def saverecord(request):
    email=request.POST["email"]
    password=request.POST["password"]
    name=request.POST["name"]
    mobile=request.POST["mobile"]
    gender=request.POST["gender"]
    address=request.POST["address"]
    photo="sample.png"
    qualification=request.POST["qualification"]
    
    
    Ob=MyUser(Email=email,Password=password,Name=name,Mobile=mobile,Gender=gender,Address=address,Photo=photo,Qualification=qualification)
    Ob.save()

    return HttpResponse("Record Saved")


def login1(request):
    email=request.POST["email"]
    password=request.POST["password"]
    ob=MyUser.objects.filter(Email=email,Password=password)
    if ob:
        request.session['em']=ob[0].id
        return HttpResponse("Valid User")
    else:
        return HttpResponse("Invalid user")


def tdashboard(request):
    id=request.session["em"]
    ob=MyUser.objects.filter(id=id)
    return render(request,'tdashboard.html',{'ob':ob[0].Name})

def tclass(request):
    id=request.session["em"]
    ob1=MyUser.objects.filter(id=id)
    ob=adcourse.objects.all()
    return render(request,'tclass.html',{'dt':ob,'ob':ob1[0].Name})

def loadsub(request):
    cid=request.POST["cid"]
    ob=adsubject.objects.filter(id=cid)
    return render(request,'ajax/loadsub.html',{'dt':ob})

def loadtsub(request):
    id=request.session["em"]
    ob=TSubJect.objects.raw("select ts.id,ac.course,as1.subject from adminsubject as1,teacher_subject ts,admincourse ac where as1.id=ts.subjectid_id and ac.id=as1.courseid_id and ts.teacherid_id="+str(id))
	#ob1=TSubJect.objects.filter(teacherid_id=id)
    return render(request,'ajax/loadtsub.html',{'dt':ob})


def savesub(request):
    sid=request.POST["sid"]
    id=request.session["em"]
    Ob=TSubJect(subjectid_id=sid,teacherid_id=id)
    Ob.save()
    return HttpResponse("Teacher Subject Saved")
def logout(request):
    del request.session['em']
    return redirect("/")