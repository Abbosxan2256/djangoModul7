from django.db.models import Model, CharField, SlugField, ForeignKey, CASCADE
from django.utils.text import slugify


class Category(Model):
    name = CharField(max_length=255)
    slug = SlugField(unique=True, editable=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)


class Product(Model):
    title = CharField(max_length=255)
    slug = SlugField(unique=True, editable=True)
    category = ForeignKey('apps.Category', CASCADE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super().save(force_insert, force_update, using, update_fields)
