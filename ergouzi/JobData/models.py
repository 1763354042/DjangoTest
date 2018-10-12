from django.db import models


class AvgSalary(models.Model):
    id = models.IntegerField(primary_key=True)
    keyword = models.CharField(db_column='keyWord', max_length=255)  # Field name made lowercase.
    avgsalary = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'avg_salary'


class Citylist(models.Model):
    id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    keyword = models.CharField(db_column='keyWord', max_length=255, blank=True, null=True)
 # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'citylist'


class Citysalary(models.Model):
    id = models.IntegerField(primary_key=True)
    keyword = models.CharField(db_column='keyWord', max_length=255, blank=True, null=True)
 # Field name made lowercase.
    city = models.CharField(max_length=255, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citysalary'


class Salaryrange(models.Model):
    id = models.IntegerField(primary_key=True)
    keyword = models.CharField(db_column='keyWord', max_length=255, blank=True, null=True)
 # Field name made lowercase.
    range = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salaryrange'

