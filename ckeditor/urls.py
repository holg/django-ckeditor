# TODO dj3
from utils.helper import url
from ckeditor import views

urlpatterns = [
    url(r'^upload/', views.upload, name='ckeditor_upload'),
    url(r'^browse/', views.browse, name='ckeditor_browse'),
]
