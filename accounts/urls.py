from django.conf.urls import url
from . import views
urlpatterns = [
	
	url(r'^$',
		views.listview,
		name = "home"),

	url(r'^profile/$',
		views.profile,
		name = "profile"),

	url(r'^follow/$',
		views.user_follow,
		name="user_follow"),

	url(r'^(?P<username>[-\w]+)/$',
		views.detailview,
		name = "user_detail"),


]