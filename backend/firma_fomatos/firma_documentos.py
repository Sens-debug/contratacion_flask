from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm #manejar las unidades de tamaño
import datetime
import os

# doc = DocxTemplate(r"C:\Users\Sistemas\Desktop\try_contratacion\backend\firma_fomatos\plantilla_prueba.docx")

ruta_imagen = r"C:\Users\Sistemas\Desktop\try_contratacion\backend\firma_fomatos\firma_prueba.jpg"





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


class Firma_documentos():
    def __init__(self, primer_nombre,segundo_nombre,
                 primer_apellido,segundo_apellido,
                 nombre_completo,direccion_residencia,cedula_ciudadania,
                 correo_electronico,telefono,area,tipo_ingreso,tipo_sangre,
                 ruta_de_almacenamiento):
        
        self.nombre_completo=nombre_completo
        self.primer_nombre=primer_nombre
        self.segundo_nombre=segundo_nombre
        self.primer_apellido=primer_apellido
        self.segundo_apellido=segundo_apellido
        self.direccion_residencia=direccion_residencia
        self.cedula_ciudadania=cedula_ciudadania
        self.correo_electronico=correo_electronico
        self.telefono=telefono
        self.area=area
        self.tipo_ingreso=tipo_ingreso
        self.tipo_sangre=tipo_sangre
        

        #obtiene la ruta del script, el cual debe compartir carpeta con la carpeta contenedora de los formatos
        ruta_script=__file__
        self.ruta_carpetas_plantillas = os.path.join(os.path.dirname(ruta_script),'Plantillas')
        self.ruta_almacenamiento = ruta_de_almacenamiento

    def firmar_formatos_administrativo(self):
        ruta_firma = r"C:\Users\Sistemas\Desktop\try_contratacion\backend\firma_fomatos\firma_prueba.jpg"
        ruta_carpeta_plantilla_administrativos=os.path.join(self.ruta_carpetas_plantillas,"Plantillas_administrativo")


        #LLena el array con el contenido de la carpeta en la ruta absoluta asignada, siempre y cuando sea un archivo finalizado en .docx
        #Sintaxis contiene salto de linea
        archivos_administrativos = [i for i in os.listdir(ruta_carpeta_plantilla_administrativos) 
                                    if os.path.isfile(os.path.join(ruta_carpeta_plantilla_administrativos,i)) 
                                    and i.endswith('.docx')]
        listado_formatos = []
        for i in archivos_administrativos:
            ruta_formato = os.path.join(ruta_carpeta_plantilla_administrativos,i)
            # Aplicamos string slicing para eliminar los ultimos 5 caracteres(.docx)
            nombre_archivo = os.path.basename(ruta_formato)[:-5]
            
            '''Valido solo en windows
             nombre_archivo=ruta_formato.split("\\")
             print(nombre_archivo[-1])
            '''

            print(nombre_archivo)
            documento_plantilla = DocxTemplate(ruta_formato)
            
            # listado_formatos.append({'formato':nombre_archivo,'documento_procesado':documento_plantilla})
            
            imagen_firma = InlineImage(documento_plantilla,ruta_firma, width=Mm(40))
            datos_a_diligenciar ={
            'primer_nombre':'Juan',
            'segundo_nombre':'Miguel',
            'primer_apellido':'Ecele',
            'segundo_apellido':'Gutierrez',
            'nombre_completo': self.nombre_completo,
            'direccion_residencia':'cl 777 # 888 9876',
            'cedula_ciudadania':self.cedula_ciudadania,
            'correo_electronico':self.correo_electronico,
            'cargo': 'Sistemas',
            'area': 'Administrativa',
            'tipo_sangre':'AB+',
            'fecha_nacimiento':'1879/12/12',
            'fecha_actual':f"{datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}",
            'telefono':'32300009800',
            'fecha_dia':datetime.datetime.now().day,
            'fecha_mes':datetime.datetime.now().month,
            'fecha_año':datetime.datetime.now().year,
            'firma': imagen_firma
        }
            documento_plantilla.render(datos_a_diligenciar)
            
            # creamos la carpeta de la persona
            # os.makedirs(f"{self.ruta_almacenamiento}\\{datos_a_diligenciar['nombre_completo']}", exist_ok=True)
            documento_plantilla.save(f'{self.ruta_almacenamiento}\\{nombre_archivo}_{datos_a_diligenciar["nombre_completo"]}_{datos_a_diligenciar["cedula_ciudadania"]}.docx')

        print(ruta_carpeta_plantilla_administrativos)


    def firmar_formatos_antibiotico(self):
        ruta_carpeta_plantilla_antibioticos= os.path.join(self.ruta_carpetas_plantillas, 'Plantillas_antibioticos')
        ruta_firma = r"C:\Users\Sistemas\Desktop\try_contratacion\backend\firma_fomatos\firma_prueba.jpg"

        # List comprehension
        archivos_antibioticos = [i for i in os.listdir(ruta_carpeta_plantilla_antibioticos)
                                 if os.path.isfile(os.path.join(ruta_carpeta_plantilla_antibioticos,i))
                                 and i.endswith('.docx')]
        for i in archivos_antibioticos:
            ruta_formato = os.path.join(ruta_carpeta_plantilla_antibioticos,i)
            nombre_archivo = os.path.basename(ruta_formato)[:-5]
            documento_plantilla = DocxTemplate(ruta_formato)
            imagen_firma = InlineImage(documento_plantilla,ruta_firma, width=Mm(40))
            print(nombre_archivo)
            datos_a_diligenciar ={
            'primer_nombre':'Juan',
            'segundo_nombre':'Miguel',
            'primer_apellido':'Ecele',
            'segundo_apellido':'Gutierrez',
            'nombre_completo': 'Juan Maicol ',
            'direccion_residencia':'cl 777 # 888 9876',
            'cedula_ciudadania':'0987654321',
            'correo_electronico':'icfne@inc.com',
            'cargo': 'Antibiotico',
            'area': 'Administrativa',
            'tipo_sangre':'AB+',
            'fecha_nacimiento':'1879/12/12',
            'fecha_actual':f"{datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}",
            'telefono':'32300009800',
            'fecha_dia':datetime.datetime.now().day,
            'fecha_mes':datetime.datetime.now().month,
            'fecha_año':datetime.datetime.now().year,
            'firma': imagen_firma
        }
            documento_plantilla.render(datos_a_diligenciar)
            os.makedirs(f"{self.ruta_carpetas_plantillas}\\Formatos_Firmados\\Antibiotico\\{datos_a_diligenciar['nombre_completo']}", exist_ok=True)
            documento_plantilla.save(f'{self.ruta_carpetas_plantillas}\\Formatos_Firmados\\Antibiotico\\{nombre_archivo}_{datos_a_diligenciar["nombre_completo"]}_{datos_a_diligenciar["cedula_ciudadania"]}.docx')

        

# signer =Firma_documentos('','','','','','','','','','','','')
# signer.firmar_formatos_administrativo()
# signer.firmar_formatos_antibiotico()
