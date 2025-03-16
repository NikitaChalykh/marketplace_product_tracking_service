from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Product(models.Model):
    """Model for tracking product vendor codes"""
    vendor_code = models.PositiveIntegerField(
        unique=True,
        verbose_name="Vendor Code"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="User"
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Creation Date"
    )

    class Meta:
        verbose_name = "Tracked Vendor Code"
        verbose_name_plural = "Tracked Vendor Codes"
        ordering = ["date"]

    def __str__(self):
        return str(self.vendor_code)


class Card(models.Model):
    """Model for product cards"""
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="cards",
        verbose_name="Product"
    )
    vendor_code = models.PositiveIntegerField(
        verbose_name="Vendor Code"
    )
    name = models.CharField(
        max_length=200,
        verbose_name="Recipe Name"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="cards",
        verbose_name="User"
    )
    discount_value = models.PositiveIntegerField(
        verbose_name="Discount Price"
    )
    value = models.PositiveIntegerField(
        verbose_name="Full Price"
    )
    brand = models.CharField(
        max_length=200,
        verbose_name="Brand"
    )
    supplier = models.CharField(
        max_length=100,
        verbose_name="Supplier"
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Creation Date"
    )

    class Meta:
        verbose_name = "Product Card"
        verbose_name_plural = "Product Cards"
        ordering = ["date"]

    def __str__(self):
        return self.name
