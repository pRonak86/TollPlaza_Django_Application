from datetime import date, datetime
from email.mime.image import MIMEImage
from unittest.mock import _patch

from django.core.mail import EmailMessage
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, redirect

from Toll.models import Customer_Registration, Ewallet, Employee, FinalAmount
from Toll.util import sendmail
from myProject.settings import EMAIL_HOST_USER


def indexPage(request):
    return render(request, 'index.html')


def homePage(request):
    return render(request, 'custRegistration.html')
    # return HttpResponse("This is the message")


def login(request):
    return render(request, 'custLogin.html')


def saveCustomer(request):
    fname = request.POST["fname"]
    lname = request.POST["lname"]
    contact = request.POST["contact"]
    email = request.POST["email"]
    gender = request.POST["gender"]
    vehicalNo = request.POST["vehicalNo"]
    address = request.POST["address"]
    City = request.POST["city"]
    State = request.POST["State"]
    password = request.POST["password"]
    request.session['email'] = email
    # today = date.today()
    # print(today)
    customer = Customer_Registration(fname=fname, lname=lname, contact=contact, emailid=email, gender=gender,
                                     vehicalNo=vehicalNo, address=address, city=City, state=State, password=password)
    s = customer.save()
    msg = "insert Data Successfull"
    return redirect("viewAllCustomerDetail")
    # return render(request,"success.html",{"msg":msg})


def viewAllCustomerDetail(request):
    if request.session.has_key('email'):
        email = request.session['email']
        cust = Customer_Registration.objects.filter(emailid=email)
        message = "Thanks For Registartion , Please wait we will Notify you Soon!!!"
        email_subject = "Registration"
        email = EmailMessage(email_subject, message, EMAIL_HOST_USER, [email])
        email.content_subtype = 'html'
        email.send()
        return render(request, "custLogin.html")


def validate(request):
    email = request.POST["email"]
    password = request.POST["password"]
    cust = Customer_Registration.objects.filter(emailid=email, password=password)
    if cust:
        if cust[0].account == "Active":
            id = cust[0].id
            print(id)
            fname = cust[0].fname
            qr_code = cust[0].qr_code
            ew = FinalAmount.objects.filter(cust_id=id)
            request.session["cust_id"]=id
            print(ew)
            if not ew:
                amount = 0
            else:
                amount = ew[0].Total_Amount
            return render(request, "cust_Dashboard.html", {'qr_code': qr_code, 'fname': fname, 'id': id, "amount": amount})
        else:
            msg = "You Account is Not activate Yet, Please wait till Administrator Active it. Try after Some Time"
            return render(request, "custLogin.html", {"msg": msg})
    else:
        msg = "Please Check Your Credentials"
        return render(request, "custLogin.html", {"msg": msg})
    ## from Here its pending 


def custDashboard(request):
    cust_id=request.session["cust_id"]
    cust=Customer_Registration.objects.filter(id=cust_id)
    qr_code=cust[0].qr_code
    fname=cust[0].fname
    ew = FinalAmount.objects.filter(cust_id=cust_id)
    amount=ew[0].Total_Amount
    print(cust_id)
    return render(request,"cust_Dashboard.html",{'qr_code': qr_code, 'fname': fname, 'id': id, "amount": amount})

def wallet(request):
    id = request.POST["id"]
    request.session['id'] = id
    return render(request, "wallet.html")


def amount(request):
    id = request.session["id"]
    ew = FinalAmount.objects.filter(cust_id=id)
    if not ew:
        amount_wallet = 0
        amount_request = request.POST["amount"]
        amount = amount_wallet + int(amount_request)
        mode = request.POST["mode"]
        EmpId = request.POST["empid"]
        cust = Customer_Registration.objects.get(pk=id)
        am = Ewallet(amount=amount, mode=mode, EmpId=EmpId, cust_id=id)
        am.save()
        final_amount=FinalAmount(cust_id=id,Total_Amount=amount)
        final_amount.save()
        last = Ewallet.objects.latest('id')
        transactionID = last.transactionID
        amount = last.amount
        msg = "Please find your Trancation Id - "
        return render(request, "cust_Dashboard.html",
                      {"id": id, "trancationId": transactionID, "fname": cust.fname, "qr_code": cust.qr_code,
                       "msg": msg, "amount": amount})
    else:
        amount_wallet = ew[0].Total_Amount
        if amount_wallet != 0:
            id1 = ew[0].pk
            amount_request = request.POST["amount"]
            amount = amount_wallet + int(amount_request)
            mode = request.POST["mode"]
            EmpId = request.POST["empid"]
            cust = Customer_Registration.objects.get(pk=id)
            am = Ewallet(amount=amount_request, mode=mode, EmpId=EmpId, cust_id=id)
            am.save()
            final_amount = FinalAmount(id=id1,cust_id=id,Total_Amount=amount)
            final_amount.save()
            last = Ewallet.objects.latest('id')
            transactionID = last.transactionID
            #amount = last.amount
            msg = "Please find your Trancation Id - "
            return render(request, "cust_Dashboard.html",
                              {"id": id, "trancationId": transactionID, "fname": cust.fname, "qr_code": cust.qr_code,
                               "msg": msg, "amount": amount})


def allTranscation(request):
    cust_id=request.session["cust_id"]
    al=Ewallet.objects.filter(cust_id=cust_id)
    print(al)
    return render(request,'allTranscation.html',{'al':al})


##################################### Admin Side ############################################

def adminLogin(request):
    return render(request, "adminLogin.html")

def dashPage(request):
    return render(request, "dashboardAdmin.html")

def adminDashPage(request):
    user=request.POST["User"]
    userName = request.POST["uname"]
    passWord = request.POST["pass"]
    if user=="Admin":
        if "Admin" == userName and passWord == "Admin":
            print("Hello")
            return render(request, "dashboardAdmin.html")
        else:
            msg = "Please Check Your Credentials"
            print("Hello1 ")
            return render(request, "adminLogin.html", {"msg": msg})
    else:
        return HttpResponse("This the Employee Page Called")


def adminAll(request):
    cust = Customer_Registration.objects.all()
    return render(request, "allCustomersAdmin.html", {"cust": cust})


def update_account(request):
    id = request.POST["id"]
    cust = Customer_Registration.objects.get(id=id)
    if cust.account == "Active":
        cust.deactivation_Date = datetime.now()
        fname = cust.fname
        email = cust.emailid
        message = "Hello " + fname + ", Your Account is temporarly deactivate by the Admin , Please Contact Admin."
        email_subject = "Your Account Is Suspended"
        email = EmailMessage(email_subject, message, EMAIL_HOST_USER, [email])
        email.content_subtype = 'html'
        email.send()
        cust.account = "Deactive"
    elif cust.account == "Deactive":
        cust.activation_Date = datetime.now()
        fname = cust.fname
        email = cust.emailid
        qr_code = cust.qr_code
        qr_image = MIMEImage(qr_code.read())
        print(qr_image)
        message = "Thanks for the Registration " + fname + ", Please find your QR Code for the Quick Toll Pass. Please do the Print and Use that."
        print(qr_code)
        print(cust.fname)
        email_subject = "Account Activate Now"
        email = EmailMessage(email_subject, message, EMAIL_HOST_USER, [email])
        email.attach(qr_image)
        email.content_subtype = 'html'
        email.send()
        cust.account = "Active"
    cust.save()
    return redirect('adminAll')


def allCustomersAdmin(request):
    return render(request, "allCustomersAdmin.html")


def admingEmpAll(request):
    emp=Employee.objects.all()
    return render(request,"allEmployeesAdmin.html",{"emp":emp})


#####################################################################################################################
def empRegistration(request):
    return render(request, "empRegister.html")


def save_emp(request):
    e_fname = request.POST["e_fname"]
    e_lname = request.POST["e_lname"]
    e_contact = request.POST["e_contact"]
    e_email = request.POST["e_email"]
    e_gender = request.POST["e_gender"]
    e_bod = request.POST["e_bod"]
    e_bloodGroup = request.POST["e_bloodGroup"]
    e_City = request.POST["e_City"]
    e_State = request.POST["e_State"]
    e_Coutry = request.POST["e_Coutry"]
    e_password = request.POST["e_password"]
    emp = Employee(e_fname=e_fname, e_lname=e_lname, e_contact=e_contact, e_email=e_email, e_gender=e_gender,
                   e_bod=e_bod, e_bloodGroup=e_bloodGroup, e_City=e_City, e_State=e_State, e_Coutry=e_Coutry,
                   e_password=e_password)
    emp.save()
    employee = Employee.objects.latest('e_empCode')
    e_fname = employee.e_fname
    e_lname = employee.e_lname
    e_final = e_fname + " " + e_lname
    e_email = employee.e_email
    print(employee.e_empCode, " ", employee.e_password)
    message = "Welcome " + e_final + ", Please note down Your Employee Code-" + employee.e_empCode + " And Password-" + employee.e_password + " for the Login Purpose"
    email_subject = "Account Activate Now"
    email = EmailMessage(email_subject, message, EMAIL_HOST_USER, [e_email])
    email.send()
    return HttpResponse("Registration Done , Please Check the Database ")



