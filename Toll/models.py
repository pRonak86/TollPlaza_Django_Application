import uuid
from collections import defaultdict
from datetime import datetime
from random import random

from django.db.models import Max

from Toll.util import generate_random_string as id_generator
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw
# Create your models here.

class Customer_Registration(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    contact=models.IntegerField(max_length=10)
    emailid=models.EmailField()
    gender=models.CharField(max_length=20)
    vehicalNo=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    registration_Date = models.DateTimeField(default=datetime.now,blank=True)
    activation_Date=models.DateTimeField(null=True)
    deactivation_Date = models.DateTimeField(null=True)
    account=models.CharField(max_length=20,default="Deactive")
    qr_code=models.ImageField(upload_to='qr_codes',blank=True)

    def __str__(self):
        return self.fname

    def save(self,*args,**kwargs):
        qrcode_img=qrcode.make(self.vehicalNo)
        canvas = Image.new('RGB',(290,290),'white')
        draw= ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname=f'qr_code-{self.fname}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname,File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)

class Ewallet(models.Model):
    transactionID=models.CharField(max_length=100, blank=True, unique=True,editable=False)
    amount=models.IntegerField()
    mode=models.CharField(max_length=20)
    transaction_Date = models.DateTimeField(default=datetime.now, blank=True)
    EmpId=models.IntegerField(default=None)
    cust_id=models.IntegerField()

    def save(self):
        if not self.transactionID:
            self.transactionID=id_generator()
            while Ewallet.objects.filter(transactionID=self.transactionID).exists():
                self.transactionID=id_generator()
        super(Ewallet, self).save()




class Employee(models.Model):
    e_fname=models.CharField(max_length=20)
    e_lname=models.CharField(max_length=20)
    e_contact=models.IntegerField()
    e_email=models.EmailField()
    e_gender=models.CharField(max_length=20)
    e_bod=models.DateField()
    e_jod=models.DateTimeField(default=datetime.now,blank=True)
    e_bloodGroup=models.CharField(max_length=20)
    e_City=models.CharField(max_length=20)
    e_State=models.CharField(max_length=20)
    e_Coutry=models.CharField(max_length=20)
    e_empCode=models.CharField(primary_key=True,editable=False,max_length=10,unique=True)
    e_password=models.CharField(max_length=20)

    def save(self, **kwargs):
        no=Employee.objects.count() #Count method is used to count object form the Employee table
        if no==None:
            no= 1
        else:
            no= no+1
        self.e_empCode = "{}{:03}".format('EMP', no)
        super().save(*kwargs)

class FinalAmount(models.Model):
    cust_id=models.IntegerField()
    Total_Amount=models.IntegerField()
    transaction_Date = models.DateTimeField(default=datetime.now, blank=True)
