from django.db import models

class SocioTorcedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    forma_pagamento = models.CharField(max_length=20, choices=[('pix', 'Pix'), ('cartao', 'Cartão de Crédito')])

    def __str__(self):
        return self.nome
