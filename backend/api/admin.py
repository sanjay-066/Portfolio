"""Django Admin configuration for portfolio models."""
from django.contrib import admin
from .models import Project, Skill, Experience, Education, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display  = ('title', 'tech_stack', 'order', 'is_featured', 'created_at')
    list_editable = ('order', 'is_featured')
    list_filter   = ('is_featured',)
    search_fields = ('title', 'description', 'tech_stack')
    ordering      = ('order', '-created_at')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display  = ('name', 'category', 'proficiency_level', 'order')
    list_editable = ('order', 'proficiency_level')
    list_filter   = ('category',)
    search_fields = ('name',)
    ordering      = ('category', 'order')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display  = ('role', 'company', 'duration', 'order')
    list_editable = ('order',)
    search_fields = ('role', 'company', 'description')
    ordering      = ('order',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display  = ('degree', 'institution', 'year', 'order')
    list_editable = ('order',)
    search_fields = ('degree', 'institution')
    ordering      = ('order',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display   = ('name', 'email', 'subject', 'submitted_at', 'is_read')
    list_editable  = ('is_read',)
    list_filter    = ('is_read',)
    search_fields  = ('name', 'email', 'message')
    readonly_fields = ('submitted_at',)
    ordering       = ('-submitted_at',)

    # Prevent creation of messages from admin (read-only model)
    def has_add_permission(self, request):
        return False


# ===== Customise Admin Site Branding =====
admin.site.site_header  = "Sanjay N — Portfolio Admin"
admin.site.site_title   = "Portfolio Admin"
admin.site.index_title  = "Manage Your Portfolio Content"
