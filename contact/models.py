from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField()
    message = models.TextField()
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    def __str__(self):
        return self.name
