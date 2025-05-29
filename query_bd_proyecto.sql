create table cargos (id int  PRIMARY KEY,
                    Cargo varchar(40)
                    );

create table estados(id int  PRIMARY Key,
                    estado varchar(20)
                    );

create table areas(id int PRIMARY Key,
                    area  varchar(40)
                    );

create table tipos_ingreso(id int PRIMARY Key,
                            tipo varchar(50)
                            );           

create table tipos_sangre(id int  PRIMARY Key,
                            tipo varchar(20)
                            );    


create table usuarios (id int AUTO_INCREMENT PRIMARY KEY,
                     primer_nombre varchar(20)not null,
                     segundo_nombre varchar(20),
                     primer_apellido varchar(20) not null,
                     segundo_apellido varchar(20) not null,
                     direccion_residencia varchar (100),
                     cedula_ciudadania varchar(20) not null,
                     correo_electronico varchar(70) not null,
                     cargo_id int,
                     tipos_sangre_id int,
                     telefono varchar(20),
                     ruta_firma varchar(400),
                     fecha_nacimiento DATE,
                     FOREIGN Key (cargo_id) references cargos(id),
                     FOREIGN Key (tipo_ingreso_id) references tipos_ingreso(id),
                     Foreign Key (tipo_sangre_id) references tipos_sangre(id)
                      );

create table documentos(id INT  PRIMARY KEY,
                       documento varchar(70)
                       );           

create table cargosxarea (cargo_id int,
                            area_id int,
                            FOREIGN KEY (cargo_id) references cargos(id)
                            FOREIGN KEY (area_id) references areas(id)
                            );           
                      
create table documentosxcargoxestado(cargo_id INT ,
                             documento_id int ,
                             estado_id int,
                             Foreign Key (cargo_id) REFERENCES cargos(id),
                             FOREIGN KEY (documento_id) REFERENCES documentos(id),
                             Foreign Key (estado_id) references estados(id)
                             );

create table usuariosxestado(id_usuario int ,
                            estado_id int ,
                            Foreign Key (id_usuario) references usuarios(id),
                            Foreign Key (estado_id) references estados(id)
                            );
 


INSERT INTO `estados` (`id`, `estado`) VALUES (1, 'seleccion'), (2, 'contratacion'), (3, 'cancelado'), (4, 'completado');


INSERT INTO `cargos` (`id`, `Cargo`) VALUES (1, 'Antibiotico'), (2, 'Cuidador'), (3, 'Permanente'), (4, 'Nutricion'), (5, 'Medico'), (6, 'Psicologia'),(7, 'Auditor'), (8, 'Fisio_terapia'),
 (9, 'Terapia_respiratoria'), (10, 'Terapia_ocupacional');

INSERT INTO 'areas' ('id','area') VALUES (1,'Administrativo'), (2, 'Asistencial');

INSERT INTO 'tipos_de_sangre' ('id','tipo') VALUES (1, '0-'),(2, '0+'),(3, 'A-'),(4, 'A+'),(5, 'B-'),(6, 'B+'),(7, 'AB-'),(8, 'AB+');

INSERT INTO 'cargosxarea' ('cargo_id','area_id') VALUES (7,1),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(8,2),(9,2),(10,2);

INSERT INTO 'documentos' ('id','docuemnto') VALUES (1,'Hoja_Vida_Firmada_Con_Foto'),(2,'Doc_Identidad_150%'),(3,'Postulacion_Al_Cargo'),(4,'Formato_Entrevista-Prueba_Seleccion'),
(5,'Certificado_Estudio'),(6,'Convalidacion_Ministerio_Edcucacion(Educacion_Exterior)'),(7,'Registro_RETHUS'),(8,'Certificado_Etica_Medica'),
(9,'Carnet_Vacunacion(Hep_B-Tetanos-Difteria-Influenza-Covid)'),(10,'Certificado_Poliza_Responsabilidad_Civil'),(11,'Certificado_Laboral'),
(12,'Certificado_Afiliacion_EPS-AFP-CESANTIAS'),(13,'Documento_Beneficiario_EPS-CCF'),(14,'RUT'),(15,'Licencia_Conduccion_Vigente'),(16,'Tarjeta_Propiedad_Vehiculo'),
(17,'Soat_Vigente'),(18,'TecnicoMecanica_vigente'),(19,'Seguro_Vehiculo'),(20,'Certificado_Policia-Contraloria-Procuraduria-Antecedentes_Medidas_Correctivas'),
(21,'Curso_RCP'),(22,'Certificado_Atencion_Victimas_Violencia_Sexual'),(23,'Certificado_Curso_Humanizacion'),(24,'Certificado_Curso_Atencion_Victimas_Con_Agentes_Quimicos'),
(25,'Certificado_Administracion_Medicamentos'),(26,'Certificado_Salud_Mental'),(27,'Certificado_Manejo_Duelo'),(28,'Certificado_En_Vacunacion'),(29,'Certificado_Codigo_Rojo'),
(30,'Certificado_Toma_Muestras_Laboratorio_Clinico'),(31,'Certificado_POCT(Pruebas_Punto_Atencion)'),(32,'Certificado_Primeros_Auxilios'),(33,'Certificacion_Cuenta_Bancaria');