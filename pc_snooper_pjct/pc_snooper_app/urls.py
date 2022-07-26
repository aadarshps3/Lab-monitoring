"""pc_snooper_pjct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
# from .import admin
from . import views
urlpatterns = [
    path('',views.login_page,name="login_page"),
    path("home",views.load_home,name="admin_home"),

    ############################## Admin add users url ######################

    path("admin_add_users",views.add_user,name="add_user"),

    ############################# Admin view Users url #######################

    path("admin_view_users",views.view_user,name="user_view"),

    ############################## Admin Shut down the system ################

    path("admin_shutdown_system",views.shutdown_system,name="system_shutdown"),

    ############################## Admin take screenshots ###################

    path('admin_take_screenshots',views.take_screenshots,name="system_screenshots"),
    path('takescreenshot/<int:id>/',views.takescreenshot,name="takescreenshot"),
    path('viewsreenshots/<int:id>/',views.viewsreenshots,name="viewsreenshots"),
    path('currentactivity',views.currentactivity,name="currentactivity"),
    path('currentactivitydata/<int:id>/',views.currentactivitydata,name="currentactivitydata"),
    path('allactivity',views.allactivity,name="allactivity"),
    path('allactivitydata/<int:id>/',views.allactivitydata,name="allactivitydata"),
    path('killprocess',views.killprocess,name="killprocess"),
    path('killaprocess/<int:id>/',views.killaprocess,name="killaprocess"),
    path('shutdownsystem/<int:id>/',views.shutdownsystem,name="shutdownsystem"),
    path('livemonitoring',views.livemonitoring,name="livemonitoring"),
    path('livemonitoringpage/<int:id>/',views.livemonitoringpage,name="livemonitoringpage"),
    path('blocksite',views.blocksite,name="blocksite"),
    path('blocksitepage/<int:id>/',views.blocksitepage,name="blocksitepage"),



    ##################################################################################################################################################
]
