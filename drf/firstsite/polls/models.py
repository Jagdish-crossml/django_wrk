from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Document(models.Model):
	name = models.CharField(max_length=30)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	PDF = models.FileField(validators=[FileExtensionValidator(['pdf'])], upload_to='pdf_file',default='settings.MEDIA_ROOT/pdf_file/dummy.pdf')
	date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.user.username+"->"+self.name