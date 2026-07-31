from django.core.management.base import BaseCommand
from services.models import Experience
import datetime

class Command(BaseCommand):
    help = 'Seeds the database with default experiences'

    def handle(self, *args, **kwargs):
        experiences_data = [
            {
                'titre': 'Mobile/Software Engineer',
                'compagnie': 'Raiseup',
                'description': 'Spearheaded the development of cross-platform mobile applications and scalable backend services. Collaborated with cross-functional teams to deliver high-performance software solutions that improved user engagement and operational efficiency.',
                'date_debut': datetime.date(2025, 1, 1),
                'date_fin': None,
                'position': 'Remote',
                'pays': 'USA'
            },
            {
                'titre': 'Freelance Full Stack Engineer',
                'compagnie': 'Self-Employed / Freelance',
                'description': 'Designed, developed, and deployed full-stack web applications for various clients. Managed the entire software development lifecycle from gathering requirements and designing UI/UX to backend architecture, database modeling, and deployment.',
                'date_debut': datetime.date(2024, 1, 1),
                'date_fin': datetime.date(2026, 1, 1),
                'position': 'Remote',
                'pays': 'USA'
            },
            {
                'titre': 'Backend Developer',
                'compagnie': 'Hooyia',
                'description': 'Architected and maintained robust RESTful APIs using modern backend frameworks. Optimized database queries, implemented secure authentication flows, and integrated third-party services to enhance platform capabilities and scale.',
                'date_debut': datetime.date(2024, 1, 1),
                'date_fin': None,
                'position': 'On-site / Hybrid',
                'pays': 'Cameroon'
            },
            {
                'titre': 'Frontend Engineer',
                'compagnie': 'Unemployed',
                'description': 'Designed and developed responsive, user-friendly web interfaces using React.js, Next.js and Tailwind CSS, focusing on performance and UX.',
                'date_debut': datetime.date(2024, 4, 1),
                'date_fin': datetime.date(2026, 1, 1),
                'position': 'Remote',
                'pays': 'USA'
            }
        ]

        for data in experiences_data:
            experience, created = Experience.objects.get_or_create(
                titre=data['titre'],
                compagnie=data['compagnie'],
                defaults={
                    'description': data['description'],
                    'date_debut': data['date_debut'],
                    'date_fin': data['date_fin'],
                    'position': data['position'],
                    'pays': data['pays']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully created experience: {data['titre']} at {data['compagnie']}"))
            else:
                self.stdout.write(self.style.WARNING(f"Experience already exists: {data['titre']} at {data['compagnie']}"))

        self.stdout.write(self.style.SUCCESS('Finished seeding experiences.'))
