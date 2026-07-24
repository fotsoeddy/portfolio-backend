from django.core.management.base import BaseCommand
from services.models import Service

class Command(BaseCommand):
    help = 'Seeds the database with default services'

    def handle(self, *args, **kwargs):
        services_data = [
            {
                'nom': 'AI Automation',
                'description': 'Automate your business workflows and processes using cutting-edge Artificial Intelligence solutions.'
            },
            {
                'nom': 'DevOps',
                'description': 'Streamline your software delivery with CI/CD pipelines, containerization, and infrastructure as code.'
            },
            {
                'nom': 'Machine Learning Model Development',
                'description': 'Custom Machine Learning models trained on your data to provide predictive insights and intelligent features.'
            },
            {
                'nom': 'Web Development',
                'description': 'Full-stack web application development using modern frameworks like Django, React, and Next.js.'
            },
            {
                'nom': 'Mobile App Development',
                'description': 'Native and cross-platform mobile application development for iOS and Android.'
            },
            {
                'nom': 'UI/UX Design',
                'description': 'User-centered design to ensure your applications are intuitive, beautiful, and engaging.'
            },
            {
                'nom': 'Cloud Architecture',
                'description': 'Scalable and secure cloud architecture design and deployment on AWS, GCP, or Azure.'
            }
        ]

        for data in services_data:
            service, created = Service.objects.get_or_create(
                nom=data['nom'], 
                defaults={'description': data['description']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully created service: {data['nom']}"))
            else:
                self.stdout.write(self.style.WARNING(f"Service already exists: {data['nom']}"))

        self.stdout.write(self.style.SUCCESS('Finished seeding services.'))
