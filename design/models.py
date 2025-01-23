from django.db import models


class Design(models.Model):
    """
    Represents a design entry, such as a living room, bedroom, or other interior designs.
    """
    name = models.CharField(max_length=200, unique=True)  # Unique name for the design
    image_url = models.URLField()  # URL to the design's image
    description = models.TextField(blank=True, null=True)  # Optional description
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for the last update

    def __str__(self):
        return self.name
