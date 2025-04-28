from django.db import models

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='image/', null=True, blank=True)
    views_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True) 
    
    def str(self) -> str:
        return f"Model<{self.title}>"