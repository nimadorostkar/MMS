from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.template.defaultfilters import truncatechars
from mptt.models import MPTTModel, TreeForeignKey
from django.core.validators import MaxValueValidator, MinValueValidator



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

    def get_absolute_url(self):
        return reverse('app:product_detail',args=[self.id])

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

    def get_absolute_url(self):
        return reverse('app:manufacturer_detail',args=[self.id])

    @property
    def short_description(self):
        return truncatechars(self.Description, 60)

    class Meta:
        verbose_name = "سازنده"
        verbose_name_plural = "سازندگان"






#------------------------------------------------------------------------------
class Category(MPTTModel):
    name = models.CharField(max_length=200, unique=True, verbose_name = "نام")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',verbose_name = "والد")


    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def get_absolute_url(self):
        return reverse('app:category_detail',args=[self.id])

    def __unicode__(self):
        return u"%s" % (self.name)

    def __str__(self):
        return str(self.name)





#------------------------------------------------------------------------------
class Mold_type(models.Model):
    Name = models.CharField(max_length=200, unique=True, verbose_name = "نام")

    def __str__(self):
      return str(self.Name)

    class Meta:
        verbose_name = "نوع قالب"
        verbose_name_plural = "نوع قالب ها"





#------------------------------------------------------------------------------
class Piece_id(models.Model):
    Name = models.CharField(max_length=200, unique=True, verbose_name = "نام")

    def __str__(self):
      return str(self.Name)

    class Meta:
        verbose_name = "شناسه قطعه"
        verbose_name_plural = "شناسه قطعه ها"






#------------------------------------------------------------------------------
class Mold(models.Model):
    Name = models.CharField(max_length=200, unique=True, verbose_name = "نام")
    Code = models.CharField(max_length=40, null=True, blank=True, unique=True, verbose_name = "کد")
    Type = models.ForeignKey(Mold_type ,on_delete=models.CASCADE ,null=True, blank=True, verbose_name = "نوع قالب")
    Piece_id = models.ForeignKey(Piece_id ,on_delete=models.CASCADE ,null=True, blank=True, verbose_name = "شناسه قطعه")
    Cavities_qty = models.IntegerField(default='1', null=True, blank=True, verbose_name = "تعداد حفره")
    Cavities_id = models.CharField(max_length=40, null=True, blank=True, verbose_name = "شناسه حفره")
    Healthy_Cavities_qty = models.IntegerField(default='1', null=True, blank=True, verbose_name = "تعداد حفره های سالم")
    Manufacturer = models.ForeignKey(Manufacturer ,on_delete=models.CASCADE ,null=True, blank=True, verbose_name = "سازنده")
    Related_product = models.ManyToManyField(Product, related_name='Product', verbose_name = "محصولات مرتبط")
    Year = models.CharField(max_length=40, null=True, blank=True, verbose_name = "سال ساخت")                                     # Date just year
    Mold_qty = models.IntegerField(default='1', null=True, blank=True, verbose_name = "تعداد قالب")
    Category = models.ForeignKey(Category ,on_delete=models.CASCADE ,null=True, blank=True, verbose_name = "دسته بندی")
    Material = models.CharField(max_length=40, null=True, blank=True, verbose_name = "متریال طراحی")                             #CHOICES
    File = models.FileField(default='media/Default.png', null=True, blank=True, verbose_name ="فایل")
    Address = models.CharField(max_length=500, null=True, blank=True, verbose_name = "آدرس")
    Description = models.TextField(max_length=1000, null=True, blank=True, verbose_name = "توضیحات")


    def __str__(self):
      return str(self.Name)

    def get_absolute_url(self):
        return reverse('app:mold_detail',args=[self.id])

    class Meta:
        verbose_name = "قالب"
        verbose_name_plural = "قالب ها"

#https://stackoverflow.com/questions/537593/multiple-images-per-model
class MoldImage(models.Model):
    property = models.ForeignKey(Mold, on_delete=models.CASCADE, related_name='images')
    Image = models.ImageField(upload_to='media', default='media/Default.png', null=True, blank=True, verbose_name = "تصویر")

    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "تصویر ها"







#------------------------------------------------------------------------------
class Repair_request(models.Model):
    Mold = models.ForeignKey(Mold ,on_delete=models.CASCADE, verbose_name = "قالب")
    Applicant = models.CharField(max_length=50, null=True, blank=True, verbose_name = "درخواست کننده")
    Description = models.TextField(max_length=1000, null=True, blank=True, verbose_name = "توضیحات مشکل وارد شده")
    StartTime = models.DateField(null=True, blank=True, verbose_name = "تاریخ درخواست")
    CheckTime = models.DateField(null=True, blank=True, verbose_name = "تاریخ بررسی")
    TestTime = models.DateField(null=True, blank=True, verbose_name = "تاریخ تست")
    EndTime = models.DateField(null=True, blank=True, verbose_name = "تاریخ اتمام")
    CHOICES = (('به اتمام رسیده','به اتمام رسیده'), ('نامشخص','نامشخص'), ('رد شده','رد شده'))
    Status=models.CharField(max_length=20,choices=CHOICES, default='نامشخص', verbose_name = "وضعیت")

    def __str__(self):
      return str(self.Mold)

    def get_absolute_url(self):
        return reverse('app:repair_req_detail',args=[self.id])

    class Meta:
        verbose_name = "درخواست تعمیر"
        verbose_name_plural = "درخواست تعمیرات"


class RepairImage(models.Model):
    property = models.ForeignKey(Repair_request, on_delete=models.CASCADE, related_name='images')
    Image = models.ImageField(upload_to='media', default='media/Default.png', null=True, blank=True, verbose_name = "تصویر")

    class Meta:
        verbose_name = "تصویر مشکل"
        verbose_name_plural = "تصویر های مشکل"






#------------------------------------------------------------------------------
class Repair_operation(models.Model):
    Request = models.ForeignKey(Repair_request ,on_delete=models.CASCADE, verbose_name = "برای درخواست")
    CHOICES = ( ('اول','اول'), ('دوم','دوم'), ('سوم','سوم'), ('چهارم','چهارم'), ('پنجم','پنجم'), ('ششم','ششم'), ('هفتم','هفتم'), ('هشتم','هشتم'), ('نهم','نهم'), ('دهم','دهم') )
    Step=models.CharField(max_length=20,choices=CHOICES, verbose_name = "گام")
    Description = models.TextField(max_length=1000, null=True, blank=True, verbose_name = "توضیحات عملیات تعمیر")


    def __str__(self):
      return "گام : " + str(self.Step) + " درخواست تعمیر : " + str(self.Request)

    def get_absolute_url(self):
        return reverse('app:repair_operation_detail',args=[self.id])

    @property
    def short_description(self):
        return truncatechars(self.Description, 60)

    class Meta:
        verbose_name = " عملیات تعمیر "
        verbose_name_plural = " عملیات تعمیرات "

class OperationImage(models.Model):
    property = models.ForeignKey(Repair_operation, on_delete=models.CASCADE, related_name='images')
    Image = models.ImageField(upload_to='media', default='media/Default.png', null=True, blank=True, verbose_name = "تصویر")

    class Meta:
        verbose_name = "تصویر عملیات"
        verbose_name_plural = "تصاویر عملیات"








#------------------------------------------------------------------------------
class Manufacture_request(models.Model):
    Mold = models.ForeignKey(Mold ,on_delete=models.CASCADE, verbose_name = "قالب")
    Applicant = models.CharField(max_length=50, null=True, blank=True, verbose_name = "درخواست کننده")
    Progress_bar = models.IntegerField(default='1', null=True, blank=True,validators=[MinValueValidator(1),MaxValueValidator(100)], verbose_name = "درصد پیشرفت" )
    Image = models.ImageField(upload_to='media', default='media/Default.png', null=True, blank=True, verbose_name = "تصویر آخرین وضعیت ساخت")
    Description=models.TextField(max_length=1000, null=True, blank=True, verbose_name = "توضیحات")
    StartTime = models.DateField(null=True, blank=True, verbose_name = "تاریخ درخواست")
    CheckTime = models.DateField(null=True, blank=True, verbose_name = "تاریخ بررسی")
    TestTime = models.DateField(null=True, blank=True, verbose_name = "تاریخ تست")
    EndTime = models.DateField(null=True, blank=True, verbose_name = "تاریخ اتمام")
    CHOICES = (('به اتمام رسیده','به اتمام رسیده'), ('نامشخص','نامشخص'), ('رد شده','رد شده'))
    Status=models.CharField(max_length=20,choices=CHOICES, default='نامشخص', verbose_name = "وضعیت")


    def __str__(self):
      return str(self.Mold)

    def get_absolute_url(self):
        return reverse('app:manufacture_req_detail',args=[self.id])

    class Meta:
        verbose_name = "درخواست ساخت قاب"
        verbose_name_plural = "درخواست های ساخت قالب"




#------------------------------------------------------------------------------
class Component_request(models.Model):
    Applicant = models.CharField(max_length=50, null=True, blank=True, verbose_name = "درخواست کننده")
    Description = models.TextField(max_length=1000, null=True, blank=True, verbose_name = "شرح درخواست")
    StartTime = models.DateField(null=True, blank=True, verbose_name = "تاریخ درخواست")
    CheckTime = models.DateField(null=True, blank=True, verbose_name = "تاریخ بررسی")
    TestTime = models.DateField(null=True, blank=True, verbose_name = "تاریخ تست")
    EndTime = models.DateField(null=True, blank=True, verbose_name = "تاریخ اتمام")
    Progress_bar = models.IntegerField(default='1', null=True, blank=True,validators=[MinValueValidator(1),MaxValueValidator(100)], verbose_name = "درصد پیشرفت" )
    CHOICES = (('به اتمام رسیده','به اتمام رسیده'), ('نامشخص','نامشخص'), ('رد شده','رد شده'))
    Status=models.CharField(max_length=20,choices=CHOICES, default='نامشخص', verbose_name = "وضعیت")

    @property
    def short_description(self):
        return truncatechars(self.Description, 40)

    def __str__(self):
        return str(self.short_description)

    def get_absolute_url(self):
        return reverse('app:component_req_detail',args=[self.id])



    class Meta:
        verbose_name = "درخواست ساخت"
        verbose_name_plural = "درخواست های ساخت"

class ComponentImage(models.Model):
    property = models.ForeignKey(Component_request, on_delete=models.CASCADE, related_name='images')
    Image = models.ImageField(upload_to='media', default='media/Default.png', null=True, blank=True, verbose_name = "تصویر")

    class Meta:
        verbose_name = "تصویر ساخت"
        verbose_name_plural = "تصاویر ساخت"










#-------------------------------------------------------- by Nima Dorostkar ---
