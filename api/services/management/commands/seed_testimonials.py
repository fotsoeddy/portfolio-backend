from django.core.management.base import BaseCommand

from services.models import Temoignage


class Command(BaseCommand):
    help = "Seeds the database with example testimonials"

    def handle(self, *args, **kwargs):
        # No photo is attached — these are illustrative placeholder
        # testimonials, not real client photos, so the frontend falls back
        # to an initials avatar rather than a stock/stolen headshot.
        testimonials_data = [
            {
                "titre": "Sarah Johnson",
                "position": "CEO at Techflow",
                "temoignage": "Fotso is an exceptional engineer. He took our complex legacy system and transformed it into a modern, scalable platform. His DevOps expertise saved us months of infrastructure headaches.",
                "etoiles": 5,
            },
            {
                "titre": "Michael Chen",
                "position": "Project Manager at Hooyis",
                "temoignage": "Working with Fotso was a breeze. He's not just a developer; he's a problem solver. The REST API he built for our mobile app is robust, well-documented, and incredibly fast.",
                "etoiles": 5,
            },
            {
                "titre": "Amara Okafor",
                "position": "Founder of AgriSmart",
                "temoignage": "The level of professionalism and technical depth Fotso brings is rare. He helped us automate our entire deployment pipeline, allowing us to ship features 3x faster than before.",
                "etoiles": 5,
            },
            {
                "titre": "David Wilson",
                "position": "CTO at CloudScale",
                "temoignage": "Fotso's deep understanding of containerization and orchestration transformed our deployment strategy. We now have a resilient, self-healing infrastructure that handles traffic spikes with ease.",
                "etoiles": 5,
            },
            {
                "titre": "Elena Rodriguez",
                "position": "Lead Designer at CreativePulse",
                "temoignage": "It's rare to find an engineer with such a strong eye for detail in both code and UI. Fotso translated our complex design visions into a high-performance Next.js application perfectly.",
                "etoiles": 4,
            },
            {
                "titre": "James Mwangi",
                "position": "Operations Director at LogisticX",
                "temoignage": "Automating our backend processes with Python and Redis reduced our processing time by 60%. Fotso delivered a solution that was not only stable but also very easy for our team to maintain.",
                "etoiles": 5,
            },
        ]

        for data in testimonials_data:
            testimonial, created = Temoignage.objects.get_or_create(
                titre=data["titre"],
                position=data["position"],
                defaults={"temoignage": data["temoignage"], "etoiles": data["etoiles"]},
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created testimonial: {data['titre']}"))
            else:
                self.stdout.write(self.style.WARNING(f"Testimonial already exists: {data['titre']}"))

        self.stdout.write(self.style.SUCCESS("Finished seeding testimonials."))
