from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.signin),
	url(r'^signin$', views.signin),
	# url(r'^auth$', views.auth_view),
	url(r'^dashboard$', views.dashboard),
	url(r'^logout$', views.logout),
	url(r'^invalid$', views.invalid_login),
	url(r'^register$', views.register_user),
	url(r'^register_success$', views.register_success),
	url(r'^profile/(?P<profile_username>\w+)/$', views.profile),
	url(r'^booksowned$', views.booksowned),
	url(r'^rentedbooks$', views.rentedbooks),
	url(r'^addbook$', views.addbook),
	url(r'^searchbook$', views.searchbook),
	url(r'^editprofile$', views.editprofile),
    url(r'^bookdetails/(?P<book_id>\d+)/$', views.bookdetails),
    url(r'^modifystatus/(?P<book_id>\d+)/$', views.modifystatus),
    url(r'^reviews/(?P<borrowed_book_transaction_id>\d+)/$', views.reviews),
]
