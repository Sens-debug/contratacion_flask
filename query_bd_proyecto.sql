create table cargos (id int  PRIMARY KEY,
                    Cargo varchar(40)
                    );

create table estados(id int  PRIMARY Key,
                    estado varchar(20)
                    );

create table areas(id int PRIMARY Key,
                    area  varchar(40)
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
                     tipo_sangre_id int,
                     telefono varchar(20),
                     ruta_firma varchar(400),
                     nombre_usuario varchar(50),
                     contraseña_usuario varchar(50),
                     fecha_nacimiento DATE,
                     estado_firma int,
                     FOREIGN Key (cargo_id) references cargos(id),
                     Foreign Key (tipo_sangre_id) references tipos_sangre(id)
                      );

create table documentos(id INT  PRIMARY KEY,
                       documento varchar(100)
                       );           

create table cargosxarea (cargo_id int,
                            area_id int,
                            FOREIGN KEY (cargo_id) references cargos(id),
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
 


INSERT INTO cargos (id, Cargo) VALUES (1, 'Antibiotico'), (2, 'Cuidador'), (3, 'Permanente'),(4,'AuditorContratacion');

INSERT INTO estados (id, estado) VALUES (1, 'seleccion'), (2, 'contratacion'), (3, 'cancelado'), (4, 'completado');

INSERT INTO areas (id,area) VALUES (1,'Administrativo'), (2, 'Asistencial');

INSERT INTO tipos_sangre (id,tipo) VALUES (1, '0-'),(2, '0+'),(3, 'A-'),(4, 'A+'),(5, 'B-'),(6, 'B+'),(7, 'AB-'),(8, 'AB+');

INSERT INTO cargosxarea (cargo_id,area_id) VALUES (1,2),(2,2),(3,2),(4,1);

INSERT INTO documentos (id,documento) VALUES (1,'Hoja_Vida_Firmada_Con_Foto'),(2,'Doc_Identidad_150%'),(3,'Postulacion_Al_Cargo'),(4,'Formato_Entrevista-Prueba_Seleccion'),
(5,'Certificado_Estudio'),(6,'Convalidacion_Ministerio_Edcucacion(Educacion_Exterior)'),(7,'Registro_RETHUS'),(8,'Certificado_Etica_Medica'),
(9,'Carnet_Vacunacion(Hep_B-Tetanos-Difteria-Influenza-Covid)'),(10,'Certificado_Poliza_Responsabilidad_Civil'),(11,'Certificado_Laboral'),
(12,'Certificado_Afiliacion_EPS-AFP-CESANTIAS'),(13,'Documento_Beneficiario_EPS-CCF'),(14,'RUT'),(15,'Licencia_Conduccion_Vigente'),(16,'Tarjeta_Propiedad_Vehiculo'),
(17,'Soat_Vigente'),(18,'TecnicoMecanica_vigente'),(19,'Seguro_Vehiculo'),(20,'Certificado_Policia-Contraloria-Procuraduria-Antecedentes_Medidas_Correctivas'),
(21,'Curso_RCP'),(22,'Certificado_Atencion_Victimas_Violencia_Sexual'),(23,'Certificado_Curso_Humanizacion'),(24,'Certificado_Curso_Atencion_Victimas_Con_Agentes_Quimicos'),
(25,'Certificado_Administracion_Medicamentos'),(26,'Certificado_Salud_Mental'),(27,'Certificado_Manejo_Duelo'),(28,'Certificado_En_Vacunacion'),(29,'Certificado_Codigo_Rojo'),
(30,'Certificado_Toma_Muestras_Laboratorio_Clinico'),(31,'Certificado_POCT(Pruebas_Punto_Atencion)'),(32,'Certificado_Primeros_Auxilios'),
(33,'Certificacion_Cuenta_Bancaria'),(34,'Firma');


INSERT INTO documentosxcargoxestado (cargo_id,documento_id,estado_id) VALUES 

(1,1,1),(1,2,1),(1,5,1),(1,12,1),(2,1,1),(2,2,1),(2,5,1),(2,12,1),(3,1,1),(3,2,1),(3,5,1),(3,12,1),

(1,1,2),(1,2,2),(1,3,2),(1,4,2),(1,5,2),(1,6,2),(1,7,2),(1,9,2),(1,10,2),(1,11,2),(1,12,2),(1,13,2),(1,14,2),(1,15,2),(1,16,2),(1,17,2),(1,18,2),(1,19,2),(1,20,2),(1,21,2),(1,22,2),
(1,23,2),(1,25,2),(1,26,2),(1,27,2),(1,28,2),(1,29,2),(1,32,2),(1,33,2),(1,34,2),

(2,1,2),(2,2,2),(2,3,2),(2,4,2),(2,5,2),(2,6,2),(2,7,2),(2,9,2),(2,10,2),(2,11,2),(2,12,2),(2,13,2),(2,14,2),(2,15,2),(2,20,2),(2,21,2),(2,22,2),(2,23,2),(2,20,2),
(2,21,2),(2,22,2),(2,23,2),(2,24,2),(2,26,2),(2,27,2),(2,28,2),(2,29,2),(2,32,2),(2,33,2),(2,34,2),

(3,1,2),(3,2,2),(3,3,2),(3,4,2),(3,5,2),(3,6,2),(3,7,2),(3,9,2),(3,10,2),(3,11,2),(3,12,2),(3,13,2),(3,14,2),(3,20,2),(3,21,2),(3,22,2),(3,23,2),(3,24,2),(3,25,2),
(3,26,2),(3,27,2),(3,28,2),(3,29,2),(3,30,2),(3,31,2),(3,32,2),(3,33,2),(3,34,2);


INSERT INTO usuarios(id,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,direccion_residencia,cedula_ciudadania,
correo_electronico,cargo_id,tipo_sangre_id,telefono,ruta_firma,nombre_usuario,contraseña_usuario,fecha_nacimiento,estado_firma) 
VALUES (NULL, 'Juan', 'Miguel', ' XD','XD','XXX#XXX/XX','287449','ips@ipstid.com',1,1,'telefono_imaginario',NULL,'JM','1',NULL,0);

INSERT INTO usuariosxestado (id_usuario,estado_id) VALUES (1,1)

