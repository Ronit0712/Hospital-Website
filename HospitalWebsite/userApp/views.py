from django.shortcuts import render
from django.http import HttpResponse
from adminApp.models import HomeImageModel, HomeCardModel, HomeServiceModel ,ServiceAboutModel ,ServiceCardModel, TrnCardModel , AboutModel, AwardModel , TeamMemberModel , BlogModel, ContactModel
# Create your views here.
def home(req):
    home_images = HomeImageModel.objects.all()
    home_cards = HomeCardModel.objects.all()
    services = HomeServiceModel.objects.all()
    service_about = ServiceAboutModel.objects.all()
    service_cards = ServiceCardModel.objects.all()
    trn_cards = TrnCardModel.objects.all()

    obj ={"home_images":home_images, "home_cards":home_cards , "services":services ,  "service_about":service_about , "service_cards":service_cards, "trn_cards":trn_cards}
    return render(req,"user/home.html",obj)


def about(req):
    abouts = AboutModel.objects.all()
    obj = {"abouts":abouts}
    return render(req,"user/about.html",obj)


def award(req):
    awards = AwardModel.objects.all()
    obj = {"awards":awards}
    return render(req,"user/award.html",obj)



def teams(req):
    members = TeamMemberModel.objects.all()
    obj = {"members":members}
    return render(req,"user/teams.html",obj)




def departments(req):
    return render(req,"user/departments.html")



def blog(req):
    blogs = BlogModel.objects.all()
    obj = {"blogs":blogs}
    return render(req,"user/blog.html",obj)


def contact(req):
    contacts = ContactModel.objects.all()
    obj = {"contacts":contacts}
    return render(req,"user/contact.html",obj)


def appoinment(req):
    return render(req,"user/appoinment.html")
def social_media(req):
    return render(req,"user/social_media.html")
def gallery(req):
    return render(req,"user/gallery.html")
def testimonial(req):
    return render(req,"user/testimonial.html")
def privacy_policy(req):
    return render(req,"user/privacy_policy.html")
def inauguration(req):
    return render(req,"user/inauguration.html")