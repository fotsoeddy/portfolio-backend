from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand

from services.models import Profil

PORTFOLIO_DIR = Path(__file__).resolve().parents[5] / "portfolio"


class Command(BaseCommand):
    help = "Seeds (or updates) the single portfolio Profil row"

    def handle(self, *args, **kwargs):
        profile, created = Profil.objects.get_or_create(
            email="fotsoeddysteve@gmail.com",
            defaults={"nom": "Steve", "prenom": "Fotso Eddy"},
        )

        profile.nom = "Steve"
        profile.prenom = "Fotso Eddy"
        profile.titre = "Software Engineer / AI Engineer / DevOps Engineer"
        profile.tagline = (
            "Full-stack developer and DevOps engineer building scalable web applications, "
            "automating infrastructure, and shipping AI-powered products end to end."
        )
        profile.bio = (
            "I'm a software engineer focused on building reliable, production-grade web "
            "applications and the infrastructure that runs them. My work spans full-stack "
            "development with React, Next.js and Django, through to CI/CD pipelines, "
            "containerization, and cloud deployment."
        )
        profile.introduction = (
            "I am a Software Engineer, AI Engineer, and DevOps Engineer passionate about "
            "building, deploying and scaling web applications. With hands-on experience in "
            "React, Next.js, Django, Docker, and cloud infrastructure, I bridge the gap between "
            "development and operations — turning ideas into reliable, production-ready products."
        )
        profile.education_summary = "B.Tech in Computer Science (currently pursuing)"
        profile.projects_summary = "Built more than 5 full-stack projects with a focus on backend and DevOps practices"
        profile.languages_tools = (
            "Python, JavaScript, TypeScript, HTML, CSS, TailwindCSS, React.js, Next.js, Django, "
            "Django REST Framework, PostgreSQL, MongoDB, Git, Docker, Nginx, AWS (EC2, S3), "
            "Linux, Bash, CI/CD, Redis, Celery"
        )
        profile.telephone = ""
        profile.adresse = ""
        profile.ville = "Douala"
        profile.pays = "Cameroon"
        profile.github = "https://github.com/fotsoeddy"
        profile.linkedin = "https://www.linkedin.com/in/fotso-eddy-453a20256/"
        profile.twitter_x = "https://x.com/fotsoeddysteve"
        profile.instagram = ""
        profile.facebook = ""
        profile.youtube = ""
        profile.website = ""
        profile.disponible = True
        profile.années_experience = 3
        profile.projets_contribues = 25

        photo_path = PORTFOLIO_DIR / "assets" / "profile2.jpeg"
        photo_about_path = PORTFOLIO_DIR / "assets" / "user-image.png"
        cv_path = PORTFOLIO_DIR / "public" / "Fotso_Eddy_CV.pdf"

        if not profile.photo and photo_path.exists():
            with open(photo_path, "rb") as fh:
                profile.photo.save(photo_path.name, File(fh), save=False)

        if not profile.photo_about and photo_about_path.exists():
            with open(photo_about_path, "rb") as fh:
                profile.photo_about.save(photo_about_path.name, File(fh), save=False)

        if not profile.cv and cv_path.exists():
            with open(cv_path, "rb") as fh:
                profile.cv.save(cv_path.name, File(fh), save=False)

        profile.save()

        verb = "Created" if created else "Updated"
        self.stdout.write(self.style.SUCCESS(f"{verb} profile for {profile.prenom} {profile.nom} (3 years experience)."))
