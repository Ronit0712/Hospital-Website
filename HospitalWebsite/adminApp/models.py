from django.db import models

# Create your models here.
class HomeImageModel(models.Model):
    home_img = models.ImageField(upload_to="static/uploads/")

class HomeCardModel(models.Model):
    cimage = models.ImageField(upload_to="static/uploads/")
    ctitle = models.CharField(max_length = 100)
    cdiscription = models.CharField(max_length = 200)

class HomeServiceModel(models.Model):
    service = models.CharField(max_length = 100)

class ServiceAboutModel(models.Model):
    sheading = models.CharField(max_length = 100)
    stitle = models.CharField(max_length = 100)
    sdetails = models.CharField(max_length = 300)

class ServiceCardModel(models.Model):
    srvimage = models.ImageField(upload_to="static/uploads/")
    srvtitle = models.CharField(max_length = 100)

class TrnCardModel(models.Model):
    trnimage = models.ImageField(upload_to="static/uploads/")
    trncount = models.CharField(max_length = 100)
    trntitle = models.CharField(max_length = 100)




# ABOUT

class AboutModel(models.Model):
    title = models.CharField(max_length = 100)
    discription = models.CharField(max_length = 1000)



# AWARD

class AwardModel(models.Model):
    awardimg = models.ImageField(upload_to="static/uploads/")



#Team Member

class TeamMemberModel(models.Model):
    tmimage = models.ImageField(upload_to="static/uploads/")
    tmname = models.CharField(max_length = 100)
    tmposition = models.CharField(max_length = 100)


#BLOG

class BlogModel(models.Model):
    bimage = models.ImageField(upload_to="static/uploads/")
    btitle = models.CharField(max_length = 100)
    bdetails = models.CharField(max_length = 1000)
    bby = models.CharField(max_length = 100)


#CONTACT

class ContactModel(models.Model):
    ctitle = models.CharField(max_length = 100 )
    cinput = models.CharField(max_length = 100 )
    cdays = models.CharField(max_length = 100 )
    ctime = models.TimeField(max_length = 100 )
    cno1 = models.CharField(max_length = 15 )
    cno2 = models.CharField(max_length = 15 )