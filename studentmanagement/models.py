from django.db import models
from admincourse.models import adcourse
class MyUser1(models.Model):
    StEmail=models.CharField(max_length=100)
    StPassword=models.CharField(max_length=100)
    StName=models.CharField(max_length=100)
    StMobile=models.CharField(max_length=100)
    StGender=models.CharField(max_length=100)
    StAddress=models.CharField(max_length=100)
    SClass=models.CharField(max_length=100,default=None, blank=True, null=True)
    StPhoto=models.CharField(max_length=100)
    
    class Meta:
        db_table="Student_Signup"

class StuRequest(models.Model):
    courseid = models.ForeignKey(adcourse, on_delete = models.SET_NULL,null =True)
    studentid = models.ForeignKey(MyUser1, on_delete = models.SET_NULL,null =True)
    
    class Meta:
        db_table="student_request"