from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^home/$', views.home),
    url(r'^all-trainings/$', views.display_trainings),
    url(r'^training-detail/(?P<training_id>\d+)/$', views.display_training),
    url(r'^training-detail/(?P<training_id>\d+)/update/$', views.update_training),
    url(r'^training/plan/$', views.plan_training),
    url(r'^training/create/$', views.create_training),
    url(r'^warm-up/create/$', views.create_warm_up),
    url(r'^core/create/$', views.create_core),
    url(r'^cool-down/create/$', views.create_cool_down),
    url(r'^calendar/$', views.display_calendar),
    url(r'^profile/$', views.display_profile),
    url(r'^profile/update/$', views.update_profile),
]