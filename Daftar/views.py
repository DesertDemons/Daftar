from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, LoginForm, ProfileForm, PostForm
from .models import Profile
from .models import Post
from .models import Follow
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
# Create your views here.


def user_register(request):
	form = UserRegisterForm()
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			# user = form.save(commit=False)
			my_user = user.username
			my_password = user.password
			user.set_password(user.password)
			user.save()
			
			login(request, user)
			return redirect("create_profile")
	context = {
		"form": form
	}
	return render(request, 'register.html', context)

def user_login(request):
	form = LoginForm()
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			my_username = form.cleaned_data['username']
			my_password = form.cleaned_data['password']
			auth_user = authenticate(username=my_username, password=my_password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect("profile_page")
	context = {
		"form": form
	}
	return render(request, 'login.html', context)

def userlogout(request):
	logout(request)
	return redirect("login")

def profile_page(request):
	if request.user.is_anonymous:
		return redirect("login")
	profile_obj = Profile.objects.get(owner=request.user)
	posts = post_list(request,profile_obj.id)

	

	context = {
		"profile": profile_obj,
		"posts": posts,
	}
	return render(request, 'profile_page.html', context)

def post_list(request,Profile_id):
	profile_obj = Profile.objects.get(id=Profile_id)
	post_obj2 =  profile_obj.post_set.all()
	return post_obj2

def create_profile(request):

	if request.user.is_anonymous:
		return redirect("login")

	form = ProfileForm()

	
	if request.method == "POST":
		form = ProfileForm(request.POST, request.FILES or None)
		if form.is_valid():
			profile_obj = form.save(commit=False)
			profile_obj.owner = request.user
			profile_obj.save()
			return redirect("profile_page")
	context = {
		"form": form,

		}
	return render(request, 'create_profile.html', context)


def create_post(request, Profile_id):
	form = PostForm()
	profile_obj = Profile.objects.get(id=Profile_id)
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post_obj = form.save(commit=False)
			post_obj.profile = profile_obj
			post_obj.user = request.user
			post_obj.save()
			return redirect("profile_page")
	
	context = {
		"form": form,
		"profile": profile_obj,
	}
	return render(request, "create_post.html", context)


def search_user(request):
	profiles = Profile.objects.exclude(owner=request.user)
	query = request.GET.get('q')
	if query:
		profiles = profiles.filter(owner__username__icontains=query)


	# follow_list = followed_list(request)

	context = {
		"profiles": profiles,
		# "follow_list": follow_list,
	}
	return render(request, "search_user.html", context)

def follow_user(request, Profile_id):
	profile_obj = Profile.objects.get(id=Profile_id)
	follow_obj, created = Follow.objects.get_or_create(user=request.user, profile=profile_obj)

	if created:
		action="Following"
	else:
		action="Unfollow"
		follow_obj.delete()

	follow_count = profile_obj.follow_set.all().count()
	following_count = request.user.follow_set.all().count()


	context = {
		"action": action,
		"count": follow_count,
		"count_following": following_count,
	}
	return JsonResponse(context, safe=False)


# def followed_list(request):
# 	follow_list = []
# 	profile = Profile.objects.get(owner=request.user)
# 	followed = profile.follow_set.all()
# 	for follow in followed:
# 		follow_list.append(follow.user)

# 	return follow_list


# def followers_page(request):
# 	followed = followed_list(request)
# 	context = {
# 		"followers_page": followed,
# 	}
# 	return render(request, "followers_page.html", context)

def followed_list(request, Profile_id):
	follow_list = []
	profile = Profile.objects.get(id=Profile_id)
	followed = profile.follow_set.all()
	for follow in followed:
		follow_list.append(follow.user)

	return follow_list


def followers_page(request, Profile_id):
	followed = followed_list(request, Profile_id)
	context = {
		"followers_page": followed,
	}
	return render(request, "followers_page.html", context)

def following_list(request, Profile_id):
	following_list = []
	profile = Profile.objects.get(id=Profile_id)
	following = profile.owner.follow_set.all()
	for follow in following:
		following_list.append(follow.profile)

	return following_list

def following_page(request, Profile_id):
	following = following_list(request, Profile_id)
	context = {
		"following_pages": following,
	}
	return render(request, "following_page.html", context)


def user_profile(request, Profile_id):
	user_profile = Profile.objects.get(id=Profile_id)
	posts = post_list(request, user_profile.id)
	follow_list = followed_list(request, Profile_id)
	my_profile = Profile.objects.get(owner=request.user)
	context = {
		"user_profile": user_profile,
		"posts": posts,
		"follow_list": follow_list,
		"my_profile": my_profile,
	}
	return render(request, "user_profile.html", context)


def feed_page(request, Profile_id):
	following_feed = []
	print(following_feed)
	profile_obj = Profile.objects.get(id=Profile_id)
	print(profile_obj)
	users = profile_obj.owner.follow_set.all()
	print(users)
	
	


	for user in users:
		following_feed.append(user.profile)

	print(following_feed)


	

	context = {
		"profiles": following_feed,
		# "posts": posts,
	}
	return render(request, "feed_page.html", context)




