from django.db import models

# Create your models here.

class City (models.Model):
	class Meta:
		app_label = "DjangoREST"
		verbose_name = "City"
		verbose_name_plural = "Cities"


	name = models.CharField(blank=True, null=True, unique=True, max_length=250)
	population = models.IntegerField(unique=False, default=0)

	def __str__(self):
		return self.name

class Hero (models.Model):
	class Meta:
		app_label = "DjangoREST"
		verbose_name = "Hero"
		verbose_name_plural = "Heroes"


	name = models.CharField(blank=True, null=True, unique=True, max_length=250)
	alias = models.CharField(blank=True, null=True, unique=True, max_length=250)
	city = models.ForeignKey(City, on_delete=models.CASCADE, default=None, null=True)
	gender_choices = [(0, "Male "), (1, "Female"), (2, "Unknown")]
	gender = models.IntegerField(choices=gender_choices, default=1)

	def __str__(self):
		return self.name

