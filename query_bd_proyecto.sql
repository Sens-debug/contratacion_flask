create table usuarios(id int AUTO_INCREMENT PRIMARY KEY,
                     primer_nombre varchar(20)not null,
                     segundo_nombre varchar(20),
                     primer_apellido varchar(20) not null,
                     segundo_apellido varchar(20),
                     correo varchar(70),
                     telefono varchar(20),
                     nombre_usuario varchar(30),
                     contraseña_usuario varchar(10)
                    );
                      

create TABLE Permanentes(id int PRIMARY KEY ,
                     ruta_cc MEDIUMTEXT,
                     ruta_hv MEDIUMTEXT,
                         FOREIGN KEY (id) REFERENCES usuarios(id)
                     )

          