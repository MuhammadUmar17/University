from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.




# ----------------------------User Accounts---------------------------------------
class User(AbstractUser):
    # name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    remember_token = models.CharField(max_length=100, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_by = models.DateTimeField(auto_now=True)

    USERNAME_FIELd= 'email'
    REQUIRED_FIELDS= []
    




# ------------------------------Projects-------------------------------------
class Project(models.Model):
    name = models.CharField(max_length=200, null=True)
    slug = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500, null=True)
    background_image_url = models.URLField(null=True)
    avatar_image_url = models.ImageField(null = True)
    start_date = models.DateField(null=True) 
    end_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True)
    # id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name





# -------------------------------------User Roles---------------------------------------
class Role(models.Model):
    name = models.CharField(max_length=200, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name





# -------------------------------Priorities-------------------------

class Prioroty(models.Model):
    name = models.CharField(max_length=200, null=True)
    css_style = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name






# -------------------------------Statuses------------------------------

class Status(models.Model):
    name = models.CharField(max_length=200, null=True)
    css_style = models.CharField(max_length=100, null= True)
    created_by = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name






# -------------------------------Project Role ------------------------------------

class Project_role(models.Model):
    Project_id = models.ForeignKey(Project, on_delete= models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    role_id = models.ForeignKey(Role, on_delete= models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





# ---------------------------------Tasks--------------------------------

class Task(models.Model):
    project_id = models.ForeignKey(Project, on_delete= models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=500, null=True)
    assignee_id = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    priority_id = models.ForeignKey(Prioroty, on_delete= models.SET_NULL, null=True)
    status_id = models.ForeignKey(Status, on_delete= models.SET_NULL, null= True)
    estimate_hours = models.FloatField(null=True)
    progress_hours = models.FloatField(null=True)
    remaing_hours = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




# -------------------------------Comments----------------------------------

class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    task_id = models.ForeignKey(Task, on_delete= models.CASCADE)
    description = models.TextField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.description