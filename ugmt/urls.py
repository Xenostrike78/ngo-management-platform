"""
URL configuration for ugmt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from userLogin import views as userView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.home,name="home"),
    path('about',views.about,name="about"),

    path('view-gallery',views.view_gallery,name="gallery"),
    path('gallery/single/post/<int:post_id>',views.single_post,name="single_post"),
    
    path('memberList',views.memberList,name="memberList"),
    path('vyawasthList',views.vyawasthList,name="vyawasthList"),
    path('niyamawaliList',views.niyamawaliList,name="niyamawaliList"),
    path('contactUs',views.contactUs,name="contactUs"),
    path('viewAllNotice',views.viewNotice,name="AllNotices"),
    path('viewAllAlert',views.viewAlert,name="AllAlert"),
    path("login/",include("userLogin.loginUrl")),
    re_path(r'^media/(?P<path>.*)$', views.SecureMediaProxyView.as_view()),

    path('api/delete-post/<int:post_id>/', userView.delete_post, name='delete_post_api'),
    path("api/update-designation/<int:member_id>/", userView.update_designation, name="update_designation"),
    path('make-home-flag/<int:user_id>/', userView.make_home_flag, name='make_home_flag'),
    path('make-admin/<int:user_id>/', userView.make_admin, name='make_admin'),

]
# + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

from django_ratelimit.exceptions import Ratelimited
from django.shortcuts import render

def custom_ratelimit_handler(request, exception=None):
    if isinstance(exception, Ratelimited):
        return render(request, "errorPage.html", {
            "sus": "🚫 Too many OTP requests from your IP."
        }, status=429)
    return render(request, "errorPage.html", {"sus": "Forbidden. IP address blocked"}, status=403)

handler403 = custom_ratelimit_handler