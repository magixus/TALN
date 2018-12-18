from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

name_app = "docsearch"
urlpatterns = [
    path('', views.index, name='index'),
    path('documents/', views.documents, name='documents'),
    path('documents/<str:doc>', views.show_doc, name='show_doc'),
    path('statistics/', views.statistics, name='statistics'),
    path('infos/', views.infos, name='infos'),
    path("searchInDocs/", views.searchTags, name="searchTags"),
    path("editcorpus/", views.addToCorpus, name="editcorpus")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
