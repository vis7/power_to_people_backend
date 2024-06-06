from django.db import models
from accounts.models import User

class Blog(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='blog_creatd_by', on_delete=models.CASCADE)
    likes = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title
