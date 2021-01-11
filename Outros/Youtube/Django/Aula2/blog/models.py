from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS = (
        ('rascunho','Rascunho'),
        ('publicado', 'Publicado'),
    )
    titulo = models.CharField(max_length=250)
    slug   = models.SlugField(max_length=250)
    autor  = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    conteudo  = models.TextField()
    publicado = models.DateTimeField(default=timezone.now) #Pega a hora e a data do momento da publicação
    criado    = models.DateTimeField(auto_now_add=True) #Pega a hora e a data do momento da criação
    alterado  = models.DateTimeField(auto_now=True) #Pega a hora e a data do momento da alteração
    status    = models.CharField(max_length=10,
                                 choices=STATUS,
                                 default='rascunho') #Status do post

    #Colocando o titulo como o nome do Post (caso contrário fica como Post Object(x)
    def __str__(self):
        return self.titulo
