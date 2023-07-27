from django.shortcuts import render

def index(request):
   return render(request,"index.html")
def about(request):
   return render(request,"about.html")
def booking(request):
   return render(request,"booking.html")
def service(request):
   return render(request,"service.html")
def contact(request):
   return render(request,"contact.html")
def team(request):
   return render(request,"team.html")
def testimonial(request):
   return render(request,"testimonial.html")
def ha(request):
   return render(request,"404.html")

# Create your views here.