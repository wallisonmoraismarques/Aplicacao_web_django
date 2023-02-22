from django.db import models
from django.contrib.auth.models import User

class Empresa (models.Model):
    cidade = models.CharField(max_length=100)
    descrisao = models.TextField()
    telefone = models.CharField( max_length=11)
    email = models.EmailField()
    data = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='empresa')
    ativo = models.BooleanField(default=True)
    cnpj = models.CharField(max_length=14)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self): 
        return str(self.id)

    class Meta:
        db_table ="empresa"
