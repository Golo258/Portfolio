from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects")
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f"Project {self.title}\t Info: {self.description}.\tLink: {self.link}"

    def get_description_type(self):
        return type(self.description)


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE
    )

    image = models.ImageField(upload_to="project_images/")

    def __str__(self):
        return f"{self.project.title} Image"


class Localization(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.city}, {self.country} ({self.postal_code})"


class Experience(models.Model):
    position = models.CharField(max_length=50, null=False, verbose_name="Job Ocupation")
    company = models.CharField(max_length=100, verbose_name="Company name")
    localization = models.ForeignKey(Localization, on_delete=models.CASCADE, default=1)
    start_date = models.DateField(verbose_name="Start date of work")
    end_date = models.DateField(verbose_name="End date of work", null=True, blank=True)

    def __str__(self) -> str:
        return f"Working as {self.position} in the company {self.company}, {self.localization} "

    def duration(self):
        if self.end_date:
            return f"{self.start_date.strftime('%Y-%m-%d')} - {self.end_date.strftime('%Y-%m-%d')}"
        else:
            return f"{self.start_date.strftime('%Y-%m-%d')} - currently"


class Skill(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField()
    level = models.IntegerField(
        default=1,
        verbose_name="Advanced Level",
        help_text="Enter value in range(0,10) ",
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )
    projects = models.ManyToManyField(
        "Project", related_name="related_projects", blank=True
    )

    def __str__(self) -> str:
        return f"Skill: {self.name} as {self.description} at a level {self.level}"
