from django.db import models
import datetime
import re, bcrypt

class LoginManager(models.Manager):
    def validator(self, inputdata):
        error = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        age_limit = datetime.timedelta(days=4745) # 13 years old
        print(age_limit)
        in_age = inputdata['dob']
        in_age = datetime.datetime.strptime(in_age, "%Y-%m-%d")
        today = datetime.datetime.today()
        curr_td = today - in_age
        
        if curr_td < age_limit:
            error['dob'] = "You are too young, at least 13 years old."
        if not inputdata['first_name'] or not inputdata['last_name'] or not inputdata['email'] or not inputdata['password']:
            error['exist'] = "All fields are required"
        if len(inputdata['first_name']) < 2:
            error['first_name'] = "First name is too short"
        if len(inputdata['last_name']) < 2:
            error['last_name'] = "Last name is too short"
        if not EMAIL_REGEX.match(inputdata['email']):
            error['email'] = 'Email address is invalid, its weird'
        if len(inputdata['password']) < 8:
            error['password'] = "Password needs to be at least 8 characters"
        if inputdata['password'] != inputdata['confirm']:
            error['nomatch'] = 'Password does not match'
        test = Login.objects.filter(email=inputdata['email'])
        if test:
            error['same'] = 'This email already exists, try another one'
        return error
    
    def login_vali(self, inputdata):
        error = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        user = Login.objects.filter(email=inputdata['email'])
        if user:
            logged_user = user[0]
        
        # print('***********************************')
        # print(logged_user.first_name)
        # print(logged_user.password)
        # print('***********************************')
        
        if not inputdata['email'] or not inputdata['password']:
            error['exist'] = 'All fields are required'
        if not user:
            error['user'] = 'User does not exists'
        if not EMAIL_REGEX.match(inputdata['email']):
            error['email'] = 'Email address is invalid, its weird'
        if not bcrypt.checkpw(inputdata['password'].encode(), logged_user.password.encode()):
            error['pass'] = 'Password does not match'
        return error

# Create your models here.
class Login(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=245)
    birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LoginManager()
    

#         in_age = postData['reg_dob']
#         in_age = datetime.datetime.strptime(in_age, "%Y-%m-%d")
#         today = datetime.datetime.today()
#         curr_td = today - in_age
#         if curr_td < age_limit:
#             errors['reg_dob'] = "You are too young to register.  Must be 13 years old."