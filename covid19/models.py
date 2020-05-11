from django.db import models

# Create your models here.


class Developer(models.Model):
    cname= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    death=models.IntegerField()
    positive= models.IntegerField()
    quarantine=models.IntegerField()
    def __str__(self):
        return self.cname


class DistrictwiseCovid(models.Model):
    District_Name= models.CharField(max_length=100)
    Confirmed_Positive_Cases=models.IntegerField()
    Cases_Tested=models.IntegerField()
    Patients_Recovered=models.IntegerField()
    People_Under_Quarantine=models.IntegerField()
    Total_Deaths=models.IntegerField()

    def __str__(self):
         return self.District_Name


