from django.db import models
from django.contrib import admin
# Create your models here.

class analizador(models.Model):

 css = {"all":("static/css/tree-vviewer.css",)}   
 js=("static/js/d3Tree.js",)
 js=("static/js/parser.js",)

admin.site.register(analizador)
