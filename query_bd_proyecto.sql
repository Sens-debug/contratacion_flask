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
 

create table metadatos_aceptacionxusuario(id int primary key auto_increment,
                                            fecha_aceptacion DATE,
                                            direccion_ip varchar(50),
                                            navegador varchar(100),
                                            usuario_id int,
                                            Foreign Key (usuario_id) references usuarios (id)
                                            );

INSERT INTO cargos (id, Cargo) VALUES (1, 'Antibiotico'), (2, 'Cuidador'), (3, 'Permanente'),(4,'AuditorContratacion'),(5,'Nutricionista'),
(6,'Psicologo'),(7,'Terapeuta Fisico'),(8,'Terapeuta ocupacional'),(9,'Terapeuta Respiratorio'),(10,'Fonoaudiolgo'),(11,'Medico General');

INSERT INTO estados (id, estado) VALUES (1, 'seleccion'), (2, 'contratacion'), (3, 'cancelado'), (4, 'completado'),(5,"contratado");

INSERT INTO areas (id,area) VALUES (1,'Administrativo'), (2, 'Asistencial');

INSERT INTO tipos_sangre (id,tipo) VALUES (1, '0-'),(2, '0+'),(3, 'A-'),(4, 'A+'),(5, 'B-'),(6, 'B+'),(7, 'AB-'),(8, 'AB+');

INSERT INTO cargosxarea (cargo_id,area_id) VALUES (1,2),(2,2),(3,2),(5,2),(6,2),(7,2),(8,2),(9,2),(10,2),(11,2),
(4,1);

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

(1,1,1),(1,2,1),(1,5,1),(1,12,1),
(2,1,1),(2,2,1),(2,5,1),(2,12,1),
(3,1,1),(3,2,1),(3,5,1),(3,12,1),
(4,1,1),(4,2,1),(4,5,1),(4,12,1),
(5,1,1),(5,2,1),(5,5,1),(5,12,1),
(6,1,1),(6,2,1),(6,5,1),(6,12,1),
(7,1,1),(7,2,1),(7,5,1),(7,12,1),
(8,1,1),(8,2,1),(8,5,1),(8,12,1),
(9,1,1),(9,2,1),(9,5,1),(9,12,1),
(10,1,1),(10,2,1),(10,5,1),(10,12,1),
(11,1,1),(11,2,1),(11,5,1),(11,12,1),


(1,1,2),(1,2,2),(1,3,2),(1,4,2),(1,5,2),(1,6,2),(1,7,2),(1,9,2),(1,10,2),(1,11,2),(1,12,2),(1,13,2),(1,14,2),(1,15,2),(1,16,2),(1,17,2),(1,18,2),(1,19,2),(1,20,2),(1,21,2),(1,22,2),
(1,23,2),(1,25,2),(1,26,2),(1,27,2),(1,28,2),(1,29,2),(1,32,2),(1,33,2),(1,34,2),

(2,1,2),(2,2,2),(2,3,2),(2,4,2),(2,5,2),(2,6,2),(2,7,2),(2,9,2),(2,10,2),(2,11,2),(2,12,2),(2,13,2),(2,14,2),(2,15,2),(2,20,2),(2,21,2),(2,22,2),(2,23,2),(2,20,2),
(2,21,2),(2,22,2),(2,23,2),(2,24,2),(2,26,2),(2,27,2),(2,28,2),(2,29,2),(2,32,2),(2,33,2),(2,34,2),

(3,1,2),(3,2,2),(3,3,2),(3,4,2),(3,5,2),(3,6,2),(3,7,2),(3,9,2),(3,10,2),(3,11,2),(3,12,2),(3,13,2),(3,14,2),(3,20,2),(3,21,2),(3,22,2),(3,23,2),(3,24,2),(3,25,2),
(3,26,2),(3,27,2),(3,28,2),(3,29,2),(3,30,2),(3,31,2),(3,32,2),(3,33,2),(3,34,2),

(5,1,2),(5,2,2),(5,3,2),(5,4,2),(5,5,2),(5,6,2),(5,7,2),(5,9,2),(5,10,2),(5,11,2),(5,12,2),(5,13,2),(5,14,2),(5,15,2),(5,16,2),(5,17,2),(5,18,2),(5,19,2),(5,20,2),(5,21,2),(5,22,2),
(5,23,2),(5,25,2),(5,26,2),(5,27,2),(5,28,2),(5,29,2),(5,32,2),(5,33,2),(5,34,2),

(6,1,2),(6,2,2),(6,3,2),(6,4,2),(6,5,2),(6,6,2),(6,7,2),(6,9,2),(6,10,2),(6,11,2),(6,12,2),(6,13,2),(6,14,2),(6,15,2),(6,16,2),(6,17,2),(6,18,2),(6,19,2),(6,20,2),(6,21,2),(6,22,2),
(6,23,2),(6,25,2),(6,26,2),(6,27,2),(6,28,2),(6,29,2),(6,32,2),(6,33,2),(6,34,2),

(7,1,2),(7,2,2),(7,3,2),(7,4,2),(7,5,2),(7,6,2),(7,7,2),(7,9,2),(7,10,2),(7,11,2),(7,12,2),(7,13,2),(7,14,2),(7,15,2),(7,16,2),(7,17,2),(7,18,2),(7,19,2),(7,20,2),(7,21,2),(7,22,2),
(7,23,2),(7,25,2),(7,26,2),(7,27,2),(7,28,2),(7,29,2),(7,32,2),(7,33,2),(7,34,2),

(8,1,2),(8,2,2),(8,3,2),(8,4,2),(8,5,2),(8,6,2),(8,7,2),(8,9,2),(8,10,2),(8,11,2),(8,12,2),(8,13,2),(8,14,2),(8,15,2),(8,16,2),(8,17,2),(8,18,2),(8,19,2),(8,20,2),(8,21,2),(8,22,2),
(8,23,2),(8,25,2),(8,26,2),(8,27,2),(8,28,2),(8,29,2),(8,32,2),(8,33,2),(8,34,2),

(9,1,2),(9,2,2),(9,3,2),(9,4,2),(9,5,2),(9,6,2),(9,7,2),(9,9,2),(9,10,2),(9,11,2),(9,12,2),(9,13,2),(9,14,2),(9,15,2),(9,16,2),(9,17,2),(9,18,2),(9,19,2),(9,20,2),(9,21,2),(9,22,2),
(9,23,2),(9,25,2),(9,26,2),(9,27,2),(9,28,2),(9,29,2),(9,32,2),(9,33,2),(9,34,2),

(10,1,2),(10,2,2),(10,3,2),(10,4,2),(10,5,2),(10,6,2),(10,7,2),(10,9,2),(10,10,2),(10,11,2),(10,12,2),(10,13,2),(10,14,2),(10,15,2),(10,16,2),(10,17,2),(10,18,2),(10,19,2),(10,20,2),(10,21,2),(10,22,2),
(10,23,2),(10,25,2),(10,26,2),(10,27,2),(10,28,2),(10,29,2),(10,32,2),(10,33,2),(10,34,2),

(11,1,2),(11,2,2),(11,3,2),(11,4,2),(11,5,2),(11,6,2),(11,7,2),(11,8,2),(11,9,2),(11,10,2),(11,11,2),(11,12,2),(11,13,2),(11,14,2),(11,15,2),(11,16,2),(11,17,2),(11,18,2),(11,19,2),(11,20,2),(11,21,2),(11,22,2),
(11,23,2),(11,25,2),(11,26,2),(11,27,2),(11,28,2),(11,29,2),(11,32,2),(11,33,2),(11,34,2);


INSERT INTO usuarios(id,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,direccion_residencia,cedula_ciudadania,
correo_electronico,cargo_id,tipo_sangre_id,telefono,ruta_firma,nombre_usuario,contraseña_usuario,fecha_nacimiento,estado_firma) 
VALUES (NULL, 'Fabian', NULL, 'Marquez', 'TID', 'cl 88 # 99-33', '5558796', 'ipstid@ipstid.com', '4', '2', '35500088', NULL, 'Fabi', '0', NULL, NULL);



