from django.db import models

class Video(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=30)
    descricao=models.TextField()
    url=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.titulo
