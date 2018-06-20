from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^home/$', views.home),
    url(r'^all-trainings/$', views.display_trainings),
    url(r'^training-detail/(?P<training_id>\d+)/$', views.display_training, name='training_detail'),
    url(r'^training-detail/(?P<training_id>\d+)/update/$', views.update_training),
    url(r'^training-detail/(?P<training_id>\d+)/subscribe/$', views.training_subscribe),
    url(r'^training-detail/all/subscribe/$', views.training_subscribe_all),
    url(r'^training-detail/all/unsubscribe/$', views.training_unsubscribe_all),
    url(r'^training-detail/week/(?P<week_nb>\d+)/subscribe/$', views.training_subscribe_week),
    url(r'^training-detail/week/(?P<week_nb>\d+)/unsubscribe/$', views.training_unsubscribe_week),
    url(r'^training-detail/(?P<training_id>\d+)/unsubscribe/$', views.training_unsubscribe),  
    url(r'^training/plan/$', views.plan_training),
    url(r'^training/create/$', views.create_training),
    url(r'^warm-up/create/$', views.create_warm_up),
    url(r'^core/create/$', views.create_core),
    url(r'^cool-down/create/$', views.create_cool_down),
    url(r'^calendar/$', views.display_calendar),
    url(r'^profile/$', views.display_profile),
    url(r'^profile/update/$', views.update_profile),
]