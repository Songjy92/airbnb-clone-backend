from django.db import models
from common.models import CommonModel

# Create your models here.


class Category(CommonModel):
    """Category for Room or Experience"""

    class CategoryKindChoices(models.TextChoices):
        ROOMS = ("room", "Rooms")
        EXPERIENCES = ("experiences", "Experiences")

    name = models.CharField(max_length=50)
    kind = models.CharField(
        max_length=30,
        choices=CategoryKindChoices.choices,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
