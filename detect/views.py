from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .apps import DetectConfig
from .models import Person
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from keras.preprocessing import image
import pickle
import numpy as np
import PIL

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
            try:
                msg = EmailMessage(
                    'Breast Cancer Prediction Report',
                    html_message,
                    'breast.cancer.predict@gmail.com',
                    [ctx.email],
                )
                msg. content_subtype = "html"
                msg.send()
            except:
                pass
            return render(request,'just.html',{'c':ctx})
        else:
            html_message = render_to_string('gmail1.html', {'c': ctx})
            try:
                msg = EmailMessage(
                    'Breast Cancer Prediction Report',
                    html_message,
                    'breast.cancer.predict@gmail.com',
                    [ctx.email],
                )
                msg. content_subtype = "html"
                msg.send()  
            except:
                pass
            return render(request,'check.html',{'c':ctx})
    else:
        x=request.session.get('b')
        ctx=get_object_or_404(Person,pk=x)
        return render(request,'predict.html',{'c':ctx})
def about(request):
    return render(request,'about.html')
def lung(request):
    img_obj=request.FILES["img"]
    imgg=PIL.Image.open(img_obj)
    test_image =imgg.resize((64,64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = DetectConfig.loaded_model.predict(test_image)
    x=request.session.get('b')
    ctx=get_object_or_404(Person,pk=x)
    if(result[0]==0):
        html_message = render_to_string('gmaillung0.html', {'c': ctx})
        try:
            msg = EmailMessage(
                'Lung Cancer Prediction Report',
                html_message,
                'breast.cancer.predict@gmail.com',
                [ctx.email],
            )
            msg. content_subtype = "html"
            msg.send()  
        except:
            pass
        return render(request,'lung0.html',{'c':ctx})
    else:
        html_message = render_to_string('lunggmail1.html', {'c': ctx})
        try:
            msg = EmailMessage(
                'Lung Cancer Prediction Report',
                html_message,
                'breast.cancer.predict@gmail.com',
                [ctx.email],
            )
            msg. content_subtype = "html"
            msg.send()  
        except:
            pass
        return render(request,'lung1.html',{'c':ctx})

    
