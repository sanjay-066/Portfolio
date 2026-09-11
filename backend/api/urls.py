"""URL patterns for the portfolio API."""
from django.urls import path
from . import views

urlpatterns = [
    path('profile/',    views.profile,         name='profile'),
    path('projects/',   views.project_list,    name='project-list'),
    path('skills/',     views.skill_list,       name='skill-list'),
    path('experience/', views.experience_list,  name='experience-list'),
    path('education/',  views.education_list,   name='education-list'),
    path('contact/',    views.contact_submit,   name='contact-submit'),
]
