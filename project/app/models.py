from django.db import models

# Create your models here.
class Student(models.Model):
    # Name=models.CharField(max_length=600)
    # City=models.CharField(max_length=100)
    # Email=models.EmailField()
    stu_name=models.CharField(max_length=250)
    stu_email=models.EmailField()
    stu_city=models.CharField(max_length=150)


    class Meta:
        db_table='Student'
        verbose_name_plural='STudent'

        # def __str__(self):
        #     return str(self.Name)
