from django.db import models

# Create your models here.

#creating a database named url with 2 tables, the parameters are link and uuid.

class Url(models.Model):
	link = models.CharField(max_length=10000) #the urls we want to shorten, the user input saved to this model
	uuid = models.CharField(max_length=10) #an Id with be attached to this link