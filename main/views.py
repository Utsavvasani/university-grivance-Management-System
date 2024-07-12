from django.shortcuts import render,redirect
from django.shortcuts import redirect
from django.utils.datastructures import MultiValueDictKeyError
from main.models import *
from django.db.models import *
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from pathlib import Path,os
from django.http import *
from django.db.models import Q
import time
import os
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils.crypto import get_random_string
import csv
import random
from django.contrib import messages

def complain_form(request):
    Category=Manage_grievanceType.objects.all()
    if "Vice-President" in request.session:
        Data=request.session['Vice-President']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        above = Manage_designation.objects.filter(Q(designationName="Vice-Chancellor") | Q(designationName="Founder and Managing Trustee"))
        to = Manage_user.objects.filter(designation__in=above)
        return render(request,"complain_form.html",{"president":sessionData,"user":Users,"category":Category,'to':to})
    elif "Director" in request.session:
        Data=request.session['Director']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        above = Manage_designation.objects.filter(Q(designationName="Vice-Chancellor") | Q(designationName="Founder and Managing Trustee") | Q(designationName="Vice-President"))
        to = Manage_user.objects.filter(designation__in=above)
        return render(request,"complain_form.html",{"director":sessionData,"user":Users,"category":Category,'to':to})
    elif "Vice-Chancellor" in request.session:
        Data=request.session['Vice-Chancellor']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        above = Manage_designation.objects.filter(Q(designationName="Founder and Managing Trustee"))
        to = Manage_user.objects.filter(designation__in=above)
        return render(request,"complain_form.html",{"chancellor":sessionData,"user":Users,"category":Category,'to':to})
    elif "Head Of Department" in request.session:
        Data=request.session['Head Of Department']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        Collage=Users.Collage
        data2=Manage_designation.objects.filter(designationName="Director")
        above = Manage_designation.objects.filter(Q(designationName="Vice-Chancellor") | Q(designationName="Founder and Managing Trustee") | Q(designationName="Vice-President") )
        to = Manage_user.objects.filter(Q(designation__in=above)|(Q(designation__in=data2)&(Q(Collage=Collage))))
        return render(request,"complain_form.html",{"hod":sessionData,"user":Users,"category":Category,'to':to})
    elif "Teacher" in request.session:
        Data=request.session['Teacher']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        Collage=Users.Collage
        Department=Users.department
        data2=Manage_designation.objects.filter(designationName="Director")
        data3=Manage_designation.objects.filter(designationName="Head Of Department")
        above = Manage_designation.objects.filter(Q(designationName="Vice-Chancellor") | Q(designationName="Founder and Managing Trustee") | Q(designationName="Vice-President") )
        to = Manage_user.objects.filter(Q(designation__in=above)|(Q(designation__in=data2)&(Q(Collage=Collage)))|(Q(designation__in=data3)&(Q(department=Department))))
        
        return render(request,"complain_form.html",{"teacher":sessionData,"user":Users,"category":Category,'to':to})
    elif "Student" in request.session:
        Data=request.session['Student']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        Collage=Users.Collage
        Department=Users.department
        data2=Manage_designation.objects.filter(designationName="Director")
        data3=Manage_designation.objects.filter(Q(designationName="Head Of Department")|Q(designationName="Teacher"))
        above = Manage_designation.objects.filter(Q(designationName="Vice-Chancellor") | Q(designationName="Founder and Managing Trustee") | Q(designationName="Vice-President") )
        to = Manage_user.objects.filter(Q(designation__in=above)|(Q(designation__in=data2)&(Q(Collage=Collage)))|(Q(designation__in=data3)&(Q(department=Department))))
        
        return render(request,"complain_form.html",{"student":sessionData,"user":Users,"category":Category,'to':to})
    elif "Admin" in request.session:
        Data=request.session['Admin']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        Collage=Users.Collage
        Department=Users.department
        data2=Manage_designation.objects.filter(designationName="Director")
        data3=Manage_designation.objects.filter(designationName="Head Of Department")
        above = Manage_designation.objects.filter(Q(designationName="Vice-Chancellor") | Q(designationName="Founder and Managing Trustee") | Q(designationName="Vice-President") )
        to = Manage_user.objects.filter(Q(designation__in=above)|(Q(designation__in=data2)&(Q(Collage=Collage)))|(Q(designation__in=data3)&(Q(department=Department))))
        
        return render(request,"complain_form.html",{"admin":sessionData,"user":Users,"category":Category,'to':to})
    else:
        return HttpResponse("hi")
#@@@@@@@@@@@@@@@@@@@@@@@@COMPLAIN@@@@@@@@@@@@@@@
def rejectGrievance(request,id):
    if request.method=="POST":
        get_Grievance_details=Manage_complainData.objects.get(id=id)
        feedback=request.POST['feedback']
        
        if "Founder and Managing Trustee" in request.session:
            Data=request.session['Founder and Managing Trustee']
            sessionData=Manage_registration.objects.get(email=Data)

        elif  "Vice-Chancellor" in request.session:
            Data=request.session['Vice-Chancellor']
            sessionData=Manage_registration.objects.get(email=Data)

            return redirect(request.META.get('HTTP_REFERER'))
        elif "Vice-President" in request.session:
            Data=request.session['Vice-President']
            sessionData=Manage_registration.objects.get(email=Data)

        elif "Director" in request.session:
            Data=request.session['Director']
            sessionData=Manage_registration.objects.get(email=Data)

        elif "Head Of Department" in request.session:
            Data=request.session['Head Of Department']
            sessionData=Manage_registration.objects.get(email=Data)

        elif "Teacher" in request.session:
            Data=request.session['Teacher']
            sessionData=Manage_registration.objects.get(email=Data)

        elif "Admin" in request.session:
            Data=request.session['Admin']
            sessionData=Manage_registration.objects.get(email=Data)

            
        elif  "Superadmin" in request.session:
            Data=request.session['Superadmin']
            sessionData=Manage_registration.objects.get(email=Data)
        get_Grievance_details.nameOfSolver=sessionData
        get_Grievance_details.remark=feedback
        get_Grievance_details.status=1
        get_Grievance_details.save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))
    
def solveGrievance(request,id):
    if request.method=="POST":
        get_Grievance_details=Manage_complainData.objects.get(id=id)
        feedback=request.POST['feedback']
        
        if "Founder and Managing Trustee" in request.session:
            Data=request.session['Founder and Managing Trustee']
            sessionData=Manage_registration.objects.get(email=Data)

        elif  "Vice-Chancellor" in request.session:
            Data=request.session['Vice-Chancellor']
            sessionData=Manage_registration.objects.get(email=Data)

            return redirect(request.META.get('HTTP_REFERER'))
        elif "Vice-President" in request.session:
            Data=request.session['Vice-President']
            sessionData=Manage_registration.objects.get(email=Data)

        elif "Director" in request.session:
            Data=request.session['Director']
            sessionData=Manage_registration.objects.get(email=Data)

        elif "Head Of Department" in request.session:
            Data=request.session['Head Of Department']
            sessionData=Manage_registration.objects.get(email=Data)

        elif "Teacher" in request.session:
            Data=request.session['Teacher']
            sessionData=Manage_registration.objects.get(email=Data)

        elif "Admin" in request.session:
            Data=request.session['Admin']
            sessionData=Manage_registration.objects.get(email=Data)

            
        elif  "Superadmin" in request.session:
            Data=request.session['Superadmin']
            sessionData=Manage_registration.objects.get(email=Data)
        get_Grievance_details.nameOfSolver=sessionData
        get_Grievance_details.remark=feedback
        get_Grievance_details.status=2
        get_Grievance_details.save()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))
def passGrievance(request,id):
    grievance=Manage_complainData.objects.get(id=id) 
    TO_Whom=grievance.to
    Power=TO_Whom.designation.power
    if Power==3:
        Des=Manage_designation.objects.get(designationName="Founder and Managing Trustee")
        To=Manage_user.objects.get(designation=Des)
        grievance.to=To
        grievance.save()
        return redirect(request.META.get('HTTP_REFERER'))  
    elif Power==4:
        Des=Manage_designation.objects.get(designationName="Vice-Chancellor")
        To=Manage_user.objects.get(designation=Des)
        grievance.to=To
        grievance.save()
        return redirect(request.META.get('HTTP_REFERER'))  
    elif Power==5:
        Des=Manage_designation.objects.get(designationName="Vice-President")
        To=Manage_user.objects.get(designation=Des)
        grievance.to=To
        grievance.save()
        return redirect(request.META.get('HTTP_REFERER'))
    elif Power==8:
        Des=Manage_designation.objects.get(designationName="Head Of Department")
        To=Manage_user.objects.get(designation=Des)
        Send_By=grievance.nameOfComplainant.uniqueId
        Send_By=Manage_user.objects.get(uniqueId=Send_By)
        Department=Send_By.department.departmentname
        Dept=Manage_department.objects.get(departmentname=str(Department))
        SendTo=Manage_user.objects.get(Q(department=Dept) & Q(designation=Des))
        grievance.to=SendTo
        grievance.save()
    elif Power==7:
        Des=Manage_designation.objects.get(designationName="admin")
        To=Manage_user.objects.get(designation=Des)
        Send_By=grievance.nameOfComplainant.uniqueId
        Send_By=Manage_user.objects.get(uniqueId=Send_By)
        Collage=Send_By.Collage.collageName
        Collage=Manage_collage.objects.get(collageName=Collage)
        SendTo=Manage_user.objects.get(Q(Collage=Collage)& Q(designation=Des))
        grievance.to=SendTo
        grievance.save()
    elif Power==6:
        Des=Manage_designation.objects.get(designationName="Director")
        To=Manage_user.objects.get(designation=Des)
        Send_By=grievance.nameOfComplainant.uniqueId
        Send_By=Manage_user.objects.get(uniqueId=Send_By)
        Collage=Send_By.Collage.collageName
        Collage=Manage_collage.objects.get(collageName=Collage)
        SendTo=Manage_user.objects.get(Q(Collage=Collage)&Q(designation=Des))
        grievance.to=SendTo
        grievance.save()
    return redirect(request.META.get('HTTP_REFERER'))  
def for_solve_grievance(request):
    if "Founder and Managing Trustee" in request.session:
        Data=request.session['Founder and Managing Trustee']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        Grievance=Manage_complainData.objects.filter(to=Users)
        return render(request,"solve.html",{"trustee":sessionData,"user":Users,"reg":sessionData,"Grievance":Grievance})
    elif  "Vice-Chancellor" in request.session:
        Data=request.session['Vice-Chancellor']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        Grievance=Manage_complainData.objects.filter(to=Users)
        return render(request,"solve.html",{"chancellor":sessionData,"user":Users ,"reg":sessionData,"Grievance":Grievance})
    elif "Vice-President" in request.session:
        Data=request.session['Vice-President']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        Grievance=Manage_complainData.objects.filter(to=Users)
        return render(request,"solve.html",{"president":sessionData,"user":Users,"reg":sessionData,"Grievance":Grievance })
    elif "Director" in request.session:
        Data=request.session['Director']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        Grievance=Manage_complainData.objects.filter(to=Users)
        return render(request,"solve.html",{"director":sessionData,"user":Users ,"reg":sessionData,"Grievance":Grievance})
    elif "Head Of Department" in request.session:
        Data=request.session['Head Of Department']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        Grievance=Manage_complainData.objects.filter(to=Users)
        return render(request,"solve.html",{"hod":sessionData,"user":Users,"reg":sessionData,"Grievance":Grievance })
    elif "Teacher" in request.session:
        Data=request.session['Teacher']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        Grievance=Manage_complainData.objects.filter(to=Users)
        return render(request,"solve.html",{"teacher":sessionData,"user":Users ,"reg":sessionData,"Grievance":Grievance})
    elif "Admin" in request.session:
        Data=request.session['Admin']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        Grievance=Manage_complainData.objects.filter(to=Users)
        return render(request,"solve.html",{"admin":sessionData,"user":Users,"reg":sessionData,"Grievance":Grievance })
    elif  "Superadmin" in request.session:
        Data=request.session['Superadmin']
        sessionData=Manage_registration.objects.get(email=Data)
        Grievance=Manage_complainData.objects.filter(to=None)
        return render(request,"solve.html",{"superadmin":sessionData,"reg":sessionData,"Grievance":Grievance})
    
    else:
        return redirect("manageLogin")

def generate_complain_id():
    while True:
        # Generate a 6-digit random number
        id_string = "LJKU_COMPLAIN_"+get_random_string(length=6, allowed_chars='0qwertyABjxcvCD12EpasdfFG34HioghbIJklzKL56MNOPQ78UV9RSTWXunYZm')
        # Check if a model instance with this id exists
        if not Manage_complainData.objects.filter(complainCode=id_string).exists():
            return id_string
        
def show_your_grievance(request):
    if "Founder and Managing Trustee" in request.session:
        Data=request.session['Founder and Managing Trustee']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        Grievance=Manage_complainData.objects.filter(nameOfComplainant=sessionData)
        return render(request,"show_your_grievance.html",{"trustee":sessionData,"user":Users,"reg":sessionData,"Grievance":Grievance})
    elif  "Vice-Chancellor" in request.session:
        Data=request.session['Vice-Chancellor']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        Grievance=Manage_complainData.objects.filter(nameOfComplainant=sessionData)
        
        return render(request,"show_your_grievance.html",{"chancellor":sessionData,"user":Users ,"reg":sessionData,"Grievance":Grievance})
    elif "Vice-President" in request.session:
        Data=request.session['Vice-President']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        Grievance=Manage_complainData.objects.filter(nameOfComplainant=sessionData)
        
        return render(request,"show_your_grievance.html",{"president":sessionData,"user":Users,"reg":sessionData,"Grievance":Grievance })
    elif "Director" in request.session:
        Data=request.session['Director']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        Grievance=Manage_complainData.objects.filter(nameOfComplainant=sessionData)
        
        return render(request,"show_your_grievance.html",{"director":sessionData,"user":Users ,"reg":sessionData,"Grievance":Grievance})
    elif "Head Of Department" in request.session:
        Data=request.session['Head Of Department']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        Grievance=Manage_complainData.objects.filter(nameOfComplainant=sessionData)
        
        return render(request,"show_your_grievance.html",{"hod":sessionData,"user":Users,"reg":sessionData,"Grievance":Grievance })
    elif "Teacher" in request.session:
        Data=request.session['Teacher']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        Grievance=Manage_complainData.objects.filter(nameOfComplainant=sessionData)
        
        return render(request,"show_your_grievance.html",{"teacher":sessionData,"user":Users ,"reg":sessionData,"Grievance":Grievance})
    elif "Student" in request.session:
        Data=request.session['Student']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        Grievance=Manage_complainData.objects.filter(nameOfComplainant=sessionData)
        #Teacher=user.objects.filter(department.departmentname==Users.department.departmentname)
        return render(request,"show_your_grievance.html",{"student":sessionData,"user":Users ,"reg":sessionData,"Grievance":Grievance})
    elif "Admin" in request.session:
        Data=request.session['Admin']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        Grievance=Manage_complainData.objects.filter(nameOfComplainant=sessionData)
        return render(request,"show_your_grievance.html",{"admin":sessionData,"user":Users,"reg":sessionData,"Grievance":Grievance })
    elif  "Superadmin" in request.session:
        Data=request.session['Superadmin']
        sessionData=Manage_registration.objects.get(email=Data)
        Grievance=Manage_complainData.objects.filter(nameOfComplainant=sessionData)   
        return render(request,"show_your_grievance.html",{"superadmin":sessionData,"reg":sessionData,"Grievance":Grievance})
    
    else:
        return redirect("manageLogin")


def addComplain(request):
    Category=request.POST["category"]
    Description=request.POST["Description"]
    Email=request.POST["email"]
    to=request.POST["to"] 
    to=Manage_user.objects.get(id=to)
    Users=Manage_registration.objects.get(uniqueId=Email)
    Category=Manage_grievanceType.objects.get(typeName=Category)
    ComplainCode=generate_complain_id()
    try:
        image=request.FILES['image']
        Manage_complainData(image=image,complainCode=ComplainCode,description=Description,status=0,category=Category,nameOfComplainant=Users,solvingDate=None,to=to).save()
        topic='Mender Company'
        data='<p style="font-style: oblique;">Hi, <b>' +Users.username +'</b>Your complaint is submitted successfully.<br>Ypour Complain Code is <b>'+ComplainCode+'</b> <br>we assure you that we will solve your complain as soon as possible</p>'
        from_email='mender.company@gmail.com'
        to_email=Users.email
        msg=EmailMultiAlternatives(topic,data,from_email,[to_email])
        msg.content_subtype='html'
        msg.send()
    except MultiValueDictKeyError:
        pass
    finally:
        Manage_complainData(complainCode=ComplainCode,description=Description,status=0,category=Category,nameOfComplainant=Users,solvingDate=None,to=to).save()
        topic='Mender Company'
        data='<p style="font-style: oblique;">Hi, <b>' +Users.username +'</b>Your complaint is submitted successfully.<br>Ypour Complain Code is <b>'+ComplainCode+'</b> <br>we assure you that we will solve your complain as soon as possible</p>'
        from_email='mender.company@gmail.com'
        to_email=Users.email
        msg=EmailMultiAlternatives(topic,data,from_email,[to_email])
        msg.content_subtype='html'
        msg.send()
    return redirect(request.META.get('HTTP_REFERER')) 

def feedback(request,id):
    if request.method=="POST":
        Feedback=request.POST['feedback']
        data=Manage_complainData.objects.get(complainCode=id)
        data.feedback=Feedback
        data.save()
        return redirect(request.META.get('HTTP_REFERER'))   

#@@@@@@@@@@@@@@@@@@@@@@@@USERCRUD@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def deleteUser(request, id):
  Users = Manage_user.objects.get(id=id)
  Reg=Manage_registration.objects.get(email=Users.email)
  Users.delete()
  Reg.delete()
  return redirect(request.META.get('HTTP_REFERER'))


def updateUser(request, id):
    UserName=request.POST['userName']     
    SurName=request.POST['surName']
    FatherName=request.POST['fatherName']
    PhoneNumber=request.POST['phoneNumber']
    Address=request.POST['address']
    Email=request.POST['email']
    User = Manage_user.objects.get(id=id)
    Designation=User.designation.designationName
    DesignationId=Manage_designation.objects.get(designationName=Designation)
    if User.designation.designationName=="Founder and Managing Trustee":
        DesigData=DesignationId
        User.designation=DesigData
        User.userName=UserName
        User.surName=SurName
        User.fatherName=FatherName
        User.phoneNumber=PhoneNumber
        User.address=Address
        User.email=Email
        try:
            
            image=request.FILES['image']

            User.image=image
            
        except MultiValueDictKeyError:
            pass
        finally:
            User.save()
            return redirect(request.META.get('HTTP_REFERER'))
    elif User.designation.designationName=="Vice-Chancellor":
        DesigData=DesignationId
        User.designation=DesigData
        User.userName=UserName
        User.surName=SurName
        User.fatherName=FatherName
        User.phoneNumber=PhoneNumber
        User.address=Address
        User.email=Email
        try:
            image=request.FILES['image']
            Manage_user.image=image
        except MultiValueDictKeyError:
            pass
        finally:
            User.save()
            return redirect(request.META.get('HTTP_REFERER'))
       
    elif User.designation.designationName=="Vice-President":

        DesigData=DesignationId
        User.designation=DesigData
        User.userName=UserName
        User.surName=SurName
        User.fatherName=FatherName
        User.phoneNumber=PhoneNumber
        User.address=Address
        User.email=Email
        try:
            image=request.FILES['image']
            Manage_user.image=image
        except MultiValueDictKeyError:
            pass
        finally:
            User.save()
            return redirect(request.META.get('HTTP_REFERER'))
    elif User.designation.designationName=="Director":
        Collage=request.POST['collage']
        Collage=Manage_collage.objects.get(collageName=Collage)
        DesigData=DesignationId
        User.designation=DesigData
        User.userName=UserName
        User.surName=SurName
        User.fatherName=FatherName
        User.Collage=Collage
        User.phoneNumber=PhoneNumber
        User.address=Address
        User.email=Email
        try:
            image=request.FILES['image']
            User.image=image
        except MultiValueDictKeyError:
            pass
        finally:
            User.save()
            return redirect(request.META.get('HTTP_REFERER'))
    elif User.designation.designationName=="Head Of Department": 
        Department=request.POST['department']
        DepartmentId=Manage_department.objects.get(departmentname=Department)
        Collage=DepartmentId.collageId
        DeptData=DepartmentId
        DesigData=DesignationId
        User.department=DeptData
        User.designation=DesigData
        User.userName=UserName
        User.surName=SurName
        User.fatherName=FatherName
        User.Collage=Collage
        User.phoneNumber=PhoneNumber
        User.address=Address
        User.email=Email
        try:
            image=request.FILES['image']
            Manage_user.image=image
        except MultiValueDictKeyError:
            pass
        finally:
            User.save()
            return redirect(request.META.get('HTTP_REFERER'))   
    elif User.designation.designationName=="Teacher":
        Department=request.POST['department']
        DepartmentId=Manage_department.objects.get(departmentname=Department)
        Collage=DepartmentId.collageId
        DeptData=DepartmentId
        DesigData=DesignationId
        User.department=DeptData
        User.designation=DesigData
        User.userName=UserName
        User.surName=SurName
        User.fatherName=FatherName
        User.phoneNumber=PhoneNumber
        User.address=Address
        User.Collage=Collage
        User.email=Email
        try:
            image=request.FILES['image']
            User.image=image
        except MultiValueDictKeyError:
            pass
        finally:
            User.save()
            return redirect(request.META.get('HTTP_REFERER'))
    elif User.designation.designationName=="Student":
        Department=request.POST['department']
        Semester=request.POST['semester']
        DepartmentId=Manage_department.objects.get(departmentname=Department)
        CollageId=Manage_collage.objects.get(collageName=DepartmentId.collageId.collageName)
        DeptData=DepartmentId
        DesigData=DesignationId
        User.department=DeptData
        User.Collage=CollageId
        User.designation=DesigData
        User.userName=UserName
        User.surName=SurName
        User.fatherName=FatherName
        User.semester=Semester
        User.phoneNumber=PhoneNumber
        User.address=Address
        User.email=Email
        try:
            image=request.FILES['image']
            User.image=image
        except MultiValueDictKeyError:
            pass
        finally:
            User.save()
            return redirect(request.META.get('HTTP_REFERER'))
    elif User.designation.designationName=="Admin":
        Semester=request.POST['semester']
        Collage=request.POST['Collage']
        Collage=Manage_collage.objects.get(collageName=Collage)
        DesigData=DesignationId
        User.designation=DesigData
        User.userName=UserName
        User.surName=SurName
        User.fatherName=FatherName
        User.phoneNumber=PhoneNumber
        User.address=Address
        User.email=Email
        User.Collage=Collage
        try:
            image=request.FILES['image']
            User.image=image
        except MultiValueDictKeyError:
            pass
        finally:
            User.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))   
 
def manageUsers(request):
        if 'Superadmin' in request.session:
            Data=request.session['Superadmin']
            sessionData=Manage_registration.objects.get(email=Data)
            all=Manage_user.objects.all()
            Designation=Manage_designation.objects.all()
            Department=Manage_department.objects.all()
            Collage=Manage_collage.objects.all()
            return render(request,"users.html",{"Users":all,"Designation":Designation,"Department":Department,"Collage":Collage,"superadmin":sessionData})
        else:
            return redirect("manageLogin")
def generate_unique_id():
    while True:
        # Generate a 6-digit random number
        id_string = get_random_string(length=17, allowed_chars='0qwertyABjxcvCD12EpasdfFG34HioghbIJklzKL56MNOPQ78UV9RSTWXunYZm')
        # Check if a model instance with this id exists
        if not Manage_user.objects.filter(uniqueId=id_string).exists():
            return id_string
def addUser(request):
    if request.method=="POST":
        Email=request.POST['email']
        Surname=request.POST['surName']
        Fathername=request.POST['fatherName']
        Name=request.POST['userName']
        ContactNo=request.POST['phoneNumber']
        Address=request.POST['address']
        Image=request.FILES['file']
        unique=generate_unique_id()
        if 'Admin' in request.POST:
            Collage=request.POST['Collage']
            Data=Manage_collage.objects.get(collageName=Collage)
            Desig=Manage_designation.objects.get(designationName='Admin')
            Manage_user(uniqueId=unique,image=Image,userName=Name,surName=Surname,fatherName=Fathername,phoneNumber=ContactNo,email=Email,address=Address,Collage=Data,designation=Desig).save()
            Manage_registration(uniqueId=unique,email=Email,username=Name,password='password@123',typeId=Desig).save()
            return redirect(request.META.get('HTTP_REFERER'))
        if 'Founder and Managing Trustee' in request.POST:
            Desig=Manage_designation.objects.get(designationName='Founder and Managing Trustee')
            Manage_user(uniqueId=unique,image=Image,userName=Name,surName=Surname,fatherName=Fathername,phoneNumber=ContactNo,email=Email,address=Address,designation=Desig).save()
            Manage_registration(uniqueId=unique,email=Email,username=Name,password='password@123',typeId=Desig).save()
            return redirect(request.META.get('HTTP_REFERER'))
        if 'Vice-Chancellor' in request.POST:
            Desig=Manage_designation.objects.get(designationName='Vice-Chancellor')
            Manage_user(uniqueId=unique,image=Image,userName=Name,surName=Surname,fatherName=Fathername,phoneNumber=ContactNo,email=Email,address=Address,designation=Desig).save()
            Manage_registration(uniqueId=unique,email=Email,username=Name,password='password@123',typeId=Desig).save()
            return redirect(request.META.get('HTTP_REFERER'))
        if 'Vice-President' in request.POST:
            Desig=Manage_designation.objects.get(designationName='Vice-President')
            Manage_user(uniqueId=unique,image=Image,userName=Name,surName=Surname,fatherName=Fathername,phoneNumber=ContactNo,email=Email,address=Address,designation=Desig).save()
            Manage_registration(uniqueId=unique,email=Email,username=Name,password='password@123',typeId=Desig).save()
            return redirect(request.META.get('HTTP_REFERER'))
        if 'Director' in request.POST:
            Collage=request.POST['Collage']
            Data=Manage_collage.objects.get(collageName=Collage)
            Desig=Manage_designation.objects.get(designationName='Director')
            Manage_user(uniqueId=unique,image=Image,userName=Name,surName=Surname,fatherName=Fathername,phoneNumber=ContactNo,email=Email,address=Address,Collage=Data,designation=Desig).save()
            Manage_registration(uniqueId=unique,email=Email,username=Name,password='password@123',typeId=Desig).save()
            return redirect(request.META.get('HTTP_REFERER'))
        if 'Head Of Department' in request.POST:
            Dept=request.POST['Department']
            Data=Manage_department.objects.get(departmentname=Dept)
            Collage=Data.collageId.collageName
            Collage=Manage_collage.objects.get(collageName=Collage)
            Desig=Manage_designation.objects.get(designationName='Head Of Department')
            Manage_user(uniqueId=unique,image=Image,userName=Name,surName=Surname,fatherName=Fathername,phoneNumber=ContactNo,email=Email,address=Address,Collage=Collage,department=Data,designation=Desig).save()
            Manage_registration(uniqueId=unique,email=Email,username=Name,password='password@123',typeId=Desig).save()
           
            return redirect(request.META.get('HTTP_REFERER'))
        if 'Teacher' in request.POST:
            Dept=request.POST['Department']
            Data=Manage_department.objects.get(departmentname=Dept)
            Collage=Data.collageId.collageName
            Collage=Manage_collage.objects.get(collageName=Collage)
            Desig=Manage_designation.objects.get(designationName='Teacher')
            Manage_user(uniqueId=unique,image=Image,userName=Name,surName=Surname,fatherName=Fathername,phoneNumber=ContactNo,email=Email,address=Address,Collage=Collage,department=Data,designation=Desig).save()
            Manage_registration(uniqueId=unique,email=Email,username=Name,password='password@123',typeId=Desig).save()
           
            return redirect(request.META.get('HTTP_REFERER'))
        if 'Student' in request.POST:
            Dept=request.POST['Department']
            Sem=request.POST['semester']
            Data=Manage_department.objects.get(departmentname=Dept)
            Collage=Data.collageId.collageName
            Collage=Manage_collage.objects.get(collageName=Collage)
            Desig=Manage_designation.objects.get(designationName='Student')
            Manage_user(uniqueId=unique,semester=Sem,image=Image,userName=Name,surName=Surname,fatherName=Fathername,phoneNumber=ContactNo,email=Email,address=Address,Collage=Collage,department=Data,designation=Desig).save()
            Manage_registration(uniqueId=unique,email=Email,username=Name,password='password@123',typeId=Desig).save()
        details=Manage_user.objects.get(uniqueId=unique)
        topic='Mender Company'
        data='<p style="font-style: oblique;">Hi, <b>' +details.userName +'</b>Your registration code is <b>'+unique+'</b>.<br>Your password  is <b>password@123</b> <br>.Thank You.</p>'
        from_email='mender.company@gmail.com'
        to_email=Email
        msg=EmailMultiAlternatives(topic,data,from_email,[to_email])
        msg.content_subtype='html'
        msg.send()
        return redirect(request.META.get('HTTP_REFERER'))
            
#@@@@@@@@@@@@@@@@@@@@@@@@GRIEVANCETYPECRUD@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def manageGrievanceType(request):
    if 'Superadmin' in request.session:
        Data=request.session['Superadmin']
        sessionData=Manage_registration.objects.get(email=Data)
        Type=Manage_grievanceType.objects.all()
        return render(request,"grievance_Type.html",{'superadmin':sessionData,'Type':Type})
    else:
        return redirect("manageLogin")
#manage category
def addCategory(request):
    if request.method == 'POST':
        CategoryName=request.POST['CategoryName']
        Manage_grievanceType(typeName=CategoryName).save()
        return redirect(request.META.get('HTTP_REFERER'))
def deleteCategory(request, id):
  GrievanceType = Manage_grievanceType.objects.get(id=id)
  GrievanceType.delete()
  return redirect(request.META.get('HTTP_REFERER'))
def updateCategory(request, id):
    CategoryName=request.POST['CategoryName']
    data = Manage_grievanceType.objects.get(id=id)
    data.typeName=CategoryName
    data.save()
    return redirect(request.META.get('HTTP_REFERER'))
#@@@@@@@@@@@@@@@@@@@@@@@@DESIGNATIONCRUD@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def manageDesignation(request):
    if 'Superadmin' in request.session:
        Data=request.session['Superadmin']
        sessionData=Manage_registration.objects.get(email=Data)
        
        Designation=Manage_designation.objects.all()
        Count=Manage_designation.objects.aggregate(Sum('power'))
        data=Count['power__sum']
        base=100/data
        return render(request,"designation.html",{'superadmin':sessionData,'designation':Designation,'data':base})
    else:
        return redirect("manageLogin")
#manage designation
def addDesignation(request):
    if request.method == 'POST':
        DesignationName=request.POST['DesignationName']
        Power=request.POST['Power']
        Manage_designation(designationName=DesignationName,power=Power).save()
        return redirect(request.META.get('HTTP_REFERER'))
def deleteDesignation(request, id):
  Designation = Manage_designation.objects.get(id=id)
  Designation.delete()
  return redirect(request.META.get('HTTP_REFERER'))
def updateDesignation(request, id):
    ddesignationName=request.POST['DesignationName']
    Ppower=request.POST['Power']
    if request.method=='POST':
        Designation = Manage_designation.objects.get(id=id)
        Designation.designationName=ddesignationName
        Designation.power=Ppower
        Designation.save()
        return redirect(request.META.get('HTTP_REFERER'))


#@@@@@@@@@@@@@@@@@@@@@@@@DEPARTMENTCRUD@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def manageDepartment(request):
    if 'Superadmin' in request.session:
        Department=Manage_department.objects.all()
        Collage=Manage_collage.objects.all()
        Data=request.session['Superadmin']
        sessionData=Manage_registration.objects.get(email=Data)
        return render(request,"department.html",{'superadmin':sessionData,'department':Department,'Collage':Collage})
    else:
        return redirect("manageLogin")
#manage department
def addDepartment(request):
    if request.method == 'POST':
        DepartmentName=request.POST['departmentName']
        Semester=request.POST['semester']
        CollageId=request.POST['collage']
        Id=Manage_collage.objects.get(collageName=CollageId)
        data=Id
        Manage_department(collageId=data,departmentname=DepartmentName,semester=Semester).save()
        return redirect(request.META.get('HTTP_REFERER'))
def deleteDepartment(request, id):
  Department = Manage_department.objects.get(id=id)
  Department.delete()
  return redirect(request.META.get('HTTP_REFERER'))
def updateDepartment(request, id):
    Dept=request.POST['Dept']
    Semester=request.POST['Semester']
    Collage=request.POST['Collage']
    Department = Manage_department.objects.get(id=id)
    Department.departmentname=Dept
    Department.semester=Semester
    Id=Manage_collage.objects.get(collageName=Collage)
    Department.collageId=Id
    Department.save()    
    return redirect(request.META.get('HTTP_REFERER'))

#@@@@@@@@@@@@@@@@@@@@@@@@COLLAGECRUD@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def manageCollage(request):
    if 'Superadmin' in request.session:
        Collage=Manage_collage.objects.all()
        Data=request.session['Superadmin']
        sessionData=Manage_registration.objects.get(email=Data)   
        return render(request,"collage.html",{'superadmin':sessionData,'collage':Collage})
    else:
        return redirect("manageLogin")
def addCollage(request):
    if request.method == 'POST':
        Name=request.POST['collageName']
        Address=request.POST['collageAddress']
        Description=request.POST['collageDescription']
        Image=request.FILES['collageImage']
        Manage_collage(collageName=Name,collageAddress=Address,collageDescription=Description,collageImage=Image).save()
        return redirect(request.META.get('HTTP_REFERER'))
def deleteCollage(request, id):
  Collage = Manage_collage.objects.get(id=id)
  data=Collage.collageImage.url
  string= Path(os.getcwd().replace("\\superadmin", ""))
  beta=Path(data)
  if os.path.exists(f'{string}{beta}'):
    os.remove(f'{string}{data}')
    Collage.delete()
  return redirect(request.META.get('HTTP_REFERER'))
    
def updateCollage(request, id):
    Name=request.POST['collageName']
    Address=request.POST['collageAddress']
    Description=request.POST['collageDescription']
    Collage = Manage_collage.objects.get(id=id)
    Collage.collageName=Name
    Collage.collageAddress=Address
    Collage.collageDescription=Description
    try:
        image=request.FILES['image']
        Collage.collageImage=image
    except MultiValueDictKeyError:
        pass
    finally:
        Collage.save()
    return redirect(request.META.get('HTTP_REFERER'))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@LOGIN@@@@@@@@@@@@@@@@@@@@@@@@@@
def manageLogin(request):
    if "Superadmin"or"Founder and Managing Trustee"or"Vice-Chancellor"or"Vice-President"or"Director"or"Head Of Department"or"Teacher"or"Student"or"Admin" not in request.session:
        if request.method=="POST":
            
            Enrollment=request.POST['enrollment']
            Password=request.POST['password']
            try:
                check=Manage_registration.objects.get(uniqueId=Enrollment,password=Password)
                
                if check.uniqueId==Enrollment and check.password==Password:
                    if check.typeId.designationName=="Founder and Managing Trustee":
                            request.session["Founder and Managing Trustee"]=check.email
                            return redirect('index')
                    elif check.typeId.designationName=="Vice-Chancellor":
                        request.session["Vice-Chancellor"]=check.email
                        return redirect('index')
                    elif check.typeId.designationName=="Vice-President":
                        request.session["Vice-President"]=check.email
                        return redirect('index')
                    elif check.typeId.designationName=="Director":
                        request.session["Director"]=check.email
                        return redirect('index')
                    elif check.typeId.designationName=="Head Of Department":
                        request.session["Head Of Department"]=check.email
                        return redirect('index')
                    elif check.typeId.designationName=="Teacher":
                        request.session["Teacher"]=check.email
                        return redirect('index')
                    elif check.typeId.designationName=="Student":
                        request.session["Student"]=check.email
                        return redirect('index')
                    elif check.typeId.designationName=="Admin":
                        request.session["Admin"]=check.email
                        return redirect('index')
                    elif check.typeId.designationName=="Superadmin":
                        request.session["Superadmin"]=check.email
                        return redirect('index')
                    else:
                        return redirect("manageLogin")
            except:
                return redirect("manageLogin")
        else:
            return render(request,"login.html")
    else:
        return redirect("index")
def manageLogout(request):
    if "Superadmin" in request.session:
        del request.session['Superadmin']
    elif "Founder and Managing Trustee"  in request.session:
        del request.session['Founder and Managing Trustee']
    elif "Vice-Chancellor" in request.session:
        del request.session['Vice-Chancellor']
    elif "Vice-President" in request.session:
        del request.session['Vice-President']
    elif "Director" in request.session:
        del request.session['Director']
    elif "Head Of Department" in request.session:
        del request.session['Head Of Department']
    elif "Teacher" in request.session:
        del request.session['Teacher']
    elif "Student" in request.session:
        del request.session['Student']
    elif "Admin" in request.session:
        del request.session['Admin']
    return redirect("manageLogin")

def index(request):
    Complain=Manage_complainData.objects.all()
    find=Manage_registration.objects.filter().first()
    if find is None:
        Manage_designation(designationName="Superadmin",power="1").save()
        data=Manage_designation.objects.get(designationName="Superadmin")
        Manage_registration(uniqueId="2020004500210000",email="superadmin@gmail.com",username="superadmin",password="password@123",typeId=data).save()
        return redirect("manageLogin")
    else:
        Count=Manage_user.objects.all().count()
        Pending=Manage_complainData.objects.filter(status=0).count()
        Solved=Manage_complainData.objects.filter(status=2).count()
        Rejected=Manage_complainData.objects.filter(status=1).count()
        if "Superadmin" in request.session:
            Data=request.session['Superadmin']
            sessionData=Manage_registration.objects.get(email=Data)
            return render(request,"index.html",{"superadmin":sessionData,"Count":Count,"Pending":Pending,"solved":Solved,"Rejected":Rejected,'Complain':Complain})
        elif "Founder and Managing Trustee" in request.session:
            Data=request.session['Founder and Managing Trustee']
            sessionData=Manage_registration.objects.get(email=Data)
            Users=Manage_user.objects.get(email=Data)
            return render(request,"index.html",{"trustee":sessionData,"user":Users,"Count":Count,"Pending":Pending,"solved":Solved,"Rejected":Rejected,'Complain':Complain})
        elif  "Vice-Chancellor" in request.session:
            Data=request.session['Vice-Chancellor']
            sessionData=Manage_registration.objects.get(email=Data)
            Users=Manage_user.objects.get(email=Data)
            return render(request,"index.html",{"chancellor":sessionData,"user":Users,"Count":Count,"Pending":Pending,"solved":Solved,"Rejected":Rejected,'Complain':Complain})
        elif "Vice-President" in request.session:
            Data=request.session['Vice-President']
            sessionData=Manage_registration.objects.get(email=Data)
            Users=Manage_user.objects.get(email=Data)
            return render(request,"index.html",{"president":sessionData,"user":Users,"Count":Count,"Pending":Pending,"solved":Solved,"Rejected":Rejected,'Complain':Complain})
        elif "Director" in request.session:
            Data=request.session['Director']
            sessionData=Manage_registration.objects.get(email=Data)
            Users=Manage_user.objects.get(email=Data)
            return render(request,"index.html",{"director":sessionData,"user":Users,"Count":Count,"Pending":Pending,"solved":Solved,"Rejected":Rejected,'Complain':Complain})
        elif "Head Of Department" in request.session:
            Data=request.session['Head Of Department']
            sessionData=Manage_registration.objects.get(email=Data)
            Users=Manage_user.objects.get(email=Data)
            return render(request,"index.html",{"hod":sessionData,"user":Users,"Count":Count,"Pending":Pending,"solved":Solved,"Rejected":Rejected,'Complain':Complain})
        elif "Teacher" in request.session:
            Data=request.session['Teacher']
            sessionData=Manage_registration.objects.get(email=Data)
            Users=Manage_user.objects.get(email=Data)
            return render(request,"index.html",{"teacher":sessionData,"user":Users,"Count":Count,"Pending":Pending,"solved":Solved,"Rejected":Rejected,'Complain':Complain})
        elif "Student" in request.session:
            Data=request.session['Student']
            sessionData=Manage_registration.objects.get(email=Data)
            Users=Manage_user.objects.get(email=Data)
            #Teacher=user.objects.filter(department.departmentname==Users.department.departmentname)
            return render(request,"index.html",{"student":sessionData,"user":Users,"Count":Count,"Pending":Pending,"solved":Solved,"Rejected":Rejected,'Complain':Complain})
        elif "Admin" in request.session:
            Data=request.session['Admin']
            sessionData=Manage_registration.objects.get(email=Data)
            Users=Manage_user.objects.get(email=Data)
            return render(request,"index.html",{"admin":sessionData,"user":Users,"Count":Count,"Pending":Pending,"solved":Solved,"Rejected":Rejected,'Complain':Complain})
        else:
            return redirect("manageLogin")

def reset_password(request):
    if request.method=="POST":
        email=request.session['Email']
        confirm=request.POST['confirm']
        reset=request.POST['reset']
        if confirm==reset:
            user = Manage_registration.objects.get(email=email)
            user.password=confirm
            user.save()
            return redirect('manageLogin')
        else:
            messages.error(request, 'ENTER BOTH SAME')
            return render(request,"reset_password.html") 
    else:
        return render(request,"reset_password.html")
def forgot_password(request):
    return render(request,"forgot_password.html")
def verify(request):
        if request.method == 'POST':
            OTP = request.session.get('OTP')
            email = request.session.get('Email')
            otp = request.POST['otp']
            user = Manage_registration.objects.get(email=email)
            if str(OTP) == otp:
                # OTP verified successfully, redirect to the reset password page
                
                return redirect('reset_password')
            else:
                messages.error(request, 'Invalid OTP.')
                return redirect('forgot_password')
        return render(request,"verify.html")
#@@@@@@@@@@@@@@@@@@@@@@@@@CHANGEPASSWORD@@@@@@@@@@@@@@@@@@@@@@@
def function_forgot(request):
    if request.method=="POST":
        Email=request.POST['email']
        try:
            data=Manage_registration.objects.get(email=Email)
            OTP= random.randint(100000, 999999)
            request.session['OTP'] = OTP
            request.session['Email'] = data.email
            topic='Mender Company'
            data='<p style="font-style: oblique;">OTP is <b>'+str(OTP)+'</b></p>'
            from_email='mender.company@gmail.com'
            to_email=Email
            msg=EmailMultiAlternatives(topic,data,from_email,[to_email])
            msg.content_subtype='html'
            msg.send()
            return redirect("verify")
        except:
            return redirect("forgot_password")
#@@@@@@@@@@@@@@@@@@@@@@@@FORGOT PASSWORD@@@@@@@@@@@@@@@@@@@@@@@
def Function_Change(request):
    if request.method=="POST":
        old=request.POST['old']
        New=request.POST['new']
        unique=request.POST['unique']
        data=Manage_registration.objects.filter(uniqueId=unique)
        if data is not None:
            data=Manage_registration.objects.get(uniqueId=unique)
            if old==data.password:
                data.password=New
                data.save()
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                return redirect('Change_Password')
        else:
                return redirect('Change_Password')
                
def Change_Password(request):
    if "Superadmin" in request.session:
        Data=request.session['Founder and Managing Trustee']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        return render(request,"Change_password.html",{"superadmin":sessionData,"user":Users,"reg":sessionData})
    if "Founder and Managing Trustee" in request.session:
        Data=request.session['Founder and Managing Trustee']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        return render(request,"Change_password.html",{"trustee":sessionData,"user":Users,"reg":sessionData})
    elif  "Vice-Chancellor" in request.session:
        Data=request.session['Vice-Chancellor']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        return render(request,"Change_password.html",{"chancellor":sessionData,"user":Users ,"reg":sessionData})
    elif "Vice-President" in request.session:
        Data=request.session['Vice-President']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        return render(request,"Change_password.html",{"president":sessionData,"user":Users,"reg":sessionData })
    elif "Director" in request.session:
        Data=request.session['Director']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        return render(request,"Change_password.html",{"director":sessionData,"user":Users ,"reg":sessionData})
    elif "Head Of Department" in request.session:
        Data=request.session['Head Of Department']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        return render(request,"Change_password.html",{"hod":sessionData,"user":Users,"reg":sessionData })
    elif "Teacher" in request.session:
        Data=request.session['Teacher']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        return render(request,"Change_password.html",{"teacher":sessionData,"user":Users ,"reg":sessionData})
    elif "Student" in request.session:
        Data=request.session['Student']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        #Teacher=user.objects.filter(department.departmentname==Users.department.departmentname)
        return render(request,"Change_password.html",{"student":sessionData,"user":Users ,"reg":sessionData})
    elif "Admin" in request.session:
        Data=request.session['Admin']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        return render(request,"Change_password.html",{"admin":sessionData,"user":Users,"reg":sessionData })
    else:
        return redirect("manageLogin")
#@@@@@@@@@@@@@@@@@@@@@@@@@REPORT@@@@@@@@@@@@@@@@@@@@@@@
def reg_report(request):
    data=Manage_user.objects.all()
    return render(request,'registration_report.html',{"data":data})
def render_pdf_view(request):
    data=Manage_user.objects.all()
    template_path = 'registration_report.html'
    context = {"data":data}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
#@@@@@@@@@@BULKUPLOAD@@@@@@@@@@@
def downloadCsvMenu(request):
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=student_details.csv'
    writer = csv.writer(response)
    writer.writerow(['uniqueId','name','surname','fathername','email','phonenumber','address','collageName','department','semester','designation'])
    meta=Manage_user.objects.all()
    for data in meta:
        if data.designation.designationName=="Student":  
            writer.writerow([data.uniqueId,data.userName,data.surName,data.fatherName,data.email,data.phoneNumber,data.address,data.Collage.collageName,data.department.departmentname,data.semester,data.designation.designationName])
           
        else:
            pass
    return response
def UploadCsvMenu(request):
    if("GET" == request.method):
        return HttpResponse("Not valid method")
    csv_file=request.FILES["file"]
    if not csv_file.name.endswith('.csv'):
        return HttpResponse("File Not valid")
    if csv_file.multiple_chunks():
        return HttpResponse("Upload File is Big")
    file_data = csv_file.read().decode("utf-8")
    lines=file_data.split("\n")
    c=len(lines)
    Student=Manage_designation.objects.get(designationName="Student")
    for i in range(0,c-1):
        fields = lines[i].split(",")
        unique=generate_unique_id()
        Name=fields[0]
        Surname=fields[1]
        Fathername=fields[2]
        Email=fields[3]
        ContactNo=fields[4]
        Address=fields[5]
        Image=fields[10]
        Sem=fields[8]
        Desig=Manage_designation.objects.get(designationName=str(fields[9]))
        Dept=Manage_department.objects.get(departmentname=str(fields[7]))
        Coll=Manage_collage.objects.get(collageName=str(fields[6]))
        Manage_user(uniqueId=unique,semester=Sem,image=Image,userName=Name,surName=Surname,fatherName=Fathername,phoneNumber=ContactNo,email=Email,address=Address,Collage=Coll,department=Dept,designation=Desig).save()
        Manage_registration(uniqueId=unique,email=Email,username=Name,password="password@123",typeId=Student).save()
        details=Manage_user.objects.get(uniqueId=unique)
        topic='Mender Company'
        data='<p style="font-style: oblique;">Hi, <b>' +details.userName +'</b>Your registration code is <b>'+unique+'</b>.<br>Your password  is <b>password@123</b> <br>.Thank You.</p>'
        from_email='mender.company@gmail.com'
        to_email=Email
        msg=EmailMultiAlternatives(topic,data,from_email,[to_email])
        msg.content_subtype='html'
        msg.send()
        return redirect(request.META.get('HTTP_REFERER'))

# Create your views here.
#@@@@@@@@@@@@@@@@@@@@@@PROFILE@@@@@@@@@@@@@@@@@@@@
def account(request):
    if "Superadmin" in request.session:
        Data=request.session['Founder and Managing Trustee']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        return render(request,"account.html",{"superadmin":sessionData,"user":Users,"reg":sessionData})
    if "Founder and Managing Trustee" in request.session:
        Data=request.session['Founder and Managing Trustee']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        return render(request,"account.html",{"trustee":sessionData,"user":Users,"reg":sessionData})
    elif  "Vice-Chancellor" in request.session:
        Data=request.session['Vice-Chancellor']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        return render(request,"account.html",{"chancellor":sessionData,"user":Users ,"reg":sessionData})
    elif "Vice-President" in request.session:
        Data=request.session['Vice-President']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        return render(request,"account.html",{"president":sessionData,"user":Users,"reg":sessionData })
    elif "Director" in request.session:
        Data=request.session['Director']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        return render(request,"account.html",{"director":sessionData,"user":Users ,"reg":sessionData})
    elif "Head Of Department" in request.session:
        Data=request.session['Head Of Department']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        return render(request,"account.html",{"hod":sessionData,"user":Users,"reg":sessionData })
    elif "Teacher" in request.session:
        Data=request.session['Teacher']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        return render(request,"account.html",{"teacher":sessionData,"user":Users ,"reg":sessionData})
    elif "Student" in request.session:
        Data=request.session['Student']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        #Teacher=user.objects.filter(department.departmentname==Users.department.departmentname)
        return render(request,"account.html",{"student":sessionData,"user":Users ,"reg":sessionData})
    elif "Admin" in request.session:
        Data=request.session['Admin']
        sessionData=Manage_registration.objects.get(email=Data)
        Users=Manage_user.objects.get(email=Data)
        return render(request,"account.html",{"admin":sessionData,"user":Users,"reg":sessionData })
    else:
        return redirect("manageLogin")

def updateProfile(request,name):
    if request.method=="POST":
        sessionData=Manage_registration.objects.get(uniqueId=name)
        Users=Manage_user.objects.get(uniqueId=name)
        username=request.POST['username']
        phone=request.POST['number']
        address=request.POST['address']
        sessionData.username=username
        Users.phoneNumber=phone
        Users.address=address
        try:
            image=request.FILES['file']
            Users.image=image
        except MultiValueDictKeyError:
            pass
        finally:
            Users.save()
            sessionData.save()
        return redirect(request.META.get('HTTP_REFERER'))
