from django.http import HttpResponse
from django.shortcuts import redirect, render
from adminApp.models import HomeImageModel, HomeCardModel, HomeServiceModel, ServiceAboutModel , ServiceCardModel , TrnCardModel, AboutModel, AwardModel, TeamMemberModel , BlogModel, ContactModel
# Create your views here.
def home(req):
    home_images = HomeImageModel.objects.all()
    home_cards = HomeCardModel.objects.all()
    services = HomeServiceModel.objects.all()
    service_about = ServiceAboutModel.objects.all()
    service_cards = ServiceCardModel.objects.all()
    trn_cards = TrnCardModel.objects.all()
    obj = {"home_images":home_images, "home_cards":home_cards, "services":services , "service_about":service_about , "service_cards":service_cards, "trn_cards":trn_cards}
    return render(req,"admin/home.html",obj)


def save_home_img (req):
    print(req.POST)
    newhome_img = HomeImageModel(
        home_img = req.FILES['home_img'],
    )
    newhome_img.save()
    #return HttpResponse ("Data Received")
    return redirect("/admin/home")

def delete_home_img(req):
    HomeImageModel.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/home")


def save_card(req):
    print(req.POST)
    newhome_card = HomeCardModel(
        cimage = req.FILES['cimage'],
        ctitle = req.POST['ctitle'],
        cdiscription = req.POST['cdiscription'],
    )
    newhome_card.save()
    #return HttpResponse("data receive")
    return redirect("/admin/home")

def delete_card(req):
    HomeCardModel.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/home")


def save_service(req):
    print(req.POST)
    newservice = HomeServiceModel(
        service = req.POST['service'],
    )
    newservice.save()
    #return HttpResponse("data receive")
    return redirect("/admin/home")

def delete_service(req):
    HomeServiceModel.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/home")


def save_service_about(req):
    newservice_about = ServiceAboutModel(
        sheading = req.POST['sheading'],
        stitle = req.POST['stitle'],
        sdetails = req.POST['sdetails'],
    )
    newservice_about.save()
    return redirect("/admin/home")
    
def delete_service_about(req):
    ServiceAboutModel.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/home")

    
def save_service_card(req):
    newservice_card = ServiceCardModel(
        srvimage = req.FILES['srvimage'],
        srvtitle = req.POST['srvtitle'],
    )
    newservice_card.save()
    return redirect("/admin/home")

def delete_service_card(req):
    ServiceCardModel.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/home")


def save_trncard(req):
    newtrncard = TrnCardModel(
        trnimage = req.FILES['trnimage'],
        trncount = req.POST['trncount'],
        trntitle = req.POST['trntitle'],
    )
    newtrncard.save()
    return redirect("/admin/home")
def delete_trncard(req):
    TrnCardModel.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/home")











def dashboard(req):
    return render(req,"admin/dashboard.html")





# ABOUT
def about_kem(req):
    abouts = AboutModel.objects.all()
    obj = {"abouts":abouts}
    return render(req,"admin/about_kem.html",obj)

def save_about(req):
    newabout = AboutModel(
        title = req.POST['title'],
        discription = req.POST['discription'],
    )
    newabout.save()
    return redirect("/admin/about_kem")

def delete_about(req):
    AboutModel.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/about_kem")








# AWARD
def awards(req):
    awards = AwardModel.objects.all()
    obj = {"awards":awards}
    return render(req,"admin/awards.html",obj)

def save_award(req):
    newaward = AwardModel(
        awardimg = req.FILES['awardimg'],
    )
    newaward.save()
    return redirect("/admin/awards")

def delete_award(req):
    AwardModel.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/awards")



# TEAM MEMBERS
def teams(req):
    members = TeamMemberModel.objects.all()
    obj = {"members":members}
    return render(req,"admin/teams.html",obj)

def save_member(req):
    newmember = TeamMemberModel(
        tmimage = req. FILES['tmimage'],
        tmname = req. POST['tmname'],
        tmposition = req.POST ['tmposition'],
    )
    newmember.save()
    return redirect("/admin/teams")

def delete_member(req):
    TeamMemberModel.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/teams")




def blogs(req):
    blogs = BlogModel.objects.all()
    obj = {"blogs":blogs}
    return render(req,"admin/blogs.html",obj)

def save_blogs(req):
    newblog = BlogModel(
        bimage = req.FILES['bimage'],
        btitle = req.POST['btitle'],
        bdetails = req.POST['bdetails'],
        bby = req.POST['bby'],
    )
    newblog.save()
    return redirect("/admin/blogs")

def delete_blogs(req):
    BlogModel.objects.get(id = req.GET['id']).delete()
    return redirect("/admin/blogs")

 

 #CONTACT
def contact_number(req):
    contacts = ContactModel.objects.all()
    obj = {"contacts":contacts}
    return render(req,"admin/contact_number.html",obj)

def save_contact (req):
    newcontact = ContactModel(
        ctitle = req.POST['ctitle'],
        cinput = req.POST['cinput'],
        cdays = req.POST['cdays'],
        ctime = req.POST['ctime'],
        cno1 = req.POST['cno1'],
        cno2 = req.POST['cno2'],
    )
    newcontact.save()
    return redirect("/admin/contact_number")




def appointment(req):
    return render(req,"admin/appointment.html")
def inauguration(req):
    return render(req,"admin/inauguration.html")
def gallery(req):
    return render(req,"admin/gallery.html")
def testimonial(req):
    return render(req,"admin/testimonial.html")
def privacy_policy(req):
    return render(req,"admin/privacy_policy.html")
def departments(req):
    return render(req,"admin/departments.html")