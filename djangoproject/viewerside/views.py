from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

import mysql.connector as mcdb
conn=mcdb.connect(host="localhost",user="root",passwd="",database="test")
print("Successfully Connected"),
cur=conn.cursor()

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def gallery(request):
    return render(request,'gallery.html')

def review(request):
    return render(request,'review.html')

def contact(request):
    return render(request,'contact.html')

def datastore(request):
    if request.method=="POST":
        print(request.POST)
        name=request.POST['name'],
        phone=request.POST['phone'],
        email=request.POST['email'],
        msg=request.POST['msg'],
        cur.execute("INSERT INTO `plusdata`(`name`,`email`,`phone`,`msg`) values('{}','{}','{}','{}')",(name,phone,email,msg))
        conn.commit()
        return redirect('contact.html')
    else:
        return redirect('contact.html')

