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
        fecha_actual = datetime.datetime.now()
        fechas =[fecha_actual.day,fecha_actual.month,fecha_actual.year]
        self.datos_a_diligenciar ={
        'nombre_completo': nombre_completo,
        'direccion_residencia':direccion_residencia,
        'cedula_ciudadania':cedula_ciudadania,
        'correo_electronico':correo_electronico,
        'cargo': cargo,
        'area': area,
        'tipo_sangre':tipo_sangre,
        'fecha_nacimiento':fecha_nacimiento,
        'fecha_actual':f"{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day}",
        'telefono':telefono,
        'fecha_dia':fechas[0],
        'fecha_mes':fechas[1],
        'fecha_año':fechas[2],
        'fecha_final_contrato':str(datetime.timedelta(days=365)+datetime.datetime(day=fechas[0],month=fechas[1],year=fechas[2]))[0:-9],
        'fecha_final_contrato_6meses':str(datetime.timedelta(days=183)+datetime.datetime(day=fechas[0],month=fechas[1],year=fechas[2]))[0:-9],
        'firma': None
        }
        self.ruta_firma = os.path.abspath(ruta_firma)
        #obtiene la ruta del script, el cual debe compartir carpeta con la carpeta contenedora de los formatos
        ruta_script=__file__
        self.ruta_carpetas_plantillas = os.path.join(os.path.dirname(ruta_script),'Plantillas')

    def firmar_formatos_administrativo(self):
        ruta_carpeta_plantilla_administrativos=os.path.join(self.ruta_carpetas_plantillas,"Plantillas_administrativo")


        #LLena el array con el contenido de la carpeta en la ruta absoluta asignada, siempre y cuando sea un archivo finalizado en .docx
        #Sintaxis contiene salto de linea
        archivos_administrativos = [i for i in os.listdir(ruta_carpeta_plantilla_administrativos) 
                                    if os.path.isfile(os.path.join(ruta_carpeta_plantilla_administrativos,i)) 
                                    and i.endswith('.docx')]
        for i in archivos_administrativos:
            ruta_formato = os.path.join(ruta_carpeta_plantilla_administrativos,i)
            # Aplicamos string slicing para eliminar los ultimos 5 caracteres(.docx)
            nombre_archivo = os.path.basename(ruta_formato)[:-5]
            
            '''Valido solo en windows
             nombre_archivo=ruta_formato.split("\\")
             print(nombre_archivo[-1])
            '''
            documento_plantilla = DocxTemplate(ruta_formato)
            
            # listado_formatos.append({'formato':nombre_archivo,'documento_procesado':documento_plantilla})
            
            imagen_firma = InlineImage(documento_plantilla,self.ruta_firma, width=Mm(40))

            documento_plantilla.render(self.datos_a_diligenciar)
            
            # creamos la carpeta de la persona
            # os.makedirs(f"{self.ruta_almacenamiento}\\{self.datos_a_diligenciar['nombre_completo']}", exist_ok=True)
            documento_plantilla.save(fr'{self.ruta_carpeta_persona}\{nombre_archivo}.docx')

        print(ruta_carpeta_plantilla_administrativos)
        
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
            documento_plantilla.save(fr'{self.ruta_carpeta_persona}\{nombre_archivo}.docx')

    def firmar_formatos_cuidador(self):
        ruta_carpeta_plantilla_cuidador= os.path.join(self.ruta_carpetas_plantillas, 'Plantillas_cuidador')
        ruta_firma = fr"{os.path.join(os.path.dirname(__file__),'firma_prueba.jpg')}"
        print(ruta_firma)

        # List comprehension
        archivos_cuidador = [i for i in os.listdir(ruta_carpeta_plantilla_cuidador)
                                 if os.path.isfile(os.path.join(ruta_carpeta_plantilla_cuidador,i))
                                 and i.endswith('.docx')]
        for i in archivos_cuidador:
            ruta_formato = os.path.join(ruta_carpeta_plantilla_cuidador,i)
            nombre_archivo = os.path.basename(ruta_formato)[:-5]
            documento_plantilla = DocxTemplate(ruta_formato)
            imagen_firma = InlineImage(documento_plantilla,self.ruta_firma, width=Mm(40), height=Mm(30))
            print(self.ruta_firma)
            self.datos_a_diligenciar["firma"] = imagen_firma
            documento_plantilla.render(self.datos_a_diligenciar)
            documento_plantilla.save(fr'{self.ruta_carpeta_persona}\{nombre_archivo}.docx')

    def firmar_formatos_permanentes(self):
        ruta_carpeta_plantilla_cuidador= os.path.join(self.ruta_carpetas_plantillas, 'Plantillas_permanente')

        # List comprehension
        archivos_cuidador = [i for i in os.listdir(ruta_carpeta_plantilla_cuidador)
                                 if os.path.isfile(os.path.join(ruta_carpeta_plantilla_cuidador,i))
                                 and i.endswith('.docx')]
        for i in archivos_cuidador:
            ruta_formato = os.path.join(ruta_carpeta_plantilla_cuidador,i)
            nombre_archivo = os.path.basename(ruta_formato)[:-5]
            documento_plantilla = DocxTemplate(ruta_formato)
            imagen_firma = InlineImage(documento_plantilla,self.ruta_firma, width=Mm(40), height=Mm(30))
            print(self.ruta_firma)
            self.datos_a_diligenciar["firma"] = imagen_firma
            documento_plantilla.render(self.datos_a_diligenciar)
            documento_plantilla.save(fr'{self.ruta_carpeta_persona}\{nombre_archivo}.docx')

    def firmar_formatos_profesionales(self):
        ruta_carpeta_plantilla_cuidador= os.path.join(self.ruta_carpetas_plantillas, 'Plantillas_profesionales')

        # List comprehension
        archivos_cuidador = [i for i in os.listdir(ruta_carpeta_plantilla_cuidador)
                                 if os.path.isfile(os.path.join(ruta_carpeta_plantilla_cuidador,i))
                                 and i.endswith('.docx')]
        for i in archivos_cuidador:
            ruta_formato = os.path.join(ruta_carpeta_plantilla_cuidador,i)
            nombre_archivo = os.path.basename(ruta_formato)[:-5]
            documento_plantilla = DocxTemplate(ruta_formato)
            imagen_firma = InlineImage(documento_plantilla,self.ruta_firma, width=Mm(40), height=Mm(30))
            print(self.ruta_firma)
            self.datos_a_diligenciar["firma"] = imagen_firma
            documento_plantilla.render(self.datos_a_diligenciar)
            documento_plantilla.save(fr'{self.ruta_carpeta_persona}\{nombre_archivo}.docx')


# signer =Firma_documentos('','','','','','','','','','','','')
# signer.firmar_formatos_administrativo()
# signer.firmar_formatos_antibiotico()
