"""
API Views for portfolio endpoints.

Endpoints:
  GET  /api/projects/     — list all featured projects
  GET  /api/skills/       — list all skills
  GET  /api/experience/   — list all experience entries
  GET  /api/education/    — list all education entries
  POST /api/contact/      — submit a contact message
  GET  /api/profile/      — hero/about profile data
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Project, Skill, Experience, Education, ContactMessage
from .serializers import (
    ProjectSerializer,
    SkillSerializer,
    ExperienceSerializer,
    EducationSerializer,
    ContactMessageSerializer,
)

# ===== Static profile data (update here or extend with a Profile model) =====
PROFILE_DATA = {
    "name": "Sanjay N",
    "title": "Full Stack Developer",
    "bio": (
        "Passionate Full Stack Developer who loves building scalable and beautiful "
        "web applications and learns AI. I enjoy solving real world problems."
    ),
    "location": "India",
    "email": "contact@sanjay.dev",
    "github": "https://github.com/sanjay-066",
    "linkedin": "https://www.linkedin.com/in/sanjay-n-44a622378",
    "skills_summary": ["Python", "JavaScript", "Java", "C++"],
    "available_for_work": True,
}


@api_view(['GET'])
def profile(request):
    """Return hero/about profile information."""
    return Response(PROFILE_DATA)


@api_view(['GET'])
def project_list(request):
    """Return all featured projects ordered by display order."""
    projects = Project.objects.filter(is_featured=True)
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def skill_list(request):
    """Return all skills."""
    skills = Skill.objects.all()
    serializer = SkillSerializer(skills, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def experience_list(request):
    """Return all experience entries."""
    experiences = Experience.objects.all()
    serializer = ExperienceSerializer(experiences, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def education_list(request):
    """Return all education entries."""
    education = Education.objects.all()
    serializer = EducationSerializer(education, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def contact_submit(request):
    """Accept and store a contact form submission."""
    serializer = ContactMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"detail": "Message received! I'll get back to you soon."},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
