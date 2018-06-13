from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^view/$', views.display_trainings),
    url(r'^training-detail/(?P<training_id>\d+)/$', views.display_training),
    url(r'^event/$', views.event),
]