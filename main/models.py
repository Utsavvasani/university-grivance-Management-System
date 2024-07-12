from django.db import models

# Create your models here.
class Manage_grievanceType(models.Model):
    typeId=models.AutoField
    typeName=models.TextField(max_length=100,unique=True)

class Manage_collage(models.Model):
    collageId=models.AutoField
    collageName=models.TextField(max_length=100)
    collageAddress=models.TextField(max_length=300)
    collageDescription=models.TextField(max_length=550)
    collageImage=models.ImageField(upload_to="collage/")
    
class Manage_department(models.Model):
    departmentId=models.AutoField
    collageId=models.ForeignKey(Manage_collage,on_delete=models.CASCADE)
    departmentname=models.CharField(max_length=200)
    semester=models.IntegerField()

class Manage_designation(models.Model):
    designationId=models.AutoField
    designationName=models.TextField(max_length=30)
    power=models.IntegerField()

class Manage_user(models.Model):
    userId=models.AutoField
    uniqueId=models.TextField(max_length=17)
    image=models.ImageField(upload_to="users/")
    userName=models.TextField(max_length=20)
    surName=models.TextField(max_length=20)
    fatherName=models.TextField(max_length=20)
    department=models.ForeignKey(Manage_department,on_delete=models.CASCADE,null=True)
    designation=models.ForeignKey(Manage_designation,on_delete=models.CASCADE,null=True)
    Collage=models.ForeignKey(Manage_collage,on_delete=models.CASCADE,null=True)
    semester=models.IntegerField(null=True)
    phoneNumber=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    address=models.CharField(max_length=100)

class Manage_registration(models.Model):
    id=models.AutoField
    uniqueId=models.TextField(max_length=17)
    email=models.EmailField(unique=True)
    username=models.TextField(max_length=50)
    password=models.TextField(max_length=50)
    typeId=models.ForeignKey(Manage_designation,on_delete=models.CASCADE)

class Manage_complainData(models.Model):
    id=models.AutoField
    complainCode=models.TextField(max_length=20)
    nameOfComplainant = models.ForeignKey(Manage_registration, on_delete=models.CASCADE, null=True,related_name='nameOfComplainant')
    nameOfSolver = models.ForeignKey(Manage_registration, on_delete=models.CASCADE, null=True,related_name='nameOfSolver')
    category=models.ForeignKey(Manage_grievanceType,on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to="GrievanceImages/",null=True)
    description=models.TextField(max_length=1000)
    remark=models.TextField(max_length=1000,null=True)
    grievanceDate=models.DateField(auto_now_add=True)
    solvingDate=models.DateField(auto_now_add=False,null=True,auto_now=True)
    status=models.IntegerField()
    feedback=models.TextField(max_length=100,null=True)
    to=models.ForeignKey(Manage_user,on_delete=models.CASCADE,null=True)

    
    