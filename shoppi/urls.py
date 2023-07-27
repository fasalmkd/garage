from django.urls import path
from.import views

urlpatterns=[
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("booking",views.booking,name="booking"),
    path("service",views.service,name="service"),
    path("contact",views.contact,name="contact"),
    path("team",views.team,name="team"),
    path("testimonial",views.testimonial,name="testimonial"),
    path("404",views.ha,name="404")
]