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
                            Foreign Key (estado_id) references estados(id));
 


INSERT INTO `estados` (`id`, `estado`) VALUES (NULL, 'sel'), (NULL, 'contra'), (NULL, 'cancel');

INSERT INTO documentos (id, documento) VALUES (NULL, 'Hoja_de_Vida_firmada_y_con_foto'), (NULL, 'Fotocopia_CC_150%'), (NULL, 'Postulacion_al_cargo'), (NULL, 'Formato_entrevista-Pruebas_seleccion'), (NULL, 'Fotocopia_certificado_estudio'),(NULL,'Convalidacion_expedida_por_el_ministerio_educacion'), (NULL, 'Resolucion_y_registro_RETHUS'), (NULL, 'Fotocopia_certificado_etica_medica'), (NULL, 'carnet_vacunacion_HepatitisB,Tetanos,Difteria,Influenza,Covid'), (NULL, 'Fotocopia_certificado_poliza_responsibilidad_civil'), (NULL, 'Certificaciones_laborales'), (NULL, 'Certificado_afiliacion_EPS,AFP,CESATIAS'), (NULL, 'Documentos_beneficiarios EPS-CCF'), (NULL, 'RUT'), (NULL, 'Licencia_conduccion_vigente'), (NULL, 'Tarjeta_propiedad_vehiculo'), (NULL, 'Soat_vigente'), (NULL, 'Tecnicomecanica'), (NULL, 'Seguro_del_vehiculo'), (NULL, 'Certificado_policia,contraloria,procuraduria,antecedentes_medidas_correctivas'), (NULL, 'Curso_RCP'),(null,'Certificado_de_atencion_a_victimas_de_violencia_sexual'),(NULL,'Certificado_curso_humanizacion'), (NULL, 'Certificado_atencion_victimas_con_agentes_quimicos'), (NULL, 'Certificado_administracion_medicamentos'), (NULL, 'Certificado_en_salud_mental'), (NULL, 'certificado_en_manejo_de_duelo'), (NULL, 'certificado_en_vacunacion'), (NULL, 'certificado_en_codigo_rojo'), (NULL, 'certificado_de_toma_de_muestras_de_laboratorio_clinico'), (NULL, 'Certificado_POCT-Pruebas_en_el_punto_de_atencion-'), (NULL, 'Certificado_primeros_auxilios'), (NULL, 'Firma'),();

INSERT INTO `cargos` (`id`, `Cargo`) VALUES (NULL, 'antibiotico'), (NULL, 'cuidador'), (NULL, 'permanente'), (NULL, 'nutricion'), (NULL, 'medico'), (NULL, 'psicologia'), (NULL, 'fisio_terapia'), (NULL, 'terapia_respiratoria'), (NULL, 'terapia_ocupacional'), (NULL, 'administrativo');

-- Insercion antibiotico
INSERT INTO `documentosxcargoxestado` (`cargo_id`, `documento_id`, `estado_id`) VALUES ('1', '1', '1'), ('1', '2', '1'), ('1', '3', '1'), ('1', '4', '1'), ('1', '5', '1'), ('1', '6', '1'), ('1', '8', '1'), ('1', '9', '1'), ('1', '10', '1'), ('1', '11', '1'), ('1', '12', '1'), ('1', '13', '1'), ('1', '14', '1'), ('1', '15', '1'), ('1', '16', '1'), ('1', '17', '1'), ('1', '18', '1'), ('1', '19', '1'), ('1', '23', '1'), ('1', '24', '1'), ('1', '25', '1'), ('1', '26', '1'), ('1', '29', '1'), ('1', '30', '2')
;