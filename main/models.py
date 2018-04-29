from django.db import models

# Create your models here.
class User_text(models.Model):
    """Model definition for User_text."""

    # TODO: Define fields here
    text = models.CharField(max_length=1024)
    gif = models.URLField(blank=True)
    class Meta:
        """Meta definition for User_text."""

        verbose_name = 'User_text'
        verbose_name_plural = 'User_texts'

    def __str__(self):
        """Unicode representation of User_text."""
        return self.text
