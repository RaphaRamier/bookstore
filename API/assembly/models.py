from django.db import models


class BookAssembly(models.Model):
    PAPER_CHOICES = (
        ('glossy', 'Glossy'),
        ('matte', 'Matte'),
        ('recycled', 'Recycled'),
        ('bond', 'Bond'),

    )

    COVER_CHOICES = (
        ('hardcover', 'Hardcover'),
        ('paperback', 'Paperback'),
        ('spiral', 'Spiral'),

    )

    BINDING_CHOICES = (
        ('perfect', 'Perfect Binding'),
        ('saddle', 'Saddle Stitch'),
        ('case', 'Case Binding'),
        ('spiral', 'Spiral Binding'),

    )

    binding_type = models.CharField(max_length=50, choices=BINDING_CHOICES)
    paper_type = models.CharField(max_length=50, choices=PAPER_CHOICES)
    cover_type = models.CharField(max_length=50, choices=COVER_CHOICES)
    weight = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.binding_type} - {self.paper_type} - {self.cover_type}'