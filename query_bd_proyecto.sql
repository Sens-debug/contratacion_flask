create table cargos (id int AUTO_INCREMENT PRIMARY KEY,
                    Cargo varchar(40)
                    );

create table estados(id int AUTO_INCREMENT PRIMARY Key,
                    estado varchar(20)
                    );

create table areas(id int AUTO_INCREMENT PRIMARY Key,
                    area  varchar(40)
                    );

create table tipos_ingreso(id int AUTO_INCREMENT PRIMARY Key,
                            tipo varchar(50)
                            );           

create table tipos_sangre(id int AUTO_INCREMENT PRIMARY Key,
                            tipo varchar(20)
                            );      

create table usuarios (id int AUTO_INCREMENT PRIMARY KEY,
                     primer_nombre varchar(20)not null,
                     segundo_nombre varchar(20),
                     primer_apellido varchar(20) not null,
                     segundo_apellido varchar(20) not null,
                     numero_cedula varchar(30),
                     direccion varchar(100),
                     correo varchar(70),
                     telefono varchar(20),
                     nombre_usuario varchar(30),
                     contraseña_usuario varchar(10),
                     cargo_id int,
                     tipo_ingreso_id int,
                     tipo_sangre_id int,
                     FOREIGN Key (cargo_id) references cargos(id),
                     FOREIGN Key (tipo_ingreso_id) references tipos_ingreso(id),
                     Foreign Key (tipo_sangre_id) references tipos_sangre(id)
                      );

create table documentos(id INT AUTO_INCREMENT PRIMARY KEY,
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
 


INSERT INTO `estados` (`id`, `estado`) VALUES (NULL, 'seleccion'), (NULL, 'contratacion'), (NULL, 'cancelado'), (Null, 'completado');


INSERT INTO `cargos` (`id`, `Cargo`) VALUES (NULL, 'antibiotico'), (NULL, 'cuidador'), (NULL, 'permanente'), (NULL, 'nutricion'), (NULL, 'medico'), (NULL, 'psicologia'),(NULL, 'auditor'), (NULL, 'fisio_terapia'), (NULL, 'terapia_respiratoria'), (NULL, 'terapia_ocupacional'), (NULL, 'administrativo');

