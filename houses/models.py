# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from shortuuidfield import ShortUUIDField

class Users(models.Model):
    user_id = ShortUUIDField(primary_key=True)
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=255)
    real_name = models.CharField(max_length=20,blank=True)
    phone = models.CharField(unique=True, max_length=11)
    email = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=32)
    id_card = models.CharField(unique=True, max_length=18, blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True)
    status = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'Users'


class Houses(models.Model):
    house_id = models.CharField(primary_key=True, max_length=32)
    owner = models.ForeignKey(Users, models.DO_NOTHING)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    business_area = models.CharField(max_length=50, blank=True, null=True)
    house_type = models.CharField(max_length=32)
    layout = models.CharField(max_length=20)
    area_sqm = models.DecimalField(max_digits=8, decimal_places=2)
    orientation = models.CharField(max_length=10, blank=True, null=True)
    floor_info = models.CharField(max_length=20, blank=True, null=True)
    decoration = models.CharField(max_length=20, blank=True, null=True)
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=32)
    publish_time = models.DateTimeField()
    other = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Houses'
