from django.core.management.base import BaseCommand

from services.models import CategorieProjet, Projet

from ._placeholder_image import generate_placeholder


class Command(BaseCommand):
    help = "Seeds (or updates) example project categories and projects"

    def handle(self, *args, **kwargs):
        projects_data = [
            {
                "titre": "Frontend Storefront",
                "categorie": ("Website", "Web Application"),
                "description": "A responsive e-commerce website with an intuitive UI and fast load times.",
                "technologies": "Next.js, TypeScript, Tailwind CSS, Stripe",
                "lien_github": "https://github.com/fotsoeddy/frontend-storefront",
                "lien_demo": "https://frontend-storefront.vercel.app",
            },
            {
                "titre": "Geo-Based Field App",
                "categorie": ("Mobile", "Mobile Application"),
                "description": "A mobile app for location-based services with real-time data sync.",
                "technologies": "React Native, Firebase, MongoDB",
                "lien_github": "https://github.com/fotsoeddy/geo-field-app",
                "lien_demo": "https://geo-field-app.vercel.app",
            },
            {
                "titre": "AI-Powered Insights Platform",
                "categorie": ("AI", "AI System"),
                "description": "An AI platform for automated data analysis and business insights.",
                "technologies": "Django, PostgreSQL, Next.js, LangChain",
                "lien_github": "https://github.com/fotsoeddy/ai-insights-platform",
                "lien_demo": "https://ai-insights-platform.vercel.app",
            },
            {
                "titre": "Support Chatbot Assistant",
                "categorie": ("AI", "AI System"),
                "description": "An AI-driven chatbot using LLMs for customer support automation.",
                "technologies": "Python, OpenAI, Hugging Face",
                "lien_github": "https://github.com/fotsoeddy/support-chatbot",
                "lien_demo": "https://support-chatbot.vercel.app",
            },
            {
                "titre": "Personal Portfolio Platform",
                "categorie": ("Website", "Web Application"),
                "description": "A personal portfolio and blog engine with a Django REST backend.",
                "technologies": "Next.js, Tailwind CSS, Django REST Framework, GSAP",
                "lien_github": "https://github.com/fotsoeddy/portfolio",
                "lien_demo": "https://fotsoeddysteve.vercel.app",
            },
            {
                "titre": "Workflow Automation Toolkit",
                "categorie": ("Full Stack", "Full Stack Application"),
                "description": "A tool for automating repetitive backend tasks using scripting and scheduled jobs.",
                "technologies": "Python, Celery, Redis, Docker",
                "lien_github": "https://github.com/fotsoeddy/workflow-automation-toolkit",
                "lien_demo": "https://workflow-automation-toolkit.vercel.app",
            },
        ]

        for data in projects_data:
            categorie_nom, categorie_type = data["categorie"]
            category, _ = CategorieProjet.objects.get_or_create(nom=categorie_nom, defaults={"type_projet": categorie_type})

            project, created = Projet.objects.get_or_create(
                titre=data["titre"],
                defaults={
                    "categorie": category,
                    "description": data["description"],
                    "technologies": data["technologies"],
                    "lien_github": data["lien_github"],
                    "lien_demo": data["lien_demo"],
                },
            )

            if not created:
                project.categorie = category
                project.description = data["description"]
                project.technologies = data["technologies"]
                project.lien_github = data["lien_github"]
                project.lien_demo = data["lien_demo"]
                project.save()

            if not project.image:
                project.image.save(
                    f"{project.pk}.jpg",
                    generate_placeholder(data["titre"], f"project-{project.pk}.jpg"),
                    save=True,
                )

            verb = "Created" if created else "Updated"
            self.stdout.write(self.style.SUCCESS(f"{verb} project: {data['titre']}"))

        self.stdout.write(self.style.SUCCESS("Finished seeding projects."))
