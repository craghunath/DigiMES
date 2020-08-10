from django.db import models


class M111m12(models.Model):
    metric = models.CharField(max_length=10, verbose_name = 'Metric No')
    description_500wrds = models.TextField(default='nil000nul', verbose_name = 'Description 500 words')
    #file_link = models.CharField(max_length=200, verbose_name = 'File link')

class M113(models.Model):
    metric = models.CharField(max_length=10, verbose_name = 'Metric No')
    option = models.CharField(max_length=30, verbose_name='Option')
    year = models.CharField(max_length=10, verbose_name='Year')
    month = models.CharField(max_length=10, verbose_name='Month')
    department = models.CharField(max_length=30, verbose_name='Department')
    teacher_name = models.CharField(max_length=100, verbose_name='Teacher name')
    participated_body = models.CharField(max_length=200, verbose_name='Participated institute/body name',default='MES')
    #file_link = models.CharField(max_length=200, verbose_name = 'File link')

class M121(models.Model):
    metric = models.CharField(max_length=10, verbose_name = 'Metric No')
    program_code = models.CharField(max_length=100, verbose_name='Program Code', default='nil000nul')
    #department = models.CharField(max_length=30, verbose_name='Department')
    program_name = models.CharField(max_length=200, verbose_name='Program Name')
    year = models.CharField(max_length=10, verbose_name='Introduction Year')
    month = models.CharField(max_length=10, verbose_name='Introduction Month')
    implment_status = models.CharField(max_length=5, verbose_name='Implementation Status')#yes/no
    implment_year = models.CharField(max_length=10, verbose_name='Implemented Year')
    implment_month = models.CharField(max_length=10, verbose_name='Implemented Month')
    program_totalNo = models.IntegerField(verbose_name='Total Programs')
    #file_link = models.CharField(max_length=200, verbose_name = 'File link')

class M122(models.Model):
    metric = models.CharField(max_length=10, verbose_name = 'Metric No')
    year = models.CharField(max_length=10, verbose_name='Introduction Year')
    month = models.CharField(max_length=10, verbose_name='Introduction Month')
    course_name = models.CharField(max_length=200, verbose_name='Add on/Certificate Course Name')
    course_code = models.CharField(max_length=100, verbose_name='Program Code', default='nil000nul')# 
    department = models.CharField(max_length=30, verbose_name='Department')
    offered_year = models.CharField(max_length=10, verbose_name='Offered Year')
    offered_month = models.CharField(max_length=10, verbose_name='Offered Month')
    offered_times = models.IntegerField(verbose_name='No of times per year')
    course_duration = models.CharField(max_length=20, verbose_name='Course Duration')
    enrolled_students_no = models.IntegerField(verbose_name='Enrolled number of Students')
    completed_students_no = models.IntegerField(verbose_name='Completed number of Students in the Year')
    course_totalNo = models.IntegerField(verbose_name='Total Courses')
    #file_link = models.CharField(max_length=200, verbose_name = 'File link')
    #1.2.3 data input not yet in the feed *********


class M123(models.Model):
    metric = models.CharField(max_length=10, verbose_name = 'Metric No')
    year = models.CharField(max_length=10, verbose_name='Offered Year')
    #month = models.CharField(max_length=10, verbose_name='Offered Month')
    enrolled_students_no = models.IntegerField(verbose_name='Enrolled number of Students')

    #1.2.3 data input not yet in the feed *********

class Filelinks(models.Model):
    metric = models.CharField(max_length=10, verbose_name = 'Metric No')
    file_name = models.CharField(max_length=300, verbose_name = 'File name')
    file_link = models.CharField(max_length=300, verbose_name = 'File link')

#https://www.youtube.com/watch?v=lE8SXffJUmI
#csv export