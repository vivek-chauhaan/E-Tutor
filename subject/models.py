from django.db import models
from admincourse.models import adcourse
class adsubject(models.Model):
    subject=models.CharField(max_length=100)
    courseid = models.ForeignKey(adcourse, on_delete = models.SET_NULL,null =True)
    def __str__(self):
        return str(self.courseid) + "-" + str(self.subject)
    class Meta:
        db_table="Adminsubject"
