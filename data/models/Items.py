from django.db import models
from .abstract.Image import AbstractImage


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    colloq = models.CharField(max_length=255)
    plaintext = models.CharField(max_length=255)

    gold_base = models.PositiveIntegerField()
    gold_purchasable = models.BooleanField()
    gold_total = models.PositiveIntegerField()
    gold_sell = models.PositiveIntegerField()

    tags = models.ManyToManyField('data.ItemTag')

    maps_11 = models.BooleanField()
    maps_12 = models.BooleanField()
    maps_21 = models.BooleanField()
    maps_22 = models.BooleanField()
    depth = models.IntegerField(null=True)

    built_from = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class ItemTag(models.Model):
    name = models.CharField(max_length=50)
    items = models.ManyToManyField(Item, related_name='tag')


class ItemStats(models.Model):
    name = models.CharField(max_length=150)
    number = models.DecimalField(decimal_places=4, max_digits=20)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="stats")


class ItemEffect(models.Model):
    name = models.CharField(max_length=150)
    number = models.CharField(max_length=50)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="effect")


class ItemImage(AbstractImage):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_image')
