from django.db import models
from subject.models import adsubject
class MyUser(models.Model):
    Email=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Name=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Photo=models.CharField(max_length=100)
    Qualification=models.CharField(max_length=100,default=None, blank=True, null=True)
    
    class Meta:
        db_table="Teacher_Signup"

class TSubJect(models.Model):
    subjectid = models.ForeignKey(adsubject, on_delete = models.SET_NULL,null =True)
    teacherid = models.ForeignKey(MyUser, on_delete = models.SET_NULL,null =True)
    
    class Meta:
        db_table="teacher_subject"