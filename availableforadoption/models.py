from django.db import models

STATUS = (
    ('AVAILABLE TO ADOPT', 'Available to Adopt'),
    ('LONG TERM FOSTER', 'Long Term Foster'),
    ('FOSTER TO ADOPT', 'Foster to Adopt'),
    ('AWAITING FOSTER', 'Awaiting Foster'),
)


class Species(models.Model):
    """
    Species Model 
    """
    species = models.CharField(max_length=100, blank=False)
    care_info = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../coming_soon', blank=False
    )
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['-species']
        """
        correct incorrect spelling of species
        """
        verbose_name_plural = 'Species'

    def __str__(self):
        return f'{self.id} {self.species}'

    def get_friendly_name(self):
        """
        friendly name instead of id
        """
        return self.friendly_name


class AvailableAdoption(models.Model):
    """
    Animals Available for Adoption
    """
    species = models.ForeignKey(
        'Species', null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    age = models.CharField(max_length=10, blank=False)
    gender = models.CharField(max_length=1, blank=False)
    image = models.ImageField(
        upload_to='images/', default='../coming_soon', blank=True
    )
    information = models.TextField(blank=False)
    status = models.CharField(max_length=30, choices=STATUS, default='available to adopt')
