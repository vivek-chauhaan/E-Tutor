from django.db import models

class adcourse(models.Model):
    course=models.CharField(max_length=100)
    def __str__(self):
        return str(self.course)
    class Meta:
        db_table="Admincourse"


