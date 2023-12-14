from django.db import models

TASK_STATUS=(
    ("Pending","Pending"),
    ("Inprogress","Inprogress"),
    ("Completed","Completed"),
)
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date= models.DateField(auto_now_add=True)
    status= models.CharField( 
        max_length = 20,
        choices = TASK_STATUS, 
        default = 'Pending'
        )

    def __str__(self):
        return self.title