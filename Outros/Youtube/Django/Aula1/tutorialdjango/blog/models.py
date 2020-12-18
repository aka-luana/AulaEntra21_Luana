from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True) # www.meusite.com/blog/introducao-ao-django
    author = models.ForeignKey(User, on_delete=models.CASCADE) # RELAÇÃO: many to one // o on_delete é caso o User seja deletado, o CASCADE faz com que o post seja deletado também
    body = models.TextField() # corpo do post
    created = models.DateTimeField(auto_now_add=True) # auto_now_add coloca automaticamento a data e a hora da criação
    updated = models.DateTimeField(auto_now=True) # a cada modificação do post o campo updated salva a hora e a data automaticamente

    class Meta: # Para organizar as postagens do mais novo para o mais velho
        ordering = ("-created",)

    def __str__(self): # Para ficar com o nome do artigo e não 'Post Object (num)'
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})