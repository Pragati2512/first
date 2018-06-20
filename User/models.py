from django.db import models
from enum import  Enum

# Create your models here.
# User Table
#enum for User_type
class UserType(Enum):
    STD="STUDENT"
    FLT="FACULTY"
    USR="USER"
    ALM="ALUMNI"
# enum for blood group

class BloodGroup(Enum):
    OMinus="O-Minus"
    AMinus = "A-Minus"
    BMinus = "B-Minus"
    ABMinus = "AB-Minus"
    OPlus = "O-Positive"
    APlus = "A-Positive"
    BPlus = "B-Positive"
    ABPlus = "AB-Positive"


class Gender(Enum):
    M="MALE"
    F="FEMALE"
    O="OTHERS"

class Catogery(Enum):
    GEN="GENERAL"
    OBC="OTHER BACKWARD CLASS"
    SC="SCHEDULE CASTE"
    ST="SCHUDLE TRIBE"




class User(models.Model):
    user_id = models.CharField(primary_key=True, unique=True, max_length=30)
    password = models.CharField(max_length=256)
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = [(tag,tag.value) for tag in Gender]
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    contact = models.IntegerField()
    email = models.EmailField()
    photo = models.ImageField()
    category = [(tag,tag.value) for tag in Catogery]
    blood_group = [(tag,tag.value) for tag in BloodGroup]
    user_type= [(tag,tag.value) for tag in UserType]



