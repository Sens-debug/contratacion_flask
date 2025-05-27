create table cargos (id int AUTO_INCREMENT PRIMARY KEY,
                    Cargo varchar(40)
                    );

create table estados(id int AUTO_INCREMENT PRIMARY Key,
                    estado varchar(10));

create table usuarios (id int AUTO_INCREMENT PRIMARY KEY,
                     primer_nombre varchar(20)not null,
                     segundo_nombre varchar(20),
                     primer_apellido varchar(20) not null,
                     segundo_apellido varchar(20) not null,
                     correo varchar(70),
                     telefono varchar(20),
                     nombre_usuario varchar(30),
                     contraseña_usuario varchar(10),
                     cargo_id int,
                     FOREIGN Key (cargo_id) references cargos(id)
                      );
create table documentos(id INT AUTO_INCREMENT PRIMARY KEY,
                       documento varchar(70)
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
 


INSERT INTO `estados` (`id`, `estado`) VALUES (NULL, 'sel'), (NULL, 'contra'), (NULL, 'cancel');



INSERT INTO `cargos` (`id`, `Cargo`) VALUES (NULL, 'antibiotico'), (NULL, 'cuidador'), (NULL, 'permanente'), (NULL, 'nutricion'), (NULL, 'medico'), (NULL, 'psicologia'),(NULL, 'auditor'), (NULL, 'fisio_terapia'), (NULL, 'terapia_respiratoria'), (NULL, 'terapia_ocupacional'), (NULL, 'administrativo');

