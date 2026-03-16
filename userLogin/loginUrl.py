
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('loginPage',views.login,name="login"),
    path('logout',views.logout,name="logout"),

    path('forgetPassword',views.forgetPassword,name="forgetPassword"),
    path('OTPverify/<str:email>/<str:token>/',views.verify_otp,name="otp"),
    path('resetPassword/<str:token>',views.resetPassword,name="reset_password"),
    
    path('sendOTP',views.sendOTP,name="SendOTP"),
    path('verifyEmail/<str:email>/<str:token>/',views.verify_email,name="VerifyEmail"),
    path('register/<str:token>/',views.register,name="register"),
    path('membership-Payment/UserCreated/',views.membershipPayment,name="MembershipPayment"),

    path('renew-token/', views.renew_token, name='renew_token'),
    path('renew-membership/<str:token>/', views.renew_membership, name='renewMembership'),
    path('renew-membership-complete/<str:token>/200/Success', views.renew_membership_success, name='renewMembershipSuccess'),
    
    path('token-Charity/<str:id>/<str:charityId>/tokengenerate',views.charityToken,name="tokenCharity"),
    path('scanQR/<str:token>/?<str:nominee_id>/?<str:token1>/?<str:charityId>',views.CharityPayment,name="CharityPayment"),
    path('downloading-QR/?<str:token>/?+<str:nomineeID>/?-<str:charityID>',views.downloadQR,name="downloadQR"),
    
    
    path('searchMembers',views.searchMember,name="searchMembers"),
    path('download_users_data/', views.download_users_data, name='download_users_data'),
    path('download_user_data/<str:memberID>/', views.download_user_data, name='download_user_data'),
    path('verify-Members',views.memberVerification,name="verifyMembers"),
    path('member-Info/<str:memberID>/',views.memberInfo,name="memberInfo"),
    path('genNotice',views.genNotice,name="genNotice"),
    path('genAlert',views.genAlert,name="genAlert"),
    path('viewNotice',views.viewNotice,name="viewNotice"),
    path('viewAlert',views.viewAlert,name="viewAlert"),
    path('checkDonation',views.checkTrustID,name="CheckDonation"),

    path('gallery-management',views.gallery_management,name="GalleryManagement"),

    path('token-idCheck/<str:charityId>/tokengenerate',views.idCheckToken,name="tokenIDcheck"),
    path('check-transactionID/<str:token>/?<str:charityId>/?<str:token1>',views.checkID,name="idCheck"),

    path('donatedTo',views.donatedTo,name="donatedTo"),
    path('profile',views.profile,name="profile"),

]
