from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

# O A4 trabalha com mm mas a biblioteca com pontos por isso vamos fazer a conversão

def conversaoMedida(mm):
    return mm/0.352777

appPasta = os.path.dirname(__file__)

# Criando
cnv = canvas.Canvas(appPasta+"\\teste.pdf", pagesize=A4)
cnv.drawString(conversaoMedida(75), conversaoMedida(140), "Este PDF foi gerado com python")
cnv.save()

# Youtube videos
# https://www.youtube.com/watch?v=DjxDm1MUbe0
# https://www.youtube.com/watch?v=p43qPkBNqp4&list=PLx4x_zx8csUhuVgWfy7keQQAy7t1J35TR&index=84