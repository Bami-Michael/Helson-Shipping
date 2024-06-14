from django.db import models

class Shipment(models.Model):
  firstname = models.CharField(max_length=255, null=True)
  lastname = models.CharField(max_length=255, null=True)
  no = models.CharField(max_length=255, null=True)
  address = models.CharField(max_length=255, null=True)
  country1 = models.CharField(max_length=255, null=True)
  country2 = models.CharField(max_length=255, null=True)

  date1 = models.DateField(null=True, blank=True)
  time1 = models.TimeField(null=True)
  msg1 = models.CharField(max_length=255, null=True)
  city1 = models.CharField(max_length=255, null=True)

  date2 = models.DateField(null=True, blank=True)
  time2 = models.TimeField(null=True)
  msg2 = models.CharField(max_length=255, null=True)
  city2 = models.CharField(max_length=255, null=True)

  date3 = models.DateField(null=True, blank=True)
  time3 = models.TimeField(null=True)
  msg3 = models.CharField(max_length=255, null=True)
  city3 = models.CharField(max_length=255, null=True)

  date4 = models.DateField(null=True, blank=True)
  time4 = models.TimeField(null=True)
  msg4 = models.CharField(max_length=255, null=True)
  city4 = models.CharField(max_length=255, null=True)

  date5 = models.DateField(null=True, blank=True)
  time5 = models.TimeField(null=True)
  msg5 = models.CharField(max_length=255, null=True)
  city5 = models.CharField(max_length=255, null=True)

  date6 = models.DateField(null=True, blank=True)
  time6 = models.TimeField(null=True)
  msg6 = models.CharField(max_length=255, null=True)
  city6 = models.CharField(max_length=255, null=True)

  date7 = models.DateField(null=True, blank=True)
  time7 = models.TimeField(null=True)
  msg7 = models.CharField(max_length=255, null=True)
  city7 = models.CharField(max_length=255, null=True)
  

  def __str__(self):
    return self.firstname