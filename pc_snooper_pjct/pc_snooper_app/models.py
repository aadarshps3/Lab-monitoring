from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

def uploaded_location(instance ,filename):
    return "%s/%s/%s" %('Screenshot',instance.userdata.username, filename)

def uploaded_file_location(instance ,filename):
    return "%s/%s/%s" %('Log',instance.userdata.username, filename)

################################################################## Admin Module #######################################################

################ user details table ######################

class RtUser(AbstractUser):
    ip_address=models.CharField(max_length=200,null=True)
    system_name=models.CharField(max_length=250,null=True)
    client_name=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    phone=models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/',null=True)


class screenshotdata(models.Model):
    userdata=models.ForeignKey(RtUser,on_delete = models.CASCADE)
    screenlog = models.FileField(upload_to='Screenshot/',null=True)
class monitoring(models.Model):
    userdata = models.ForeignKey(RtUser,on_delete = models.CASCADE)
    userlogdata = models.FileField(upload_to='Log/')





class userlog(models.Model):
    userdata=models.ForeignKey(RtUser, on_delete = models.CASCADE)
    screen=models.ForeignKey(screenshotdata, on_delete = models.CASCADE)
    userlogdata=models.ForeignKey(monitoring,on_delete = models.CASCADE)




########################################################################################################################################
