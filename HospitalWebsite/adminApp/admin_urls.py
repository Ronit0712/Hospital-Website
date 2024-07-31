from django.contrib import admin
from django.urls import path
from adminApp import views

urlpatterns = [
    path('',views.dashboard),
    path('home/',views.home),
    path('save_home_img/',views.save_home_img),
    path('delete_home_img/',views.delete_home_img),
    path('save_card/',views.save_card),
    path('delete_card/',views.delete_card),
    path('save_service/',views.save_service),
    path('delete_service/',views.delete_service),
    path('save_service_about/',views.save_service_about),
    path('delete_service_about/',views.delete_service_about),
    path('save_service_card/',views.save_service_card),
    path('delete_service_card/',views.delete_service_card),
    path('save_trncard/',views.save_trncard),
    path('delete_trncard/',views.delete_trncard),





    path('about_kem/',views.about_kem),
    path('save_about/',views.save_about),
    path('delete_about/',views.delete_about),




    path('awards/',views.awards),
    path('save_award/',views.save_award),
    path('delete_award/',views.delete_award),




    path('teams/',views.teams),
    path('save_member/',views.save_member),
    path('delete_member/',views.delete_member),



    path('blogs/',views.blogs),
    path('save_blogs/',views.save_blogs),
    path('delete_blogs/',views.delete_blogs),



    path('contact_number/',views.contact_number),
    path('save_contact/',views.save_contact),



    path('appointment/',views.appointment),
    path('inauguration/',views.inauguration),
    path('gallery/',views.gallery),
    path('testimonial/',views.testimonial),
    path('privacy_policy/',views.privacy_policy),
    path('deparments/',views.departments)




    




    
]