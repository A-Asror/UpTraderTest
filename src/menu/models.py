from django.db import models
from django.utils.text import slugify

from src.base.models import BaseModel


class MenuModel(BaseModel):
    title: str = models.CharField(max_length=255, db_column="title")
    content: str = models.TextField(db_column="content")
    slug: str = models.SlugField(max_length=255, unique=True, blank=True, null=True, db_column="slug")

    class Meta:
        db_table = "menu"
        verbose_name = "Menu"
        verbose_name_plural = "Menu"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.set_slug()
        super(MenuModel, self).save(*args, **kwargs)

    def set_slug(self):
        self.slug = slugify(self.title)

