from django.shortcuts import render
from .models import student
from django.http import HttpResponse
# Create your views here.
def insert(request):
    if request.method == "POST":
        sid=request.POST['sid']
        sname=request.POST['sname']
        branch=request.POST['branch']
        place=request.POST['place']
        contact=request.POST['contact']   
        j=student(sid=sid,sname=sname,branch=branch,place=place,contact=contact)
        j.save()
        return HttpResponse("record has been stored successfully...")
    return render(request,"datainsert.html")