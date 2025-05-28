from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm #manejar las unidades de tamaño
import datetime
import os

# doc = DocxTemplate(r"C:\Users\Sistemas\Desktop\try_contratacion\backend\firma_fomatos\plantilla_prueba.docx")

ruta_imagen = r"C:\Users\Sistemas\Desktop\try_contratacion\backend\firma_fomatos\firma_prueba.jpg"
# ruta_imagen = "/firma_formatos/firma_prueba.jpg"
ruta_script=__file__
ruta_carpetas_formatos = os.path.dirname(ruta_script)
print(ruta_carpetas_formatos)
ruta_carpeta_plantilla_administrativos=os.path.join(ruta_carpetas_formatos,"Plantillas_administrativo")
#LLena el array con el contenido de la carpeta en la ruta absoluta asignada, siempre y cuando sea un archivo
archivos_administrativos = [i for i in os.listdir(ruta_carpeta_plantilla_administrativos) if os.path.isfile(os.path.join(ruta_carpeta_plantilla_administrativos,i))]
# print(archivos_administrativos)
for i in archivos_administrativos:
    print(os.path.join(ruta_carpeta_plantilla_administrativos,i))
# print(os.listdir(ruta_carpeta_plantilla_administrativos))
print(ruta_carpeta_plantilla_administrativos)
ruta_carpeta_plantilla_antibioticos= None
ruta_carpeta_plantilla_cuidadores = None
ruta_carpeta_plantilla_permanentes = None


# imagen = InlineImage(doc,ruta_imagen, width=Mm(40))
fecha = datetime.datetime.now()
dia = fecha.day
mes = fecha.month
año = fecha.year
strign_fecha = f'{dia}/{mes}/{año}'
variables = {'fecha':strign_fecha,
             'nombre':'Diana Urueña',
             'cedula':'0000018451',
             'cargo':'Gerente General',
            #  'firma' : imagen
             }
# print(variables)

# doc.render(variables)
# doc.save(r'C:\Users\Sistemas\Desktop\try_contratacion\backend\firma_fomatos\prueba.docx')