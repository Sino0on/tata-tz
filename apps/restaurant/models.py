from django.db import models
from django.utils.translation import gettext_lazy as _

rating = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))


class Restaurant(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField()
    image = models.ImageField(upload_to='rest/images/%Y/')
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=240)
    map_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('Restaurant')
        verbose_name_plural = _('Restaurants')
        ordering = ['-created_at']


class Review(models.Model):
    comment = models.CharField(max_length=200)
    rating = models.PositiveIntegerField(choices=rating)
    rest = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.comment[0:10]}.. - {self.rest.title}'

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')
        ordering = ['-created_at']
