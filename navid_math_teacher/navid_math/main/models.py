from django.db import models

# Create your models here.
class seasions(models.Model):
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    # title = models.CharField(max_length=100)
    # suggest = models.BooleanField(default=True )
    # body = models.TextField()
    seasions = models.IntegerField(max_length=2)

class titels(models.Model):
    seasion = models.ForeignKey(seasions, on_delete=models.CASCADE ,related_name='titels')
    subjects = models.CharField(max_length=45)
    
class description(models.Model):
    seasion = models.ForeignKey(seasions, on_delete=models.CASCADE ,related_name='descr', default=1)
    subject = models.ForeignKey(titels , on_delete=models.CASCADE ,related_name='desription')
    a=models.BooleanField(default=False,blank=True)
    b=models.BooleanField(default=False,blank=True)
    c=models.BooleanField(default=False,blank=True)
    d=models.BooleanField(default=False,blank=True)
    e=models.BooleanField(default=False,blank=True)

class question(models.Model):
    seasion = models.ForeignKey(seasions, on_delete=models.CASCADE ,related_name='desclr', default=1)
    subject = models.ForeignKey(titels , on_delete=models.CASCADE ,related_name='question')
    body = models.TextField()
    choice1 = models.CharField(max_length=45 , default='2')
    choice2 = models.CharField(max_length=45, default='3')
    choice3 = models.CharField(max_length=45, default='4')
    choice4 = models.CharField(max_length=45, default='5')
    answer = models.IntegerField()
    why=models.TextField()
    
class dq(models.Model):
    seasion = models.ForeignKey(seasions, on_delete=models.CASCADE ,related_name='deslr', default=1)
    subject = models.ForeignKey(titels , on_delete=models.CASCADE ,related_name='day_question')
    body = models.TextField()
    choice1 = models.CharField(max_length=45 , default='2')
    choice2 = models.CharField(max_length=45, default='3')
    choice3 = models.CharField(max_length=45, default='4')
    choice4 = models.CharField(max_length=45, default='5')
    answer = models.IntegerField()
    why=models.TextField()
    