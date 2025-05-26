create table cargos (id int AUTO_INCREMENT PRIMARY KEY,
                    Cargo varchar(20)
                    );

create table usuarios (id int AUTO_INCREMENT PRIMARY KEY,
                     primer_nombre varchar(20)not null,
                     segundo_nombre varchar(20),
                     primer_apellido varchar(20) not null,
                     segundo_apellido varchar(20),
                     correo varchar(70),
                     telefono varchar(20),
                     nombre_usuario varchar(30),
                     contraseña_usuario varchar(10),
                     cargo_id int,
                     FOREIGN Key (cargo_id) references cargos(id)
                      );
create table documentos(id INT AUTO_INCREMENT PRIMARY KEY,
                       documento varchar(40)
                       );                      
                      
create table documentosxcargo(cargo_id INT,
                             documento_id int,
                             Foreign Key (cargo_id) REFERENCES cargos(id),
                             FOREIGN KEY (documento_id) REFERENCES documentos(id)
                             );
                     

INSERT INTO `documentos` (`id`, `documento`) VALUES (NULL, 'cedula_ciudadania'), (NULL, 'hoja_de_vida'), (NULL, 'carnet_vacunacion');
INSERT INTO `cargos` (`id`, `Cargo`) VALUES (NULL, 'Cuidador'), (NULL, 'Auxiliar_Enfermeria');
INSERT INTO `documentosxcargo` (`cargo_id`, `documento_id`) VALUES ('1', '1'), ('1', '2'), ('2', '1'), ('2', '2'), ('2', '3');
INSERT INTO `usuarios` (`id`, `primer_nombre`, `segundo_nombre`, `primer_apellido`, `segundo_apellido`, `correo`, `telefono`, `nombre_usuario`, `contraseña_usuario`, `cargo_id`) VALUES (NULL, 'Jose', NULL, 'Arbelaez', NULL, NULL, NULL, 'JA', '123', '1'), (NULL, 'Maria', NULL, 'Magdalena', NULL, NULL, NULL, 'MM', '321', '2');
