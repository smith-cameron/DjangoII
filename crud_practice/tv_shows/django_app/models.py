from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45, default=None)
    email = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45, default=None)
    description = models.TextField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"""<Show object: 
        Title: {self.title} 
        Network: {self.network}
        description: {self.description}
        release_date: {self.release_date}
        created_at: {self.created_at}
        ({self.id})>"""