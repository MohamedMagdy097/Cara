from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    address = models.CharField(max_length = 511)
    mobile = models.CharField(max_length = 20, null = False)
    profile_pic = models.ImageField(upload_to = 'static/img/', null = True, blank = True)
    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

class Site(models.Model):
    # logo inside navbar
    logo = models.ImageField(upload_to='static/img/')
    
    # hero text
    hero_h4 = models.TextField()
    hero_h2 = models.TextField()
    hero_h1 = models.TextField()
    hero_p = models.TextField()
    hero_button_text = models.CharField(max_length=255)
    
    # features images
    feature1_img = models.ImageField(upload_to='static/img/')
    feature2_img = models.ImageField(upload_to='static/img/')
    feature3_img = models.ImageField(upload_to='static/img/')
    feature4_img = models.ImageField(upload_to='static/img/')
    feature5_img = models.ImageField(upload_to='static/img/')
    feature6_img = models.ImageField(upload_to='static/img/')
    # features text
    feature1_text = models.CharField(max_length=255)
    feature2_text = models.CharField(max_length=255)
    feature3_text = models.CharField(max_length=255)
    feature4_text = models.CharField(max_length=255)
    feature5_text = models.CharField(max_length=255)
    feature6_text = models.CharField(max_length=255)
    
    # banner
    banner_h4 = models.CharField(max_length=255)
    banner_h2 = models.TextField()
    banner_button_text = models.CharField(max_length=255)
    
    # small banner1
    sm_banner1_h4 = models.CharField(max_length=255)
    sm_banner1_h2 = models.TextField()
    sm_banner1_span = models.TextField()
    sm_banner1_button_text = models.CharField(max_length=255)
    # small banner2
    sm_banner2_h4 = models.CharField(max_length=255)
    sm_banner2_h2 = models.TextField()
    sm_banner2_span = models.TextField()
    sm_banner2_button_text = models.CharField(max_length=255)
    
    # very small banner1
    vsm_banner1_h4 = models.CharField(max_length=255)
    vsm_banner1_h2 = models.TextField()
    # very small banner2
    vsm_banner2_h4 = models.CharField(max_length=255)
    vsm_banner2_h2 = models.TextField()
    # very small banner3
    vsm_banner3_h4 = models.CharField(max_length=255)
    vsm_banner3_h2 = models.TextField()
    
    # contact
    contact_label = models.CharField(max_length=255)
    address_label = models.CharField(max_length=255)
    address = models.TextField()
    phone_label = models.CharField(max_length=255)
    phone = models.TextField()
    hours_label = models.CharField(max_length=255)
    hours = models.TextField()
    
    # follow us
    facebook = models.TextField()
    twitter = models.TextField()
    instagram = models.TextField()
    pinterest = models.TextField()
    youtube = models.TextField()
    
    # about
    about_label = models.CharField(max_length=255)
    about_us_label = models.CharField(max_length=255)
    about_us = models.TextField()
    delivery_information_label = models.CharField(max_length=255)
    delivery_information = models.TextField()
    privacy_policy_label = models.CharField(max_length=255)
    privacy_policy = models.TextField()
    terms_conditions_label = models.CharField(max_length=255)
    terms_conditions = models.TextField()
    contact_us_label = models.CharField(max_length=255)
    contact_us = models.TextField()
    
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-date_added']
        
class Shop(models.Model):
    # page header text
    page_header_h2 = models.CharField(max_length=255)
    page_header_p= models.TextField()
    hero_button_text = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_added']
             
class Product(models.Model):
    slug = models.SlugField()
    
    # product
    img = models.ImageField(upload_to='static/img/')
    seller = models.CharField(max_length=255)
    name = models.TextField()
    stars = models.IntegerField()
    price = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField()
    new = models.BooleanField()
    added = models.BooleanField()
    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.name
        
class ProductDetail(models.Model):
    slug = models.ForeignKey(Product, related_name='details', on_delete=models.CASCADE, blank=True, null=True)
    img1 = models.ImageField(upload_to='static/img/', blank=True, null=True)
    img2 = models.ImageField(upload_to='static/img/', blank=True, null=True)
    img3 = models.ImageField(upload_to='static/img/', blank=True, null=True)
    description = models.TextField(blank = True, null = True)
    
