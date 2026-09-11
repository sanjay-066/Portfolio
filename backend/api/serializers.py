"""DRF Serializers for portfolio API models."""
from rest_framework import serializers
from .models import Project, Skill, Experience, Education, ContactMessage


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'tech_stack',
            'github_url', 'live_url', 'image_url', 'order', 'is_featured',
        ]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'category', 'proficiency_level', 'icon', 'order']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'company', 'role', 'duration', 'description', 'tech_stack', 'order']


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'institution', 'degree', 'year', 'description', 'order']


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'subject', 'message', 'submitted_at']
        read_only_fields = ['id', 'submitted_at']

    def validate_email(self, value):
        """Basic email validation."""
        if not value or '@' not in value:
            raise serializers.ValidationError("A valid email address is required.")
        return value

    def validate_message(self, value):
        if len(value.strip()) < 10:
            raise serializers.ValidationError("Message must be at least 10 characters long.")
        return value
