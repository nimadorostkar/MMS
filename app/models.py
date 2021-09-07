from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.template.defaultfilters import truncatechars
from extensions.utils import jalali_converter
from mptt.models import MPTTModel, TreeForeignKey





#------------------------------------------------------------------------------
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True,related_name='profile',verbose_name = "کاربر")
  phone = models.CharField(max_length=50,null=True, blank=True,verbose_name = " شماره تماس  ")
  address = models.CharField(max_length=3000,null=True, blank=True,verbose_name = " آدرس  ")
  user_photo = models.ImageField(upload_to='user_uploads/user_photo',default='user_uploads/user_photo/default.png',null=True, blank=True,verbose_name = "تصویر کاربر")


  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
      if created:
          Profile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
      instance.profile.save()

  def image_tag(self):
        return format_html("<img width=50 src='{}'>".format(self.user_photo.url))

  def user_name(self):
        return str(self.user)

  class Meta:
      verbose_name = "پروفایل"
      verbose_name_plural = " پروفایل ها "

  def __str__(self):
    return "پروفایل : " + str(self.user)







#------------------------------------------------------------------------------
class Product(models.Model):
    Name = models.CharField(max_length=200, unique=True, verbose_name = "نام")
    Description = models.TextField(max_length=1000, null=True, blank=True, verbose_name = "توضیحات")
    Image = models.ImageField(upload_to='media', default='media/Default.png', null=True, blank=True, verbose_name = "تصویر")


    def image_tag(self):
        return format_html("<img width=50 src='{}'>".format(self.Image.url))

    def __str__(self):
      return str(self.Name)

    @property
    def short_description(self):
        return truncatechars(self.Description, 60)

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"



#------------------------------------------------------------------------------
class Manufacturer(models.Model):
    Name = models.CharField(max_length=200, unique=True, verbose_name = "نام")
    Description = models.TextField(max_length=1000, null=True, blank=True, verbose_name = "توضیحات")


    def __str__(self):
      return str(self.Name)

    @property
    def short_description(self):
        return truncatechars(self.Description, 60)

    class Meta:
        verbose_name = "سازنده"
        verbose_name_plural = "سازندگان"





#------------------------------------------------------------------------------
class Mold(models.Model):
    Name = models.CharField(max_length=200, unique=True, verbose_name = "نام")
    Code = models.CharField(max_length=40, null=True, blank=True, unique=True, verbose_name = "کد")
    CHOICES = (('فلزی','فلزی'), ('پلاستیکی','پلاستیکی'), ('دایکست','دایکست'), ('فورج','فورج'))
    Type = models.CharField(max_length=15, choices=CHOICES, verbose_name = "نوع قالب")
    Piece_id = models.CharField(max_length=40, null=True, blank=True, unique=True, verbose_name = "شناسه قطعه")
    Cavities_qty = models.IntegerField(default='1', null=True, blank=True, verbose_name = "تعداد حفره")
    Cavities_id = models.CharField(max_length=40, null=True, blank=True, verbose_name = "شناسه حفره")
    Healthy_Cavities_qty = models.IntegerField(default='1', null=True, blank=True, verbose_name = "تعداد حفره های سالم")
    Manufacturer = models.ForeignKey(Manufacturer ,on_delete=models.CASCADE ,null=True, blank=True, verbose_name = "سازنده")
    Year = models.CharField(max_length=40, null=True, blank=True, verbose_name = "سال ساخت")                                     # Date just year
    Mold_qty = models.IntegerField(default='1', null=True, blank=True, verbose_name = "تعداد قالب")
    Related_product = models.ManyToManyField(Product, related_name='Product', verbose_name = "محصولات مرتبط")
    Category = models.CharField(max_length=40, null=True, blank=True, verbose_name = "دسته بندی")                                #ForeignKey or MPTT
    Material = models.CharField(max_length=40, null=True, blank=True, verbose_name = "متریال طراحی")                             #CHOICES
    Image = models.ImageField(upload_to='media', default='media/Default.png', null=True, blank=True, verbose_name = "تصویر")     #multi image
    File = models.FileField(default='media/Default.png', null=True, blank=True, verbose_name ="فایل")
    Address = models.CharField(max_length=500, null=True, blank=True, verbose_name = "آدرس")
    Description = models.TextField(max_length=1000, null=True, blank=True, verbose_name = "توضیحات")


    def image_tag(self):
        return format_html("<img width=50 src='{}'>".format(self.Image.url))

    def __str__(self):
      return str(self.Name)

    class Meta:
        verbose_name = "قالب"
        verbose_name_plural = "قالب ها"





#------------------------------------------------------------------------------
# MPTT Model -->  https://django-mptt.readthedocs.io/en/latest/index.html
class Category(MPTTModel):
    name = models.ForeignKey(Mold, on_delete=models.CASCADE, related_name = "mat_name", verbose_name = "نام قالب")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',verbose_name = "والد")


    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __unicode__(self):
        return u"%s" % (self.name)

    def __str__(self):
        return str(self.name)















#-------------------------------------------------------- by Nima Dorostkar ---
