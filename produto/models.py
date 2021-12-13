from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(max_length=255)
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='produto_images/%Y/%m', blank=True, null=True)
    slug = models.SlugField(unique=True)
    preco_marketing = models.FloatField(default=0)
    preco_marketing_promo = models.FloatField(default=0)
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variacao'),
            ('S', 'Simples')
        )
    )
    
    def __str__(self):
        return self.nome
