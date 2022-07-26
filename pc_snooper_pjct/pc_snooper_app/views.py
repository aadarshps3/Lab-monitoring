from django.shortcuts import render,redirect

from .forms import *
from .models import *
from django.contrib import messages
import requests
import base64
from PIL import Image
from io import BytesIO
import random as rm
import requests, json
from django.core.files.storage import FileSystemStorage
import time
def login_page(request):
    return redirect('login')


##################### load Home page ###########################


def load_home(request):

    return render(request,'admin/admin_homepage.html')


##################### Add Users #################################

def add_user(request):
    form=TUserCreationForm()

    if request.method == "POST":

        form = TUserCreationForm(request.POST,request.FILES)
        print('1')


        # print(filedata)
        if form.is_valid():
            print('2')
            filedata = request.FILES['image']
            name = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password1')

            print('3')
            print(name,password,email,filedata)
            form.save()
            # fs = FileSystemStorage()
            # file1 = fs.save(filedata.name, filedata)
            # fileurl = fs.url(file1)
            #time.sleep(10)
            # with open(fileurl, "rb") as img_file:
            #     b64_string = base64.b64encode(img_file.read())
            b64_string = base64.b64encode(filedata.read())
            #print(b64_string)
            # im = Image.open(BytesIO(base64.b64decode(b64_string)))
            # im.save('new111.png', 'PNG')
            b64_string=str(b64_string)
            data = b64_string.replace('b', '', 1)
            obj=RtUser.objects.all()
            from requests.auth import HTTPBasicAuth
            import os
            for userdata in obj:
                if not userdata.is_superuser:
                    #data='hgi'
                    print('hihihi')
                    print(userdata.ip_address)

                    r = requests.get('http://'+userdata.ip_address+':9595/registeruser', data={'name': name, 'email': email,'password':password,'img':data})
                    # url = os.environ.get("URL",'http://'+userdata.ip_address+':9595/registeruser' )
                    # url = "%s" % (url)
                    # body = {"name" : "%s" % name, "email" : "%s" % email}
                    # response = requests.post(url, auth=HTTPBasicAuth('USER', 'PASSWORD'), headers={'Content-Type': 'application/json'}, json=body)
                    # if response.status_code == 200:
                    #     print("Code 200")
                    # else:
                    #     print("Code not 200")
            messages.success(request,"The user has been added sucessfully!")

            return redirect('user_view')




    return render(request,'admin/admin_user_add.html',{"forms":form})





########################## View Users ################################


def view_user(request):
    obj=RtUser.objects.all()

    if request.method =="POST":
        req_id=request.POST.get("remove_id")

        try:
            obj_delete=RtUser.objects.get(id=req_id)

        except RtUser.DoesNotExist:
            obj_delete = None

        obj_delete.delete()

    return  render(request,'admin/view_users.html',{"user_details":obj})


################################ Take screenshots ########################

def take_screenshots(request):
    obj = RtUser.objects.all()
    context = {
        "user_details":obj,
        'button':'Screenshot',
    }
    return render(request,'admin/screenshot_system.html',context)
def viewsreenshots(request,id=None):
    user=RtUser.objects.get(id=id)
    obj=screenshotdata.objects.filter(userdata=user)
    return render(request,'admin/userdata.html',{"user_details":obj})
################################ Shutdown  system ############################

def shutdown_system(request):
    obj = RtUser.objects.all()

    return render(request, 'admin/shutdown_system.html', {"user_details": obj})

def takescreenshot(request,id=None):
    print('start')
    userdata=RtUser.objects.get(id=id)
    #screenshotdata.objects.get(userdata=userdata)
    # if request.method == 'POST':
    #     print('post')
    #     r = requests.post('http://192.168.1.101:9595/screenshot', params=request.POST)
    # else:
    #     print('get')
    #     # r = requests.get('https://www.somedomain.com/some/url/save', params=request.GET)
    r = requests.get('http://'+userdata.ip_address+':9595/screenshot', params=request.GET)
    print('rrrr',r)
    # a=r.headers['content-type']
    # print(a)
    # a=r.encoding
    # print(a)
    # a=r.text
    # print('ttt',a[0])
    a=r.json()
    print('ttt1',a['data'])
    data = bytes(a['data'], 'utf-8')
    im = Image.open(BytesIO(base64.b64decode(data)))
    imgname1=rm.randint(12479325879,789321566999)
    imagname='media/Screenshot/'+str(imgname1)+'.png'
    img='Screenshot/'+str(imgname1)+'.png'
    im.save(imagname, 'PNG')
    if r.status_code == 200:
        print('worked')
    screenshotdata.objects.create(userdata=userdata,screenlog=img)
        #return HttpResponse('Yay, it worked')
    return redirect('system_screenshots')



def currentactivity(request):
    obj = RtUser.objects.all()

    return render(request,'admin/currentactivity.html', {'user_details':obj})
from django.http import JsonResponse
def currentactivitydata(request,id=None):
    userdata=RtUser.objects.get(id=id)

    r = requests.get('http://'+userdata.ip_address+':9595/current_app', params=request.GET)
    print('rrrr',r)
    a=r.json()
    print('ttt1',a['data'])
    messages.success(request,a['data'])
    # return JsonResponse({'result': r}, safe=False)
    return redirect('currentactivity')


#####screen monitoring #####
def allactivity(request):
    obj = RtUser.objects.all()

    return render(request,'admin/allactivity.html', {'user_details':obj})

def allactivitydata(request,id=None):
    userdata=RtUser.objects.get(id=id)

    r = requests.get('http://'+userdata.ip_address+':9595/allstatus', params=request.GET)
    print('rrrr',r)
    a=r.json()
    #print('ttt1',a['data'])
    trydata=a['data']
    print(len(trydata))
    print(trydata[2]['name'])
    json_response = json.dumps(a, indent=3)
    print(type(json_response))
    #messages.success(request,a['data'])
    # return JsonResponse({'result': r}, safe=False)
    #a = [{'A': 'val1', 'B': 'val2'}, {'C': 'val3', 'D': 'val4'}]
    context = {
        'length':len(trydata),
        'data':json_response
    }
    return render(request,'admin/viewallactivity.html',context)

def killprocess(request):
    obj = RtUser.objects.all()

    return render(request,'admin/killprocess.html', {'user_details':obj})

def killaprocess(request,id=None):
    userdata=RtUser.objects.get(id=id)
    if request.method=='POST':
        data=request.POST.get('q')
        print(data)
        instance= request.POST.get('userid')
        print(instance)
        userdata=RtUser.objects.get(id=instance)


        r = requests.get('http://'+userdata.ip_address+':9595/killprocess/'+data, params=request.GET)

        messages.success(request,"Process killed sucessfully!")
        return render(request,'admin/killprocesspage.html',{'data':userdata})



    return render(request,'admin/killprocesspage.html',{'data':userdata})


def shutdownsystem(request,id=None):
    userdata=RtUser.objects.get(id=id)
    r = requests.get('http://'+userdata.ip_address+':9595/shutdown', params=request.GET)
    a=r.json()
    if a:
        messages.success(request,"System shutdown sucessfully!")
        return render(request, 'admin/shutdown_system.html', {"user_details": userdata})

def livemonitoring(request):
    obj = RtUser.objects.all()

    return render(request,'admin/livemonitoring.html', {'user_details':obj})

def livemonitoringpage(request,id=None):
    userdata=RtUser.objects.get(id=id)

    r = requests.get('http://'+userdata.ip_address+':9595/monitoring', params=request.GET)
    print('rrrr',r)
    a=r.json()
    json_response = json.dumps(a, indent=3)
    context = {
        'data':json_response
    }
    return render(request,'admin/livemonitoringpage.html',context)



############################################################################################################################################################################


def blocksite(request):
    obj = RtUser.objects.all()

    return render(request,'admin/blocksite.html', {'user_details':obj})


def blocksitepage(request,id=None):
    userdata = RtUser.objects.get(id=id)
    if request.method=='POST':
        data=request.POST.get('q')
        r = requests.get('http://'+userdata.ip_address+':9595/blocksite',data={'address':data})
        print('rrrr',r)
        messages.success(request,"Process killed sucessfully!")
        return render(request,'admin/blocksitepage.html',{'data':userdata})

    return render(request,'admin/blocksitepage.html',{'data':userdata})