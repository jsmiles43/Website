from django.db import models


class Card(models.Model):
	name = models.CharField(max_length = 50)
	description = models.TextField()
	code = models.CharField(max_length = 50)
	url = models.URLField(blank=True, max_length = 50)
	group = models.IntegerField(default = 1)
	


	CARD_CHOICES = (
		('Software', 'Software'),
		('Stack', 'Stack'),
		('Language', 'Language'),
	)

	card_choice = models.CharField(
        max_length=10,
        choices=CARD_CHOICES,
        default='Software',
    )


	def __str__(self):
		return str(self.name)

