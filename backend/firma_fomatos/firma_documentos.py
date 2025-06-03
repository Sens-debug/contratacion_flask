from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm #manejar las unidades de tamaño
import datetime
import os

class Firma_documentos():
    def __init__(self,
                 nombre_completo,direccion_residencia,cedula_ciudadania,
                 correo_electronico,telefono,area,cargo,tipo_sangre,fecha_nacimiento, ruta_carpeta_persona,
                 ruta_firma):
        self.ruta_carpeta_persona = ruta_carpeta_persona
        self.datos_a_diligenciar ={
        'nombre_completo': nombre_completo,
        'direccion_residencia':direccion_residencia,
        'cedula_ciudadania':cedula_ciudadania,
        'correo_electronico':correo_electronico,
        'cargo': cargo,
        'area': area,
        'tipo_sangre':tipo_sangre,
        'fecha_nacimiento':fecha_nacimiento,
        'fecha_actual':f"{datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}",
        'telefono':telefono,
        'fecha_dia':datetime.datetime.now().day,
        'fecha_mes':datetime.datetime.now().month,
        'fecha_año':datetime.datetime.now().year,
        'firma': None
        }
        self.ruta_firma = os.path.abspath(ruta_firma)
        #obtiene la ruta del script, el cual debe compartir carpeta con la carpeta contenedora de los formatos
        ruta_script=__file__
        self.ruta_carpetas_plantillas = os.path.join(os.path.dirname(ruta_script),'Plantillas')

    def firmar_formatos_administrativo(self):
    #     # ruta_firma = r"C:\Users\Sistemas\Desktop\try_contratacion\backend\firma_fomatos\firma_prueba.jpg"
    #     ruta_carpeta_plantilla_administrativos=os.path.join(self.ruta_carpetas_plantillas,"Plantillas_administrativo")


    #     #LLena el array con el contenido de la carpeta en la ruta absoluta asignada, siempre y cuando sea un archivo finalizado en .docx
    #     #Sintaxis contiene salto de linea
    #     archivos_administrativos = [i for i in os.listdir(ruta_carpeta_plantilla_administrativos) 
    #                                 if os.path.isfile(os.path.join(ruta_carpeta_plantilla_administrativos,i)) 
    #                                 and i.endswith('.docx')]
    #     listado_formatos = []
    #     for i in archivos_administrativos:
    #         ruta_formato = os.path.join(ruta_carpeta_plantilla_administrativos,i)
    #         # Aplicamos string slicing para eliminar los ultimos 5 caracteres(.docx)
    #         nombre_archivo = os.path.basename(ruta_formato)[:-5]
            
    #         '''Valido solo en windows
    #          nombre_archivo=ruta_formato.split("\\")
    #          print(nombre_archivo[-1])
    #         '''

           
    #         documento_plantilla = DocxTemplate(ruta_formato)
            
    #         # listado_formatos.append({'formato':nombre_archivo,'documento_procesado':documento_plantilla})
            
    #         imagen_firma = InlineImage(documento_plantilla,ruta_firma, width=Mm(40))

    #         documento_plantilla.render(datos_a_diligenciar)
            
    #         # creamos la carpeta de la persona
    #         # os.makedirs(f"{self.ruta_almacenamiento}\\{datos_a_diligenciar['nombre_completo']}", exist_ok=True)
    #         documento_plantilla.save(fr'{self.ruta_carpeta_persona}\{nombre_archivo}_{datos_a_diligenciar["nombre_completo"]}_{datos_a_diligenciar["cedula_ciudadania"]}.docx')

    #     print(ruta_carpeta_plantilla_administrativos)
        pass


    def firmar_formatos_antibiotico(self):
        ruta_carpeta_plantilla_antibioticos= os.path.join(self.ruta_carpetas_plantillas, 'Plantillas_antibioticos')
        ruta_firma = fr"{os.path.join(os.path.dirname(__file__),'firma_prueba.jpg')}"
        print(ruta_firma)

        # List comprehension
        archivos_antibioticos = [i for i in os.listdir(ruta_carpeta_plantilla_antibioticos)
                                 if os.path.isfile(os.path.join(ruta_carpeta_plantilla_antibioticos,i))
                                 and i.endswith('.docx')]
        for i in archivos_antibioticos:
            ruta_formato = os.path.join(ruta_carpeta_plantilla_antibioticos,i)
            nombre_archivo = os.path.basename(ruta_formato)[:-5]
            documento_plantilla = DocxTemplate(ruta_formato)
            imagen_firma = InlineImage(documento_plantilla,self.ruta_firma, width=Mm(40), height=Mm(30))
            print(self.ruta_firma)
            self.datos_a_diligenciar["firma"] = imagen_firma
            documento_plantilla.render(self.datos_a_diligenciar)
            # os.makedirs(f"{self.ruta_carpetas_plantillas}\\Formatos_Firmados\\Antibiotico\\{self.datos_a_diligenciar['nombre_completo']}", exist_ok=True)
            documento_plantilla.save(fr'{self.ruta_carpeta_persona}\{nombre_archivo}_{self.datos_a_diligenciar["nombre_completo"]}_{self.datos_a_diligenciar["cedula_ciudadania"]}.docx')

        

# signer =Firma_documentos('','','','','','','','','','','','')
# signer.firmar_formatos_administrativo()
# signer.firmar_formatos_antibiotico()
