from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)

class category(models.Model):
    category_name = models.CharField(max_length=100)

class music_teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    image = models.CharField(max_length=100)


class user(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE)

class rating(models.Model):
    rating = models.CharField(max_length=100)
    MUSIC_TEACHER = models.ForeignKey(music_teacher,on_delete=models.CASCADE)
    USER = models.ForeignKey(user,on_delete=models.CASCADE)
    date = models.CharField(max_length=100)

class feedback(models.Model):
    feedback = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    USER = models.ForeignKey(user,on_delete=models.CASCADE)


class own_category(models.Model):
    CATEGORY = models.ForeignKey(category,on_delete=models.CASCADE)
    MUSIC_TEACHER = models.ForeignKey(music_teacher,on_delete=models.CASCADE)
    fees = models.CharField(max_length=100)

class class_new(models.Model):
    starttime = models.CharField(max_length=100)
    endtime = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    MUSIC_TEACHER = models.ForeignKey(music_teacher,on_delete=models.CASCADE)
    OWN_CATEGORY = models.ForeignKey(own_category,on_delete=models.CASCADE)



class requests(models.Model):
    request_date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    USER = models.ForeignKey(user,on_delete=models.CASCADE)
    OWN_CATEGORY = models.ForeignKey(own_category,on_delete=models.CASCADE)

class allocate_time(models.Model):
    CLASS_NEW = models.ForeignKey(class_new,on_delete=models.CASCADE)
    REQUESTS = models.ForeignKey(requests,on_delete=models.CASCADE)
    date = models.CharField(max_length=100)

class payment(models.Model):
    date = models.DateField()
    payment_method = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    REQUESTS = models.ForeignKey(requests,on_delete=models.CASCADE)













