from django.db import models

# Create your models here.

class Question(models.Model):
    texto = models.TextField(verbose_name="Texto de la pregunta")
    def __str__(self):
        return self.texto 

class ChooseAnswer(models.Model):
    pregunta = models.ForeignKey(Question, related_name='preguntas', on_delete=models.CASCADE)
    correcta = models.BooleanField(verbose_name='Is correct?', default=False, null=False)
    texto = models.TextField(verbose_name='Texto de la respuesta')

    def __str__(self):
        return self.texto 

    
