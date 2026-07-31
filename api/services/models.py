from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify


class Experience(models.Model):
    titre       = models.CharField(max_length=200)
    compagnie   = models.CharField(max_length=200)
    description = models.TextField()
    date_debut  = models.DateField()
    date_fin    = models.DateField(null=True, blank=True)
    position    = models.CharField(max_length=200)
    pays        = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.titre} - {self.compagnie}"


class Service(models.Model):
    nom         = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.nom


class CategoriBlog(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Blog(models.Model):
    auteur      = models.CharField(max_length=200)
    categorie   = models.ForeignKey(CategoriBlog, on_delete=models.SET_NULL, null=True)
    titre       = models.CharField(max_length=200)
    slug        = models.SlugField(max_length=220, unique=True, blank=True)
    image       = models.ImageField(upload_to='blog/')
    description = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.titre)
            slug = base_slug
            suffix = 2
            while Blog.objects.exclude(pk=self.pk).filter(slug=slug).exists():
                slug = f"{base_slug}-{suffix}"
                suffix += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre


class Temoignage(models.Model):
    photo       = models.ImageField(upload_to='temoignages/', null=True, blank=True)
    titre       = models.CharField(max_length=200)
    position    = models.CharField(max_length=200)
    temoignage  = models.TextField()
    etoiles     = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.titre} - {self.position}"


class Contact(models.Model):
    nom       = models.CharField(max_length=200)
    email     = models.EmailField()
    message   = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.email}"


class CategorieProjet(models.Model):
    nom             = models.CharField(max_length=200)
    type_projet     = models.CharField(max_length=200)

    def __str__(self):
        return self.nom


class Projet(models.Model):
    categorie    = models.ForeignKey(CategorieProjet, on_delete=models.SET_NULL, null=True)
    image        = models.ImageField(upload_to='projets/')
    titre        = models.CharField(max_length=200)
    description  = models.TextField()
    technologies = models.CharField(max_length=500)
    lien_github  = models.URLField(blank=True)
    lien_demo    = models.URLField(blank=True)

    def __str__(self):
        return self.titre
    
    
class Profil(models.Model):
    # Infos personnelles
    nom         = models.CharField(max_length=100)
    prenom      = models.CharField(max_length=100)
    photo       = models.ImageField(upload_to='profil/')
    photo_about = models.ImageField(upload_to='profil/', null=True, blank=True)
    titre       = models.CharField(max_length=200)  # ex: "Software Engineer / DevOps Engineer"
    tagline     = models.CharField(max_length=500, blank=True) # Hero section summary
    bio         = models.TextField()  # bio / à propos
    introduction = models.TextField(blank=True) # The "I am a Software Engineer..." full intro
    
    # Education & Skills
    education_summary = models.TextField(blank=True) # ex: B.Tech in Computer Science
    projects_summary  = models.TextField(blank=True) # ex: Built more than 5 full-stack projects
    languages_tools   = models.TextField(blank=True) # List of languages and tools
    
    # Coordonnées
    email       = models.EmailField()
    telephone   = models.CharField(max_length=20, blank=True)
    adresse     = models.CharField(max_length=200, blank=True)
    ville       = models.CharField(max_length=100, blank=True)
    pays        = models.CharField(max_length=100, blank=True)
    
    # Réseaux sociaux
    github      = models.URLField(blank=True)
    linkedin    = models.URLField(blank=True)
    twitter_x   = models.URLField(blank=True)
    instagram   = models.URLField(blank=True)
    facebook    = models.URLField(blank=True)
    youtube     = models.URLField(blank=True)
    website     = models.URLField(blank=True)
    
    # CV
    cv          = models.FileField(upload_to='cv/', blank=True)
    
    # Infos pro
    disponible  = models.BooleanField(default=True)
    années_experience = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"