from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#Para AJAX
from django.http import JsonResponse
from django.views.decorators.http import require_POST
#from common.decorators import ajax_required
from .models import Contact

#@ajax_required #solo funciona si se hace un peticion AJAX
@require_POST #solo funciona si es una peticion POST
@login_required
def user_follow(request):

	user_id = request.POST.get('id')
	action = request.POST.get('action')
	if user_id and action:
		try:
			print("si")
			user = User.objects.get(id=user_id)
			if action == 'follow':
				print("yeah")
				Contact.objects.get_or_create(user_from=request.user, user_to=user)
			else:
				print("no")
				Contact.objects.filter(user_from=request.user, user_to=user).delete()
			return JsonResponse({'status':'OK'})

		except User.DoesNotExist:
			return JsonResponse({'status':'nel'})

	else:
		print("no")
		JsonResponse({'status':'nel'})

@login_required
def listview(request):
	users = User.objects.filter(is_active=True)
	return render(request,'user/list.html',{'secction':'people','users':users})

@login_required
def detailview(request, username):
	user = get_object_or_404(User, username=username,is_active=True)
	return render(request,'user/detail.html',{'section':'people','user':user})

@login_required
def profile(request):
	followers = Contact.objects.filter(user_to=request.user)
	return render(request, 'user/profile.html',{'user':request.user,'followers':followers})