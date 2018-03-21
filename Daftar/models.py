from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	owner = models.OneToOneField(User, on_delete=models.CASCADE)
	# image = models.ImageField(null=True)
	established = models.DateField(auto_now_add=True)
	bio = models.CharField(max_length=350)



class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	title = models.CharField(max_length=150)
	context = models.TextField()
	established = models.DateField(auto_now_add=True)


class Follow(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	# following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="who_follows")
	# follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="who_followed")