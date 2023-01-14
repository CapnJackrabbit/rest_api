from django.db import models
from uuid import uuid4

class Books(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4,editable=False)
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    ano_lan = models.IntegerField()
    estado = models.CharField(max_length=50)
    paginas = models.IntegerField()
    editora = models.CharField(max_length=50)
    criado_em = models.DateField(auto_now_add=True)
