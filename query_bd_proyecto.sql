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
                     
                     