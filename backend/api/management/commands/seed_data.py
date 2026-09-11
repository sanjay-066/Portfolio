"""
Management command to seed the database with default portfolio data.
Run with: python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from api.models import Project, Skill, Experience, Education


class Command(BaseCommand):
    help = 'Seed the database with sample portfolio data for Sanjay N'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding portfolio data...')

        # ===== PROJECTS =====
        Project.objects.all().delete()
        projects = [
            {
                'title': 'Personal Portfolio Website',
                'description': 'A full-stack personal portfolio showcasing projects and skills, built with Django REST API and plain HTML/CSS/JS frontend with MySQL database.',
                'tech_stack': 'Django, Python, MySQL, JavaScript, HTML, CSS',
                'github_url': 'https://github.com/sanjay-066',
                'live_url': '',
                'order': 1,
            },
            {
                'title': 'AI Chat Application',
                'description': 'An AI-powered conversational application integrating ML models to provide intelligent responses and assist users with real-world problem solving.',
                'tech_stack': 'Python, Flask, AI/ML, JavaScript',
                'github_url': 'https://github.com/sanjay-066',
                'live_url': '',
                'order': 2,
            },
            {
                'title': 'Task Management System',
                'description': 'A full-featured task management web application with user authentication, task CRUD operations, priority levels and real-time status tracking.',
                'tech_stack': 'Java, Spring Boot, MySQL, HTML, CSS',
                'github_url': 'https://github.com/sanjay-066',
                'live_url': '',
                'order': 3,
            },
        ]
        for p in projects:
            Project.objects.create(**p)
        self.stdout.write(self.style.SUCCESS(f'  [OK] Created {len(projects)} projects'))
        Skill.objects.all().delete()
        skills = [
            # Languages
            {'name': 'Python',     'category': 'Languages', 'proficiency_level': 90, 'order': 1},
            {'name': 'JavaScript', 'category': 'Languages', 'proficiency_level': 80, 'order': 2},
            {'name': 'Java',       'category': 'Languages', 'proficiency_level': 75, 'order': 3},
            {'name': 'C++',        'category': 'Languages', 'proficiency_level': 70, 'order': 4},
            # Web
            {'name': 'Django',     'category': 'Web Development', 'proficiency_level': 85, 'order': 1},
            {'name': 'HTML5',      'category': 'Web Development', 'proficiency_level': 90, 'order': 2},
            {'name': 'CSS3',       'category': 'Web Development', 'proficiency_level': 85, 'order': 3},
            {'name': 'REST APIs',  'category': 'Web Development', 'proficiency_level': 80, 'order': 4},
            # Databases
            {'name': 'MySQL',      'category': 'Databases', 'proficiency_level': 80, 'order': 1},
            {'name': 'PostgreSQL', 'category': 'Databases', 'proficiency_level': 70, 'order': 2},
            {'name': 'SQLite',     'category': 'Databases', 'proficiency_level': 85, 'order': 3},
            # Tools
            {'name': 'Git',        'category': 'Tools', 'proficiency_level': 85, 'order': 1},
            {'name': 'GitHub',     'category': 'Tools', 'proficiency_level': 85, 'order': 2},
            {'name': 'VS Code',    'category': 'Tools', 'proficiency_level': 90, 'order': 3},
            {'name': 'Linux',      'category': 'Tools', 'proficiency_level': 75, 'order': 4},
            # AI/ML
            {'name': 'Machine Learning', 'category': 'AI / ML', 'proficiency_level': 70, 'order': 1},
            {'name': 'NumPy',      'category': 'AI / ML', 'proficiency_level': 75, 'order': 2},
            {'name': 'Pandas',     'category': 'AI / ML', 'proficiency_level': 75, 'order': 3},
            {'name': 'Scikit-learn','category': 'AI / ML', 'proficiency_level': 65, 'order': 4},
        ]
        for s in skills:
            Skill.objects.create(**s)
        self.stdout.write(self.style.SUCCESS(f'  [OK] Created {len(skills)} skills'))

        # ===== EXPERIENCE =====
        Experience.objects.all().delete()
        experiences = [
            {
                'company': 'Tech Company (Update via Admin)',
                'role': 'Full Stack Developer Intern',
                'duration': '2024 — Present',
                'description': 'Developed and maintained web applications using Django and JavaScript. Collaborated with teams to design scalable APIs and integrate AI features into existing products.',
                'tech_stack': 'Django, Python, MySQL',
                'order': 1,
            },
            {
                'company': 'GitHub / Open Source',
                'role': 'Open Source Contributor',
                'duration': '2023 — 2024',
                'description': 'Contributed to open-source Python projects, fixing bugs, improving documentation, and implementing new features. Reviewed pull requests and engaged with developer communities.',
                'tech_stack': 'Python, Git, Open Source',
                'order': 2,
            },
        ]
        for e in experiences:
            Experience.objects.create(**e)
        self.stdout.write(self.style.SUCCESS(f'  [OK] Created {len(experiences)} experience entries'))

        # ===== EDUCATION =====
        Education.objects.all().delete()
        education = [
            {
                'institution': 'Your University (Update via Admin)',
                'degree': 'Bachelor of Engineering — Computer Science',
                'year': '2022 — 2026',
                'description': 'Studying core CS concepts including Data Structures, Algorithms, Operating Systems, Database Management, Software Engineering, and Artificial Intelligence.',
                'order': 1,
            },
            {
                'institution': 'Your School (Update via Admin)',
                'degree': 'Higher Secondary (XII) — Science / CS',
                'year': '2020 — 2022',
                'description': 'Completed higher secondary with focus on Mathematics, Physics, and Computer Science. Developed foundational programming skills in C++ and Python.',
                'order': 2,
            },
        ]
        for e in education:
            Education.objects.create(**e)
        self.stdout.write(self.style.SUCCESS(f'  [OK] Created {len(education)} education entries'))

        self.stdout.write(self.style.SUCCESS('\nPortfolio data seeded successfully!'))
        self.stdout.write('  --> Update placeholder entries via: http://localhost:8000/admin/')
