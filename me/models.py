from django.db import models
from datetime import datetime


# Create your models here.
class Personal_info(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    interests = models.TextField(max_length=1000)

    def __str__(self):
        return self.last_name



class Expirience(models.Model):
    work_level = models.TextField(blank=False)
    place_of_work = models.CharField(max_length=100)
    job_description = models.TextField(blank=True, null=True)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    left_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.place_of_work


class Education(models.Model):
    school_name = models.CharField(max_length=100, blank=False)
    course = models.CharField(max_length=100, blank=False)
    GPA = models.IntegerField()
    join_date = models.DateTimeField(default=datetime.now, blank=False)
    left_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.school_name


class Awards(models.Model):
    award_name = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.award_name
