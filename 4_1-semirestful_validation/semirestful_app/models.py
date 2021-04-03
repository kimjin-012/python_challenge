from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def validator(self, inputdata):
        error = {}
        if not inputdata['title'] or not inputdata['network'] or not inputdata['desc'] or not inputdata['date']:
            error['exist'] = "All fields are required"
        if len(inputdata['title']) < 2:
            error['title'] = "Show's title should be at least 2 characters"
        if len(inputdata['network']) < 3:
            error['network'] = "Show's network should be at least 3 characters"
        if len(inputdata['desc']) < 10:
            error['desc'] = "Show's description should be at least 10 characters"
        if len(inputdata['release']) > 10:
            error['date'] = "Show's date character limit has reahced, smaller word pls"
        return error
    
# Create your models here.
class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    date = models.DateField(default='1900-12-01')
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()