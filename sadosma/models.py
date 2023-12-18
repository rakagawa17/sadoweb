from django.db import models

class Trivia(models.Model):

    class Meta:
        db_table = 'trivias'
    
    japanese = models.CharField(max_length=255)
    english = models.CharField(max_length=255)
    chinese1 = models.CharField(max_length=255)
    chinese2 = models.CharField(max_length=255)
    korean = models.CharField(max_length=255)
    mongolian = models.CharField(max_length=255)
    category = models.CharField(max_length=15)
    url1 = models.CharField(max_length=255)
    url2 = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=1023, null=True, blank=True)

    def __str__(self):
        return self.japanese