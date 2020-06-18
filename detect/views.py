from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .apps import DetectConfig
from .models import Person
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
import pickle

def home(request):
    if request.method=="POST":
        name=request.POST['name']
        gender=request.POST['gender']
        age=request.POST['age']
        email=request.POST['email']
        z=Person(name=name,gender=gender,age=age,email=email)    
        z.save()
        a=z.id
        request.session['b']=a
        dest = get_object_or_404(Person,pk=z.id)
        return render(request,'predict.html',{'c':dest})
    else:
        return render(request,'index.html')
def start(request):
    if request.method=="POST":
        a=int(request.POST['op1'])
        b=int(request.POST['op2'])
        c=int(request.POST['op3'])
        d=int(request.POST['op4'])
        e=int(request.POST['op5'])
        f=int(request.POST['op6'])
        g=int(request.POST['op7'])
        h=int(request.POST['op8'])
        i=int(request.POST['op9'])
        l=[a,b,c,d,e,f,g,h,i]
        ans=DetectConfig.mdl.predict([l])
        x=request.session.get('b')
        ctx=get_object_or_404(Person,pk=x)
        if(ans[0]==2):
            html_message = render_to_string('gmail.html', {'c': ctx})
            msg = EmailMessage(
                'Cancer Prediction',
                html_message,
                'breast.cancer.predict@gmail.com',
                [ctx.email],
            )
            msg. content_subtype = "html"
            msg.send()
            return render(request,'just.html',{'c':ctx})
        else:
            html_message = render_to_string('gmail1.html', {'c': ctx})
            msg = EmailMessage(
                'Cancer Prediction',
                html_message,
                'breast.cancer.predict@gmail.com',
                [ctx.email],
            )
            msg. content_subtype = "html"
            msg.send()  
            return render(request,'check.html',{'c':ctx})
    else:
        x=request.session.get('b')
        ctx=get_object_or_404(Person,pk=x)
        return render(request,'predict.html',{'c':ctx})
def about(request):
    return render(request,'about.html')
 
            