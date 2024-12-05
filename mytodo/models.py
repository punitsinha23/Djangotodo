from django.db import models

class todo(models.Model):
    title = models.TextField(max_length=100)
    desc = models.TextField(max_length=500)
    due_date = models.DateField( null=True)

