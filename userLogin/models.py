# Create your models here.
from datetime import timedelta
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

def aadharPic(instance,file):
    return f"{instance.mobile}/{instance.aadhar}-Aadhar/{file}"
def profile(instance,file):
    return f"{instance.mobile}/profilePic/{file}"

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=200,default="Name")
    email = models.EmailField(max_length=150,unique=True,default="Email")
    dob = models.DateField(default="ddmmyy")
    designation = models.CharField(max_length=100,default="UGMT Member")
    gender = models.CharField(max_length=10,default="Gender")
    blood_group = models.CharField(max_length=5,default="Blood Group")
    state = models.CharField(max_length=100,default="State")
    district = models.CharField(max_length=100,default="District")
    zip_code = models.CharField(max_length=6, default="000000")
    address = models.TextField(default="Address")
    near_by = models.TextField(default="nearBy")
    mobile = models.CharField(max_length=10,default="Mobile")
    mobile_home = models.CharField(max_length=10, blank=True, null=True,default="Mobile")
    aadhar = models.CharField(max_length=15, unique=True,default="AadharNumber")
    aadharPhoto = models.ImageField(upload_to=aadharPic,default="defaultProfile.png")
    profilePic = models.ImageField(
        upload_to=profile,default="defaultProfile.png",
        validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'])]
    )
    #Nominee-1 Details
    nominee1_name = models.CharField(max_length=200,default="Nominee1-Name")
    nominee1_mobile = models.CharField(max_length=20,null=True, blank=True,default="Nominee1-Mobile")
    nominee1_relation = models.CharField(max_length=20,null=True, blank=True,default="Nominee1-Relation")
    # Chronic Disease
    chronic_disease = models.CharField(max_length=10,default="No")

    #Referrence Details
    refer_name = models.CharField(max_length=200,default="Refer Name")
    refer_id = models.CharField(max_length=10,null=True, blank=True,default="Refer id")
    refer_mobile = models.CharField(max_length=20,null=True, blank=True,default="Refer Mobile")


    is_verified = models.BooleanField(default=False)
    registerDate = models.DateField(timezone.now)
    expiring_Date = models.DateField(timezone.now()  + timedelta(days=365)) 
    password = models.TextField()

    # ADDON
    home_flag = models.BooleanField(default=False)  # Show on Home flag

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile']  # Include mobile in required fields but email is used for login

    objects = CustomUserManager()


class Notice(models.Model):
    date = models.DateField(default=timezone.now)
    notice_text = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="creatorNotice")
    is_delete = models.BooleanField(default=False)

class CharityAlert(models.Model):
    date = models.DateField(default=timezone.now)
    text_area = models.TextField()
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Receiver")
    receiverNominee = models.CharField(max_length=15, unique=False,default="NomineeAadhar")
    bank_name = models.CharField(max_length=200, default="Bank Name")
    upi_id = models.CharField(max_length=200, default="UPI ID")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_per_member = models.DecimalField(max_digits=10, decimal_places=2)
    generated_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="creatorAlert")
    is_delete = models.BooleanField(default=False)
    donation_status = models.BooleanField(default=False)
    
class DonationTransactionID(models.Model):
    transaction_id = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="donor")
    charity_alert = models.ForeignKey(CharityAlert, on_delete=models.CASCADE, related_name="donation_request")
    date = models.DateField(default=timezone.now)
    is_matched = models.BooleanField(default=False)


class TrustDonationID(models.Model):
    transaction_id = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200,default="Name")
    mobile = models.CharField(max_length=10,default="Mobile")
    date = models.DateField(default=timezone.now)
    is_matched = models.BooleanField(default=False)

class DonatedTo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="donor_history")
    charity_alert = models.ForeignKey(CharityAlert, on_delete=models.CASCADE, related_name="donation_history")
    date = models.DateField(default=timezone.now)


# --- UPDATE MEDIA FILES
from datetime import datetime
def ngo_media_upload_path(instance, filename):
    today = datetime.now().strftime('%Y-%m-%d')
    return f"UGMTmedia/{today}/{filename}"

class NGOPost(models.Model):
    caption = models.CharField(max_length=255, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ngo_posts')
    created_at = models.DateTimeField(default=timezone.now)
    event_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Post by {self.created_by.name} on {self.created_at.strftime('%Y-%m-%d')}"

class NGOMedia(models.Model):
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )

    post = models.ForeignKey(NGOPost, on_delete=models.CASCADE, related_name='media_files',null=True, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ngo_media')
    media_file = models.FileField(
        upload_to=ngo_media_upload_path,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'mp4', 'mov', 'avi', 'webm'])]
    )
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    # uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(default=timezone.now)
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.media_type} for Post {self.post.id}"

# ------------------