"""
Models for the portfolio API.
Manage all data via Django Admin at /admin/
"""
from django.db import models
from django.utils import timezone


class Project(models.Model):
    """A portfolio project entry."""
    title       = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack  = models.CharField(
        max_length=500,
        help_text="Comma-separated list of technologies, e.g. 'Django, Python, MySQL'"
    )
    github_url  = models.URLField(blank=True, null=True)
    live_url    = models.URLField(blank=True, null=True)
    image_url   = models.URLField(blank=True, null=True, help_text="Optional cover image URL")
    order       = models.PositiveIntegerField(default=0, help_text="Display order (lower = first)")
    is_featured = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title


class Skill(models.Model):
    """A skill or technology."""
    CATEGORY_CHOICES = [
        ('Languages',        'Languages'),
        ('Web Development',  'Web Development'),
        ('Databases',        'Databases'),
        ('Tools',            'Tools'),
        ('AI / ML',          'AI / ML'),
        ('Other',            'Other'),
    ]

    name              = models.CharField(max_length=100)
    category          = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    proficiency_level = models.PositiveIntegerField(
        default=80,
        help_text="Proficiency percentage (1-100)"
    )
    icon              = models.CharField(max_length=100, blank=True, help_text="Optional Font Awesome class")
    order             = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['category', 'order', 'name']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return f"{self.name} ({self.category})"


class Experience(models.Model):
    """Work experience entry."""
    company     = models.CharField(max_length=200)
    role        = models.CharField(max_length=200)
    duration    = models.CharField(max_length=100, help_text="e.g. 'Jan 2024 — Present'")
    description = models.TextField()
    tech_stack  = models.CharField(
        max_length=500, blank=True,
        help_text="Comma-separated technologies used"
    )
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return f"{self.role} @ {self.company}"


class Education(models.Model):
    """Education entry."""
    institution = models.CharField(max_length=300)
    degree      = models.CharField(max_length=300)
    year        = models.CharField(max_length=50, help_text="e.g. '2022 — 2026'")
    description = models.TextField(blank=True)
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Education'
        verbose_name_plural = 'Education'

    def __str__(self):
        return f"{self.degree} — {self.institution}"


class ContactMessage(models.Model):
    """Contact form submissions."""
    name         = models.CharField(max_length=200)
    email        = models.EmailField()
    subject      = models.CharField(max_length=300, blank=True)
    message      = models.TextField()
    submitted_at = models.DateTimeField(default=timezone.now)
    is_read      = models.BooleanField(default=False)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"Message from {self.name} <{self.email}> — {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"
