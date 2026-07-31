from django.core.management.base import BaseCommand

from services.models import Blog, CategoriBlog

from ._placeholder_image import generate_placeholder


class Command(BaseCommand):
    help = "Seeds the database with example blog categories and posts"

    def handle(self, *args, **kwargs):
        deleted, _ = Blog.objects.all().delete()
        if deleted:
            self.stdout.write(self.style.WARNING(f"Deleted {deleted} existing blog post(s)."))

        posts_data = [
            {
                "titre": "Dockerizing a Django + Next.js App: A Full Guide",
                "categorie": "DevOps",
                "description": "Step-by-step walkthrough of containerizing a full-stack application with Docker and Docker Compose, from development to production.",
            },
            {
                "titre": "Building REST APIs with Django REST Framework",
                "categorie": "Backend",
                "description": "Learn how to build clean, secure, and scalable REST APIs using DRF, JWT authentication, and proper serializer design patterns.",
            },
            {
                "titre": "CI/CD Pipelines with GitHub Actions",
                "categorie": "DevOps",
                "description": "Automate your testing and deployment workflows using GitHub Actions — from lint checks to production deploys on every push.",
            },
            {
                "titre": "Getting Started with Redis and Celery in Django",
                "categorie": "Backend",
                "description": "Offload long-running tasks, schedule jobs, and improve app performance using Celery workers backed by Redis.",
            },
            {
                "titre": "Next.js 15 App Router: What You Need to Know",
                "categorie": "Frontend",
                "description": "A practical guide to the App Router in Next.js 15 — layouts, server components, streaming, and route handlers explained.",
            },
            {
                "titre": "Nginx as a Reverse Proxy: Production Setup Guide",
                "categorie": "DevOps",
                "description": "Configure Nginx to securely serve your web application, handle SSL termination, and load balance across multiple server instances.",
            },
        ]

        for data in posts_data:
            category, _ = CategoriBlog.objects.get_or_create(nom=data["categorie"])

            post = Blog.objects.create(
                titre=data["titre"],
                auteur="Fotso Eddy Steve",
                categorie=category,
                description=data["description"],
            )

            post.image.save(
                f"{post.pk}.jpg",
                generate_placeholder(data["titre"], f"blog-{post.pk}.jpg"),
                save=True,
            )
            self.stdout.write(self.style.SUCCESS(f"Created blog post: {data['titre']} (slug={post.slug})"))

        self.stdout.write(self.style.SUCCESS("Finished seeding blog posts."))
