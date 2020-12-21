from django.db import models


class Authororm(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=15)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authororm'


class Bookorm(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookorm'


class Douban(models.Model):
    film_content = models.TextField(blank=True, null=True)
    film_star = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'douban'


class Info(models.Model):
    itemid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    birthday = models.CharField(max_length=50, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'info'


class Userinfo(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userinfo'


class Userlog(models.Model):
    out_id = models.IntegerField(blank=True, null=True)
    in_id = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userlog'


class Usermoney(models.Model):
    money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usermoney'
