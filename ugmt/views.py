from django.shortcuts import render,redirect
from userLogin.models import User,Notice,CharityAlert,NGOMedia,NGOPost
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings

import os
from django.http import FileResponse, Http404
from django.views import View

class SecureMediaProxyView(View):
    def get(self, request, path):
        # Absolute file path
        file_path = os.path.join(settings.MEDIA_ROOT, path)

        # Check if file exists
        if not os.path.exists(file_path):
            raise Http404("File does not exist")

        # ✅ Allow profile pictures to be shown publicly
        if 'profile' in path.lower()  or 'ugmtmedia' in path.lower():
            return FileResponse(open(file_path, 'rb'))

        # ✅ Allow logged-in users to access other files (like Aadhaar)
        if request.user.is_authenticated:
            if os.path.isfile(file_path):
                return FileResponse(open(file_path, 'rb'))
            raise Http404("File not found")
            # return FileResponse(open(file_path, 'rb'))

        # ❌ Block all other access attempts
        raise Http404("Unauthorized")


def home(request):
    try:
        latest_media = NGOMedia.objects.filter(media_type="image").order_by('-uploaded_at')[:8]
        users = User.objects.filter(is_verified=True,home_flag=True).order_by("id")[:20]
        charity = CharityAlert.objects.filter(is_delete=False).order_by("id")[::-1]
        notice = Notice.objects.filter(is_delete=False).order_by("id")[::-1]
        return render(request,"home.html",{"usersDatass":users,"Alert":charity,"Notice":notice,'latest_media': latest_media})
    except Exception as e:
        return render(request,"errorPage.html",{"error": e})

def about(request):
    return render(request,"aboutUs.html")

def view_gallery(request):
    posts = NGOPost.objects.prefetch_related('media_files').order_by('-event_date')
    posts_data = []

    month = request.GET.get("month")
    year = request.GET.get("year")

    # Apply filters if provided
    if year:
        yea = int(year)
        posts = posts.filter(event_date__year=yea)
    if month:
        mon = int(month)
        posts = posts.filter(event_date__month=mon)

    # If no filters applied → limit to 5 latest posts
    if not month and not year:
        posts = posts[:12]

    for post in posts:
        media_list = []
        for media in post.media_files.all():
            if media.media_type == "video":
                media_list.append({'type': "video", 'url': media.media_file})
            else:
                media_list.append({'type': "image", 'url': media.media_file.url})

        posts_data.append({
            'id': post.id,
            'caption': post.caption,
            'date': post.event_date.strftime('%B %d, %Y'),
            'media': media_list,
            'count': len(media_list),
        })
    return render(request, 'Gallery/ourWork.html',{"posts_data":posts_data,"s_month":month,"s_year":year})

def single_post(request,post_id):
    try:
        post = NGOPost.objects.prefetch_related('media_files').get(id=post_id)
    except NGOPost.DoesNotExist:
        return redirect("view_gallery")   # fallback

    media_list = []
    for media in post.media_files.all():
        if media.media_type == "video":
            media_list.append({'type': "video", 'url': media.media_file})
        else:
            media_list.append({'type': "image", 'url': media.media_file.url})


    post_data = {
        'id': post.id,
        'caption': post.caption,
        'date': post.event_date.strftime('%B %d, %Y') if post.event_date else "",
        'media': media_list,
    }
    return render(request, "Gallery/galleryPost.html", {"post": post_data})


def memberList(request):
    try:
        users = User.objects.filter(is_verified=True).order_by("id")
        paginator = Paginator(users, 15) 
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,"memberList.html",{"usersDatass": page_obj})
    except Exception as e:
        return render(request,"errorPage.html",{"error": e})

def vyawasthList(request):
    return render(request,"vyawasthList.html")

def niyamawaliList(request):
    return render(request,"niyamawali.html")

def viewNotice(request):
    try:
        notice = Notice.objects.filter(is_delete=False).order_by("id")[::-1]
        return render(request,"viewAllNotice.html",{"Notices":notice})
    except Exception as e:
        return render(request,"errorPage.html",{"error": e})

def viewAlert(request):
    try:
        charity = CharityAlert.objects.filter(is_delete=False).order_by("id")[::-1]
        return render(request,"viewAllCharity.html",{"Charity":charity})
    except Exception as e:
        return render(request,"errorPage.html",{"error": e})

def contactUs(request):
    try:
        if request.method=="POST":
            name=request.POST.get("Name")
            subject=request.POST.get("Subject")
            number=request.POST.get("PhoneNumber")
            email=request.POST.get("email")
            content=request.POST.get("content")
            send_mail(
                "UGMT received an inquiry",
                f"Name: {name}\n Subject: {subject}\n Number: {number}\n Email: {email}\nContent: \n{content}",
                settings.EMAIL_HOST,['uniquegroupofmankindtrust@gmail.com'],fail_silently=False)
            return redirect("home")
        else:
            if request.user.is_authenticated:
                user = User.objects.get(email=request.user)
                return render(request,"contactUs.html",{"userContact":user})
            else:
                user=None
                return render(request,"contactUs.html",{"userContact":user})
    except Exception as e:
        return render(request,"errorPage.html",{"error": e})

