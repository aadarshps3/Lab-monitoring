from django.contrib import admin
from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib import messages
# Register your models here.

admin.site.register(RtUser)
admin.site.register(screenshotdata)
admin.site.register(monitoring)
admin.site.register(userlog)


##################################################################### Admin Module ##################################################################################

#
# ##################### load Home page ###########################
#
# def load_home(request):
#
#     return render(request,'admin/admin_homepage.html')
#
#
# ##################### Add Users #################################
#
# def add_user(request):
#     form=TUserCreationForm()
#
#     if request.method == "POST":
#
#         form = TUserCreationForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             messages.success(request,"The user has been added sucessfully!")
#
#
#
#
#     return render(request,'admin/admin_user_add.html',{"forms":form})
#
#
#
#
#
# ########################## View Users ################################
#
#
# def view_user(request):
#     obj=RtUser.objects.all()
#
#     if request.method =="POST":
#         req_id=request.POST.get("remove_id")
#
#         try:
#             obj_delete=RtUser.objects.get(id=req_id)
#
#         except RtUser.DoesNotExist:
#             obj_delete = None
#
#         obj_delete.delete()
#
#     return  render(request,'admin/view_users.html',{"user_details":obj})
#
#
# ################################ Take screenshots ########################
#
# def take_screenshots(request):
#     obj = RtUser.objects.all()
#
#     return render(request,'admin/screenshot_system.html',{"user_details":obj})
#
# ################################ Shutdown  system ############################
#
# def shutdown_system(request):
#     obj = RtUser.objects.all()
#
#     return render(request, 'admin/shutdown_system.html', {"user_details": obj})
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# ############################################################################################################################################################################
#
