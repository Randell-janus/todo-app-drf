from django.db import models

class Todo(models.Model):
  _id = models.BigAutoField(primary_key=True, editable=False)
  body = models.CharField(max_length=200)  
  duration = models.IntegerField(default=1)
  createdAt = models.DateTimeField(auto_now_add=True, null=True)
  updatedAt = models.DateTimeField(auto_now=True)

      
  def __str__(self):
    return self.body