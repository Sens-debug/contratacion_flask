from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm #manejar las unidades de tamaño
import datetime
import os

doc = DocxTemplate(r"C:\Users\Sistemas\Desktop\try_contratacion\backend\firma_fomatos\plantilla_prueba.docx")

# ruta_imagen = r"C:\Users\Sistemas\Desktop\try_contratacion\backend\firma_fomatos\firma_prueba.jpg"
ruta_imagen = "/firma_formatos/firma_prueba.jpg"
ruta_script=__file__
ruta_formatos = os.path.dirname(ruta_script)
ruta_backend = os.path.dirname(ruta_formatos)
print( ruta_formatos, ruta_backend)
print(os.path.abspath(ruta_script))
imagen = InlineImage(doc,ruta_imagen, width=Mm(40))
fecha = datetime.datetime.now()
dia = fecha.day
mes = fecha.month
año = fecha.year
strign_fecha = f'{dia}/{mes}/{año}'
variables = {'fecha':strign_fecha,
             'nombre':'Diana Urueña',
             'cedula':'0000018451',
             'cargo':'Gerente General',
             'firma' : imagen
             }
print(variables)

# doc.render(variables)
# doc.save(r'C:\Users\Sistemas\Desktop\try_contratacion\backend\firma_fomatos\prueba.docx')
