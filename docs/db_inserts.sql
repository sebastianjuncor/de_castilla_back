/*-------------------------------------------------------------------------Desde aquí­ empiezan los registros-------------------------------------------------------------- */

INSERT INTO db_de_castilla.Permiso ( descripcion_Permiso, estado) VALUES
  ('Crear usuario', 1),
  ('Eliminar usuario', 1),
  ('Editar usuario', 1),
  ('Ver usuarios', 1),
  ('Crear rol', 1),
  ('Eliminar rol', 1),
  ('Editar rol', 1),
  ('Ver roles', 1),
  ('Crear producto', 1),
  ('Eliminar producto', 1),
  ('Modificar producto', 1),
  ('Ver productos', 1),
  ('Crear cliente', 1),
  ('Eliminar cliente', 1),
  ('Editar cliente', 1),
  ('Ver clientes', 1),
  ('Crear pedido', 1),
  ('Eliminar pedido', 1),
  ('Editar pedido', 1),
  ('Ver pedidos', 1),
  ('Gestionar proveedores', 1),
  ('Generar reportes', 1),
  ('Gestionar inventario de insumos', 1),
  ('Gestionar inventario de productos', 1),
  ('Realizar ventas', 1),
  ('Gestionar pedidos', 1),
  ('Gestionar empleados', 1),
  ('Gestionar clientes', 1),
  ('Gestionar roles de usuario', 1),
  ('Gestionar permisos', 1),
  ('Aprobar pedidos', 1),
  ('Cancelar pedidos', 1),
  ('Gestionar calificaciones de proveedores', 1),
  ('Gestionar calificaciones de pedidos', 1),
  ('Crear categorí­a', 1),
  ('Eliminar categorí­a', 1),
  ('Editar categorí­a', 1),
  ('Ver categorí­as', 1),
  ('Gestionar inventario de productos', 1),
  ('Gestionar inventario de insumos', 1);

INSERT INTO db_de_castilla.Sabor (nombre_Sabor, estado) VALUES
  ('Vainilla', 1),
  ('Chocolate', 1),
  ('Fresa', 1),
  ('Caramelo', 1),
  ('Limón', 1),
  ('Cafí©', 1),
  ('Naranja', 1),
  ('Menta', 1),
  ('Maracuya', 1),
  ('Mora', 1);

INSERT INTO db_de_castilla.Categoria (nombre_Categoria, descripcion_Categoria, estado) VALUES
  ('Obleas', 'Las obleas son pequeñas delicias crujientes, ideales para disfrutar en cualquier momento del dí­a. Ofrecemos una amplia selección de obleas  con diferentes ingredientes y sabores.',1),
  ('Cupcakes', 'Los cupcakes son pequeños pasteles individuales que se decoran con creatividad. Nuestra colección de cupcakes incluye sabores clásicos y combinaciones íºnicas que te encantarán.',1),
  ('Malteadas', 'En nuestra panaderí­a encontrarás una variedad de panes frescos y deliciosos, desde panes blancos y integrales hasta baguettes y bollos dulces.',1),
  ('Postres', 'La categorí­a de postres ofrece una selección de dulces exquisitos que te deleitarán. Desde mousses y flanes hasta postres con frutas frescas, aquí­ encontrarás algo para satisfacer tu antojo.',1),
  ('Tortas', 'Nuestras tartas son autí©nticas obras maestras de la reposterí­a. Disponemos de tartas clásicas como la de manzana y la de chocolate, así­ como creaciones íºnicas que te sorprenderán.',1),
  ('Dulces', 'Esta categorí­a está llena de dulces irresistibles, desde caramelos y chicles hasta chocolates y bombones. Si tienes un diente dulce, esta es la categorí­a perfecta para ti.',1),
  ('Bebidas', 'Acompaña tus postres con nuestras refrescantes bebidas. Ofrecemos una variedad de opciones, como batidos, jugos naturales y cafí©, para complementar tus delicias.',1),
  ('Helados', 'Nuestros helados son suaves, cremosos y están disponibles en una amplia gama de sabores. Ya sea que prefieras los clásicos como la vainilla y el chocolate, o sabores más extravagantes, aquí­ encontrarás el helado perfecto para ti.',1),
  ('Cheesecake', 'El cheesecake es un postre de queso cremoso y consistencia suave que se sirve sobre una base de galleta. Nuestros cheesecakes son simplemente deliciosos y están disponibles en una variedad de sabores y presentaciones.',1),
  ('waffles','waffles son crujientes por fuera y esponjosos por dentro, cubiertos con sabrosos toppings que van desde frutas frescas y crema batida hasta siropes dulces y indulgentes.',1);

INSERT INTO db_de_castilla.Proveedor (estado_Proveedor, empresa_Proveedor, nombre_Proveedor, correo_Proveedor, nit_Proveedor, celular_Proveedor, celular_respaldo_Proveedor, estado) VALUES
  (1, 'La carreta', 'Felipe Rodriguez', 'proveedora@example.com', '1234567890', 1234567890, NULL, 1),
  (1, 'Cream helado', 'Juan Junco', 'proveedorb@example.com', '0987654321', 9876543210, NULL, 1),
  (1, 'Alqueria', 'Bryan Mutis', 'proveedorc@example.com', '9876543210', 5678901234, NULL, 1),
  (1, 'Santillana', 'Camila Arias', 'proveedord@example.com', '5432109876', 4567890123, NULL, 1),
  (1, 'Oliverios', 'Marí­a Pardo', 'proveedore@example.com', '0123456789', 7890123456, NULL, 1),
  (1, 'Colombina', 'Daniel Girón', 'proveedorf@example.com', '6789012345', 2345678901, NULL, 1),
  (1, 'Obleas S.A', 'Cristian Beltran', 'proveedorg@example.com', '4567890123', 9012345678, NULL, 1),
  (1, 'Alpina', 'Kevin Calderon', 'proveedorh@example.com', '2345678901', 3456789012, NULL, 1),
  (1, 'Agrocampo ', 'Brayan Sanchez', 'proveedori@example.com', '9012345678', 6789012345, NULL, 1),
  (1, 'D1', 'Yeison Suarez', 'proveedorj@example.com', '7654321098', 0123456789, NULL, 1);

INSERT INTO db_de_castilla.Rol (nombre_Rol, estado) VALUES
  ('Administrador', 1),
  ('Usuario', 1),
  ('Empleado', 1);

INSERT INTO db_de_castilla.tipo_Movimiento (nombre_tipo_Movimiento, estado) VALUES
  ('Entrada', 1),
  ('Salida', 1);

INSERT INTO db_de_castilla.Estado_insumo (nombre_Estado_insumo, estado) VALUES
  ('No Caducado', 1),
  ('Caducado', 1);

INSERT INTO db_de_castilla.Insumo (nombre_Insumo, id_Estado_insumo, estado) VALUES
  ('Harina', 1, 1),
  ('Azíºcar', 1, 1),
  ('Mantequilla', 1, 1),
  ('Huevos', 1, 1),
  ('Leche', 1, 1),
  ('Vainilla', 1, 1),
  ('Helado', 1, 1),
  ('Fresas', 1, 1),
  ('Crema', 1, 1),
  ('Gelatina', 1, 1),
  ('Nueces', 1, 1),
  ('Canela', 1, 1),
  ('Arequipe', 1, 1),
  ('Levadura', 1, 1),
  ('Chips de Chocolate', 1, 1),
  ('oblea', 1, 1),
  ('Coco rallado', 1, 1),
  ('Galletas', 1, 1),
  ('Cafí© molido', 1, 1),
  ('Almendras', 2, 1);

INSERT INTO db_de_castilla.Producto (nombre_Producto, precio_Producto, imagen_Producto, id_Categoria_FK, estado) VALUES 
  ('Oblea especial', 4500, 'imagen1.jpg', 1, 1),
  ('Oblea con adicional', 3000, 'imagen2.jpg', 1, 1),
  ('Oblea sencilla', 2000, 'imagen3.jpg', 1, 1),
  ('Cupcake', 6000, 'imagen4.jpg', 2, 1),
  ('Malteada grande', 15000, 'imagen5.jpg', 3, 1),
  ('Malteada mediana', 12000, 'imagen5.jpg', 3, 1),
  ('Cheesecake', 6000, 'imagen6.jpg', 4, 1),
  ('Tres leches', 6000, 'imagen7.jpg', 4, 1),
  ('bandeja tres leches', 50000,'imagen8.jpg',4, 1),
  ('Merengon', 10000, 'imagen8.jpg', 4, 1),
  ('Torta de zanahoria', 4000, 'imagen9.jpg', 5, 1),
  ('Capuchino', 25000, 'imagen13.jpg', 7, 1),
  ('Tinto', 1500, 'imagen14.jpg', 7, 1),
  ('Mocaccino', 2500, 'imagen15.jpg', 7, 1),
  ('Helado sencillo', 2500, 'imagen16.jpg', 8, 1),
  ('Helado doble', 4500, 'imagen17.jpg', 8, 1),
  ('Helado triple', 6500, 'imagen18.jpg', 8, 1),
  ('Torta desemilla de amapola y naranja','4000', 'imagen18.jpg',5, 1),
  ('Torta de agras', '5000','imagen18.jpg',5, 1),
  ('Torta de chocolate', '4000','imagen18.jpg',5, 1),
  ('Torta de vainilla', '4000','imagen18.jpg',5, 1),
  ('Waffle sencillo', '11000','imagen18.jpg', 10, 1),
  ('Waffle especial con fruta', '14000','imagen18.jpg',10 , 1),
  ('Malteada pequeña', '10000','imagen18.jpg',3 , 1),
  ('Copa de helado con fruta', '10000', 'imagen18.jpg', 8, 1),
  ('Brownie con helado(con dos sabores de helado, 1)', '7000', 'imagen18.jpg',8, 1),
  ('Matrimonio', '6000','imagen18.jpg', 4, 1),
  ('Dulce de papayuela', '6000','imagen18.jpg', 6, 1),
  ('Leche asada', '7000', 'imagen18.jpg', 4, 1),
  ('Dulce tropical', '6000','imagen18.jpg', 6, 1),
  ('Flan de caramelo','6000', 'imagen18.jpg', 4, 1),
  ('Arroz con leche', '3000','imagen18.jpg', 4, 1),
  ('Brebas con arequipe', 6000 ,'imagen18.jpg', 6, 1);
  
INSERT INTO db_de_castilla.Rol_has_Permiso (id_Rol_FK, id_Permiso_FK, estado) VALUES
  (1, 1, 1),
  (1, 2, 1),
  (1, 3, 1),
  (1, 4, 1),
  (1, 5, 1),
  (1, 6, 1),
  (1, 7, 1),
  (1, 8, 1),
  (1, 9, 1),
  (1, 10, 1),
  (1, 11, 1),
  (1, 12, 1),
  (1, 13, 1),
  (1, 14, 1),
  (1, 15, 1),
  (1, 16, 1),
  (1, 17, 1),
  (1, 18, 1),
  (1, 19, 1),
  (1, 20, 1),
  (1, 21, 1),
  (1, 22, 1),
  (1, 23, 1),
  (1, 24, 1),
  (1, 25, 1),
  (1, 26, 1),
  (1, 27, 1),
  (1, 28, 1),
  (1, 29, 1),
  (1, 30, 1),
  (1, 31, 1),
  (1, 32, 1),
  (1, 33, 1),
  (1, 34, 1),
  (1, 35, 1),
  (1, 36, 1),
  (1, 37, 1),
  (1, 38, 1),
  (1, 39, 1),
  (1, 40, 1),
  (2, 1, 1),
  (2, 2, 1),
  (2, 3, 1),
  (2, 4, 1),
  (2, 5, 1),
  (2, 6, 1),
  (2, 7, 1),
  (2, 8, 1),
  (2, 9, 1),
  (2, 10, 1),
  (2, 11, 1),
  (2, 12, 1),
  (2, 13, 1),
  (2, 14, 1),
  (2, 15, 1),
  (2, 16, 1),
  (2, 17, 1),
  (2, 18, 1),
  (2, 19, 1),
  (2, 20, 1),
  (2, 21, 1),
  (2, 22, 1),
  (2, 23, 1),
  (2, 24, 1),
  (2, 25, 1),
  (2, 26, 1),
  (2, 27, 1),
  (2, 28, 1),
  (2, 29, 1),
  (2, 30, 1),
  (2, 31, 1),
  (2, 32, 1),
  (2, 33, 1),
  (2, 34, 1),
  (2, 35, 1),
  (2, 36, 1),
  (2, 37, 1),
  (2, 38, 1),
  (2, 39, 1),
  (2, 40, 1),
  (3, 1, 1),
  (3, 2, 1),
  (3, 3, 1),
  (3, 4, 1),
  (3, 5, 1),
  (3, 6, 1),
  (3, 7, 1),
  (3, 8, 1),
  (3, 9, 1),
  (3, 10, 1),
  (3, 11, 1),
  (3, 12, 1),
  (3, 13, 1),
  (3, 14, 1),
  (3, 15, 1),
  (3, 16, 1),
  (3, 17, 1),
  (3, 18, 1),
  (3, 19, 1),
  (3, 20, 1),
  (3, 21, 1),
  (3, 22, 1),
  (3, 23, 1),
  (3, 24, 1),
  (3, 25, 1),
  (3, 26, 1),
  (3, 27, 1),
  (3, 28, 1),
  (3, 29, 1),
  (3, 30, 1),
  (3, 31, 1),
  (3, 32, 1),
  (3, 33, 1),
  (3, 34, 1),
  (3, 35, 1),
  (3, 36, 1),
  (3, 37, 1),
  (3, 38, 1),
  (3, 39, 1),
  (3, 40, 1);

INSERT INTO db_de_castilla.Usuario (no_Documento_Usuario, email, password, celular_Usuario, nombre_Usuario, apellido_Usuario, id_Rol_FK, estado, is_superuser, is_active, is_staff) VALUES
  (1234567890, 'admin@admin.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 1234567890, 'Camila Alexandra', 'Arias Ruiz', 1, 1, 1, 1, 1),
  (2345678901, 'Rodriguez_Martinez@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 2345678901, 'Juan David', 'Rodriguez Martinez', 3, 1, 1, 1, 1),
  (3456789012, 'Martinez_Lopez@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 3456789012, 'Laura Sofia', 'Martinez Lopez', 3, 1, 1, 1, 1),
  (4567890123, 'Lopez_Gonzalez@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 4567890123, 'Carlos Andres', 'Lopez Gonzalez', 2, 1, 1, 1, 1),
  (5678901234, 'Gonzalez_Hernandez@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 5678901234, 'Ana Gabriela', 'Gonzalez Hernandez', 2, 1, 1, 1, 1),
  (6789012345, 'Hernandez_Perez@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 6789012345, 'Luis Felipe', 'Hernandez Perez', 2, 1, 1, 1, 1),
  (7890123456, 'Perez_Torres@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 7890123456, 'Valentina Alejandra', 'Perez Torres', 2, 1, 1, 1, 1),
  (8901234567, 'Torres_Ramirez@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 8901234567, 'Felipe Andres', 'Torres Ramirez', 2, 1, 1, 1, 1),
  (9012345678, 'Ramirez_Sanchez@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 9012345678, 'Camila Antonia', 'Ramirez Sanchez', 2, 1, 1, 1, 1),
  (1234567891, 'Sanchez_Romero@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 1234567891, 'Santiago Alejandro', 'Sanchez Romero', 2, 1, 1, 1, 1),
  (2345678902, 'Romero_Morales@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 2345678902, 'Isabella Valeria', 'Romero Morales', 2, 1, 1, 1, 1),
  (3456789013, 'Morales_Flores@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 3456789013, 'David Santiago', 'Morales Flores', 2, 1, 1, 1, 1),
  (4567890124, 'Flores_Cruz@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 4567890124, 'Sofia Valentina', 'Flores Cruz', 2, 1, 1, 1, 1),
  (5678901235, 'Cruz_Gomez@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 5678901235, 'Sebastian Jose', 'Cruz Gomez', 2, 1, 1, 1, 1),
  (6789012346, 'Gomez_Reyes@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 6789012346, 'Daniela Mariana', 'Gomez Reyes', 2, 1, 1, 1, 1),
  (7890123457, 'Reyes_Vargas@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 7890123457, 'Alejandro Sebastian', 'Reyes Vargas', 2, 1, 1, 1, 1),
  (8901234568, 'Vargas_Castro@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 8901234568, 'Gabriela Alejandra', 'Vargas Castro', 2, 1, 1, 1, 1),
  (9012345679, 'Castro_Ruiz@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 9012345679, 'Diego Alejandro', 'Castro Ruiz', 2, 1, 1, 1, 1),
  (1234567892, 'Ruiz_Jimenez@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 1234567892, 'Natalia Andrea', 'Ruiz Jimenez', 2, 1, 1, 1, 1),
  (2345678903, 'Jimenez_Medina@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 2345678903, 'Andres Felipe', 'Jimenez Medina', 2, 1, 1, 1, 1),
  (3456789014, 'Medina_Ortega@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 3456789014, 'Victoria Camila', 'Medina Ortega', 2, 1, 1, 1, 1),
  (4567890125, 'Ortega_Silva@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 4567890125, 'Juan Sebastian', 'Ortega Silva', 2, 1, 1, 1, 1),
  (5678901236, 'Silva_Mendoza@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 5678901236, 'Valeria Isabella', 'Silva Mendoza', 2, 1, 1, 1, 1),
  (6789012347, 'Mendoza_Delgado@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 6789012347, 'Jose Daniel', 'Mendoza Delgado', 2, 1, 1, 1, 1),
  (7890123458, 'Delgado_Rios@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 7890123458, 'Antonia Camila', 'Delgado Rios', 2, 1, 1, 1, 1),
  (8901234569, 'Rios_Aguilar@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 8901234569, 'Felipe Sebastian', 'Rios Aguilar', 2, 1, 1, 1, 1),
  (9012345680, 'Aguilar_Nuñez@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 9012345680, 'Mariana Daniela', 'Aguilar Nuñez', 2, 1, 1, 1, 1),
  (1234567893, 'Nuñez_Paredes@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 1234567893, 'Santiago Felipe', 'Nuñez Paredes', 2, 1, 1, 1, 1),
  (2345678904, 'Paredes_Cordero@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 2345678904, 'Alejandra Valentina', 'Paredes Cordero', 2, 1, 1, 1, 1),
  (3456789015, 'Cordero_Guzman@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 3456789015, 'Luis Eduardo', 'Cordero Guzman', 2, 1, 1, 1, 1),
  (4567890126, 'Guzman_Mora@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 4567890126, 'Andrea Natalia', 'Guzman Mora', 2, 1, 1, 1, 1),
  (5678901237, 'Mora_Cabrera@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 5678901237, 'Alejandro Felipe', 'Mora Cabrera', 2, 1, 1, 1, 1),
  (6789012348, 'Cabrera_Peralta@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 6789012348, 'Valentina Sofia', 'Cabrera Peralta', 2, 1, 1, 1, 1),
  (7890123459, 'Peralta_Leon@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 7890123459, 'Carlos Eduardo', 'Peralta Leon', 2, 1, 1, 1, 1),
  (8901234570, 'Leon_Ayala@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 8901234570, 'Gabriela Sofia', 'Leon Ayala', 2, 1, 1, 1, 1),
  (9012345681, 'Ayala_Bautista@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 9012345681, 'Juan Felipe', 'Ayala Bautista', 2, 1, 1, 1, 1),
  (1234567894, 'Bautista_Caceres@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 1234567894, 'Isabella Maria', 'Bautista Caceres', 2, 1, 1, 1, 1),
  (2345678905, 'Caceres_Navarro@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 2345678905, 'Andres David', 'Caceres Navarro', 2, 1, 1, 1, 1),
  (3456789016, 'Navarro_Peña@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 3456789016, 'Camila Valeria', 'Navarro Peña', 2, 1, 1, 1, 1),
  (4567890127, 'Peña_Rojas@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 4567890127, 'Sebastian Andres', 'Peña Rojas', 2, 1, 1, 1, 1),
  (5678901238, 'Rojas_Acosta@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 5678901238, 'Mariana Gabriela', 'Rojas Acosta', 2, 1, 1, 1, 1),
  (6789012349, 'Acosta_Avila@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 6789012349, 'Jose Alejandro', 'Acosta Avila', 2, 1, 1, 1, 1),
  (7890123460, 'Avila_Duarte@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 7890123460, 'Antonia Sofia', 'Avila Duarte', 2, 1, 1, 1, 1),
  (8901234571, 'Duarte_Rivas@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 8901234571, 'Felipe Alejandro', 'Duarte Rivas', 2, 1, 1, 1, 1),
  (9012345682, 'Rivas_Palacios@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 9012345682, 'Daniela Valentina', 'Rivas Palacios', 2, 1, 1, 1, 1),
  (1234567895, 'Palacios_Zambrano@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 1234567895, 'Alejandro David', 'Palacios Zambrano', 2, 1, 1, 1, 1),
  (2345678906, 'Zambrano_Escobar@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 2345678906, 'Valeria Gabriela', 'Zambrano Escobar', 2, 1, 1, 1, 1),
  (3456789017, 'Escobar_Ibarra@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 3456789017, 'Eduardo Felipe', 'Escobar Ibarra', 2, 1, 1, 1, 1),
  (4567890128, 'Ibarra_Montoya@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 4567890128, 'Natalia Valentina', 'Ibarra Montoya', 2, 1, 1, 1, 1),
  (5678901239, 'Montoya_Valencia@example.com', 'pbkdf2_sha256$720000$LwA8aP8OHOvRqWGnJKqzZZ$tNdX7A74LyzxiNO+4YSv3IAjsdBGEC3M3KwHJ7U0qgU=', 5678901239, 'Felipe Juan', 'Montoya Valencia', 2, 1, 1, 1, 1);
  
INSERT INTO db_de_castilla.Estado_Pedido(nombre_Estado, estado) VALUES
  ('Por Aprobar', 1),
  ('Aprobado', 1),
  ('Preparándose', 1),
  ('Para Recoger', 1),
  ('Cancelado', 1),
  ('Aceptar Cambios', 1),
  ('Finalizados', 1);
  
INSERT INTO db_de_castilla.Pedido (descripcion_Pedido, fecha_Pedido, id_Estado_Pedido_fk, no_Documento_Usuario_FK, estado) VALUES 
  ('Sin descripción', '2023-06-12 09:30:00', 5, 7890123456, 1),
  ('Sin descripción', '2023-06-12 10:15:00', 1, 8901234567, 1),
  ('Sin descripción', '2023-06-12 11:20:00', 3, 2345678902, 1),
  ('Sin descripción', '2023-06-12 12:45:00', 5, 6789012346, 1),
  ('Sin descripción', '2023-06-12 13:30:00', 1, 2345678903, 1),
  ('Sin descripción', '2023-06-12 14:20:00', 3, 1234567893, 1),
  ('Sin descripción', '2023-06-12 15:15:00', 5, 5678901237, 1),
  ('Sin descripción', '2023-06-12 16:10:00', 1, 6789012348, 1),
  ('Sin descripción', '2023-06-12 17:25:00', 3, 7890123459, 1),
  ('Sin descripción', '2023-06-12 18:40:00', 2, 5678901238, 1);
  
INSERT INTO db_de_castilla.Calificacion (estrellas_Calificacion,comentario_Calificacion, id_Proveedor_FK, estado) VALUES
  (5, 'Excelente proveedor', 1, 1),
  (4, 'Buen servicio y productos de calidad', 1, 1),
  (3, 'Regular atención al cliente', 1, 1),
  (5, 'Muy satisfecho con los productos', 2, 1),
  (2, 'Entrega tardí­a y productos defectuosos', 2, 1),
  (4, 'Buen precio y variedad de productos', 2, 1),
  (3, 'Falta de comunicación y retraso en la entrega', 3, 1),
  (4, 'Productos frescos y bien presentados', 3, 1),
  (2, 'Mala atención al cliente y productos de baja calidad', 3, 1),
  (5, 'Siempre cumplen con los plazos de entrega', 4, 1),
  (4, 'Atención rápida y eficiente', 4, 1),
  (3, 'Algunos productos llegaron en mal estado', 4, 1),
  (4, 'Buen trato y solución rápida a los problemas', 5, 1),
  (2, 'No cumplieron con lo acordado', 5, 1),
  (5, 'Excelente calidad de los productos', 5, 1),
  (3, 'Precios competitivos pero poca variedad', 6, 1),
  (4, 'Buen servicio postventa', 6, 1),
  (5, 'Recomiendo ampliamente a este proveedor', 6, 1),
  (2, 'Mal embalaje de los productos', 7, 1),
  (3, 'Entrega demorada sin previo aviso', 7, 1),
  (4, 'Productos frescos y bien empacados', 7, 1),
  (5, 'Siempre nos proveen con productos de calidad', 8, 1),
  (3, 'Atención al cliente deficiente', 8, 1),
  (4, 'Precios justos y calidad garantizada', 8, 1),
  (2, 'No cumplen con los plazos de entrega', 9, 1),
  (3, 'Productos defectuosos', 9, 1),
  (4, 'Buena comunicación y seguimiento de los pedidos', 9, 1),
  (5, 'El mejor proveedor que hemos tenido', 10, 1),
  (4, 'Respuesta rápida ante cualquier inconveniente', 10, 1),
  (3, 'Productos de buena calidad pero precios elevados', 10, 1);
  
INSERT INTO db_de_castilla.estado_oc (id_estado_oc, nombre_estado_oc, estado) VALUES
  (1, 'Solicitada', 1),
  (2, 'Finalizada', 1);
  
INSERT INTO db_de_castilla.Orden_Compra (fecha_oc, hora_oc, id_Estado_oc_FK, estado) VALUES
  ('2023-05-31', '10:00:00', 1, 1),
  ('2023-05-31', '11:30:00', 2, 1),
  ('2023-06-01', '09:45:00', 1, 1),
  ('2023-06-02', '14:20:00', 1, 1),
  ('2023-06-03', '16:30:00', 2, 1),
  ('2023-06-03', '18:45:00', 1, 1),
  ('2023-06-04', '12:15:00', 1, 1),
  ('2023-06-05', '10:30:00', 2, 1),
  ('2023-06-06', '15:00:00', 1, 1),
  ('2023-06-07', '17:45:00', 1, 1),
  ('2023-06-08', '09:15:00', 2, 1),
  ('2023-06-09', '11:30:00', 1, 1),
  ('2023-06-09', '13:45:00', 2, 1),
  ('2023-06-10', '16:00:00', 1, 1),
  ('2023-06-11', '10:45:00', 1, 1),
  ('2023-06-12', '14:30:00', 2, 1),
  ('2023-06-13', '12:00:00', 1, 1),
  ('2023-06-14', '09:30:00', 2, 1),
  ('2023-06-15', '11:45:00', 1, 1),
  ('2023-06-16', '15:15:00', 2, 1);

INSERT INTO db_de_castilla.Detalle_OC (cantidad_insumo, id_Insumo_FK, id_oc_FK, estado) VALUES
  (5, 1, 1, 1),
  (3, 2, 1, 1),
  (2, 3, 1, 1),
  (4, 4, 2, 1),
  (1, 5, 2, 1),
  (3, 6, 2, 1),
  (2, 7, 3, 1),
  (4, 8, 3, 1),
  (2, 9, 3, 1),
  (5, 10, 4, 1),
  (3, 11, 4, 1),
  (2, 12, 4, 1),
  (4, 13, 5, 1),
  (1, 14, 5, 1),
  (3, 15, 5, 1),
  (2, 16, 6, 1),
  (4, 17, 6, 1),
  (2, 18, 6, 1),
  (5, 19, 7, 1),
  (3, 20, 7, 1),
  (2, 1, 8, 1),
  (4, 2, 8, 1),
  (1, 3, 8, 1),
  (3, 4, 9, 1),
  (2, 5, 9, 1),
  (4, 6, 9, 1),
  (1, 7, 10, 1),
  (3, 8, 10, 1),
  (2, 9, 10, 1),
  (5, 10, 11, 1),
  (3, 11, 11, 1),
  (2, 12, 11, 1),
  (4, 13, 12, 1),
  (1, 14, 12, 1),
  (3, 15, 12, 1),
  (2, 16, 13, 1),
  (4, 17, 13, 1),
  (2, 18, 13, 1),
  (5, 19, 14, 1),
  (3, 20, 14, 1),
  (2, 1, 15, 1),
  (4, 2, 15, 1),
  (1, 3, 15, 1),
  (3, 4, 16, 1),
  (2, 5, 16, 1);
  
INSERT INTO db_de_castilla.historico(fecha_movimiento, cantidad_Historico, tipo_Historico, id_Insumo_FK, id_tipo_Movimiento_FK, estado) VALUES 
  ('2022-01-01 10:30:00', 100,'INSUMO', 1, 1, 1),
  ('2022-02-15 16:00:00', 100,'INSUMO', 2, 1, 1),
  ('2022-03-05 12:30:00', 100,'INSUMO', 3, 1, 1),
  ('2022-04-20 09:45:00', 100,'INSUMO', 4, 1, 1),
  ('2022-05-10 14:30:00', 100,'INSUMO', 5, 1, 1),
  ('2022-06-12 11:45:00', 100,'INSUMO', 6, 1, 1),
  ('2022-07-05 10:15:00', 100,'INSUMO', 7, 1, 1),
  ('2022-08-18 14:00:00', 100,'INSUMO', 8, 1, 1),
  ('2022-09-22 15:00:00', 100,'INSUMO', 9, 1, 1),
  ('2022-10-30 11:30:00', 100,'INSUMO', 10, 1, 1),
  ('2022-11-12 17:45:00', 100,'INSUMO', 11, 1, 1),
  ('2022-12-05 12:45:00', 100,'INSUMO', 12, 1, 1),
  ('2023-01-10 10:30:00', 100,'INSUMO', 13, 1, 1),
  ('2023-02-18 16:00:00', 100,'INSUMO', 14, 1, 1),
  ('2023-03-05 12:30:00', 100,'INSUMO', 15, 1, 1),
  ('2023-04-20 09:45:00', 100,'INSUMO', 16, 1, 1),
  ('2023-05-10 14:30:00', 100,'INSUMO', 17, 1, 1),
  ('2023-06-12 11:45:00', 100,'INSUMO', 18, 1, 1),
  ('2023-07-05 10:15:00', 100,'INSUMO', 19, 1, 1),
  ('2023-08-18 14:00:00', 100,'INSUMO', 20,1, 1);
  
INSERT INTO db_de_castilla.historico(fecha_movimiento, cantidad_Historico, tipo_Historico, id_Producto_FK, id_tipo_Movimiento_FK, estado) VALUES 
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 1, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 2, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 3, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 4, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 5, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 6, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 7, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 8, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 9, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 10, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 11, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 12, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 13, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 14, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 15, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 16, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 17, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 18, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 19, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 20, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 21, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 22, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 23, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 24, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 25, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 26, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 27, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 28, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 29, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 30, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 31, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 32, 1, 1),
  ( '2022-01-01 10:30:00', 100, 'PRODUCTO', 33, 1, 1);

INSERT INTO db_de_castilla.Venta (fecha_Venta, hora_venta, total_Venta, no_Documento_Usuario_FK, estado) VALUES
  ('2023-01-01', '09:30:00', 150000, 2345678901, 1),
  ('2023-01-02', '14:45:00', 200000, 2345678901, 1),
  ('2023-01-02', '16:20:00', 120000, 2345678901, 1),
  ('2023-01-03', '10:15:00', 180000, 2345678901, 1),
  ('2023-01-03', '12:30:00', 90000, 2345678901, 1),
  ('2023-01-04', '15:45:00', 140000, 2345678901, 1),
  ('2023-01-05', '11:10:00', 160000, 2345678901, 1),
  ('2023-01-06', '17:25:00', 110000, 2345678901, 1),
  ('2023-01-06', '19:40:00', 170000, 2345678901, 1),
  ('2023-01-07', '13:55:00', 130000, 2345678901, 1),
  ('2023-01-08', '09:00:00', 190000, 2345678901, 1),
  ('2023-01-09', '14:15:00', 100000, 2345678901, 1),
  ('2023-01-09', '16:30:00', 150000, 2345678901, 1),
  ('2023-01-10', '12:45:00', 200000, 2345678901, 1),
  ('2023-01-11', '10:40:00', 120000, 2345678901, 1),
  ('2023-01-11', '13:00:00', 180000, 2345678901, 1),
  ('2023-01-12', '15:15:00', 90000, 2345678901, 1),
  ('2023-01-13', '11:30:00', 140000, 2345678901, 1),
  ('2023-01-14', '17:45:00', 160000, 2345678901, 1),
  ('2023-01-14', '20:00:00', 110000, 2345678901, 1),
  ('2023-01-15', '09:30:00', 120000, 3456789012, 1),
  ('2023-01-16', '14:45:00', 180000, 3456789012, 1),
  ('2023-01-16', '16:20:00', 110000, 3456789012, 1),
  ('2023-01-17', '10:15:00', 150000, 3456789012, 1),
  ('2023-01-17', '12:30:00', 90000, 3456789012, 1),
  ('2023-01-18', '15:45:00', 170000, 3456789012, 1),
  ('2023-01-19', '11:10:00', 130000, 3456789012, 1),
  ('2023-01-20', '17:25:00', 160000, 3456789012, 1),
  ('2023-01-20', '19:40:00', 140000, 3456789012, 1),
  ('2023-01-21', '13:55:00', 190000, 3456789012, 1),
  ('2023-01-22', '09:00:00', 100000, 3456789012, 1),
  ('2023-01-23', '14:15:00', 150000, 3456789012, 1),
  ('2023-01-23', '16:30:00', 200000, 3456789012, 1),
  ('2023-01-24', '12:45:00', 120000, 3456789012, 1),
  ('2023-01-25', '10:40:00', 180000, 3456789012, 1),
  ('2023-01-25', '13:00:00', 90000, 3456789012, 1),
  ('2023-01-26', '15:15:00', 140000, 3456789012, 1),
  ('2023-01-27', '11:30:00', 160000, 3456789012, 1),
  ('2023-01-28', '17:45:00', 110000, 3456789012, 1),
  ('2023-01-28', '20:00:00', 130000, 3456789012, 1),
  ('2023-06-12', '09:30:00', 4500, 3456789012, 1),
  ('2023-06-12', '10:15:00', 12000, 3456789012, 1),
  ('2023-06-12', '11:20:00', 50000, 3456789012, 1),
  ('2023-06-12', '13:30:00', 60000, 3456789012, 1),
  ('2023-06-12', '14:20:00', 12000, 3456789012, 1),
  ('2023-06-12', '16:10:00' , 215000, 3456789012, 1),
  ('2023-06-12', '17:25:00', 32000, 3456789012, 1);
  
INSERT INTO db_de_castilla.oc_has_proveedor (id_oc_fk, id_proveedor_fk, estado) VALUES
  (13, 1, 1),
  (7, 2, 1),
  (5, 3, 1),
  (11, 4, 1),
  (14, 4, 1),
  (15, 4, 1),
  (20, 4, 1),
  (7, 6, 1),
  (1, 5, 1),
  (2, 5, 1),
  (3, 10, 1),
  (4, 10, 1),
  (6, 10, 1),
  (8, 9, 1),
  (9, 10, 1),
  (10, 10, 1),
  (12, 5, 1),
  (16, 7, 1),
  (17, 5, 1),
  (18, 4, 1),
  (19, 9, 1),
  (19, 4, 1);
  
INSERT INTO db_de_castilla.Detalle_Pedido (cantidad_producto, subtotal_Detalle_Pedido, id_Producto_FK, id_Pedido_FK, estado) VALUES
  (2, 9000, 1, 1, 1),
  (1, 3000, 2, 1, 1),
  (3, 6000, 3, 1, 1),
  (1, 6000, 4, 2, 1),
  (2, 30000, 5, 3, 1),
  (1, 24000, 6, 4, 1),
  (2, 12000, 7, 5, 1),
  (1, 6000, 8, 5, 1),
  (1, 50000, 9, 6, 1),
  (2, 20000, 10, 7, 1),
  (3, 12000, 11, 8, 1),
  (1, 4000, 12, 8, 1),
  (2, 50000, 13, 9, 1),
  (1, 1500, 14, 9, 1),
  (2, 5000, 15, 9, 1),
  (1, 2500, 16, 10, 1),
  (1, 4500, 17, 10, 1),
  (1, 6500, 18, 10, 1);
  
  
INSERT INTO db_de_castilla.Detalle_Venta (cantidad_producto, subtotal_Detalle_Venta, id_Producto_FK, id_Venta_FK, estado) VALUES
  (2, 9000, 1, 1, 1),
  (1, 3000, 2, 1, 1),
  (3, 6000, 3, 1, 1),
  (1, 6000, 4, 2, 1),
  (2, 30000, 5, 3, 1),
  (1, 24000, 6, 4, 1),
  (2, 12000, 7, 5, 1),
  (1, 6000, 8, 5, 1),
  (1, 50000, 9, 6, 1),
  (2, 20000, 10, 7, 1),
  (3, 12000, 11, 8, 1),
  (1, 4000, 12, 8, 1),
  (2, 50000, 13, 9, 1),
  (1, 1500, 14, 9, 1),
  (2, 5000, 15, 9, 1),
  (1, 2500, 16, 10, 1),
  (1, 4500, 17, 10, 1),
  (1, 6500, 18, 10, 1),
  (1, 4000, 19, 11, 1),
  (1, 5000, 20, 11, 1),
  (1, 4000, 21, 11, 1),
  (1, 4000, 22, 11, 1),
  (2, 22000, 23, 12, 1),
  (1, 28000, 24, 12, 1),
  (1, 20000, 25, 13, 1),
  (1, 25000, 26, 14, 1),
  (1, 15000, 27, 15, 1),
  (2, 9000, 28, 15, 1),
  (1, 14000, 29, 16, 1),
  (1, 10000, 30, 17, 1),
  (1, 7000, 31, 18, 1),
  (2, 12000, 32, 18, 1),
  (1, 6000, 12, 19, 1),
  (1, 6000, 12, 20, 1),
  (1, 7000, 12, 21, 1),
  (1, 6000, 12, 22, 1),
  (1, 6000, 12, 23, 1),
  (1, 3000, 12, 24, 1),
  (1, 6000, 12, 24, 1),
  (1, 6000, 12, 25, 1),
  (1, 6000, 12, 26, 1),
  (1, 6000, 12, 26, 1),
  (1, 6000, 12, 27, 1),
  (1, 6000, 12, 28, 1),
  (1, 6000, 12, 29, 1),
  (1, 3000, 12, 30, 1),
  (1, 6000, 12, 31, 1),
  (1, 4500, 1, 32, 1),
  (2, 6000, 2, 32, 1),
  (1, 3000, 3, 32, 1),
  (3, 9000, 4, 33, 1),
  (1, 6000, 5, 33, 1),
  (2, 12000, 6, 34, 1),
  (1, 6000, 7, 34, 1),
  (1, 15000, 8, 35, 1),
  (2, 30000, 9, 36, 1),
  (1, 12000, 10, 36, 1),
  (1, 2000, 11, 36, 1),
  (1, 4000, 12, 37, 1),
  (1, 6000, 13, 37, 1),
  (1, 6000, 14, 38, 1),
  (2, 12000, 15, 39, 1),
  (1, 6000, 16, 39, 1),
  (1, 4000, 17, 40, 1),
  (1, 4000, 18, 40, 1),
  (2, 10000, 19, 40, 1),
  (1, 6000, 20, 41, 1),
  (1, 5000, 21, 41, 1),
  (1, 4000, 22, 42, 1),
  (1, 4000, 23, 42, 1),
  (1, 6000, 24, 43, 1),
  (1, 3000, 25, 43, 1),
  (1, 6000, 26, 44, 1),
  (1, 6000, 27, 44, 1),
  (1, 4000, 28, 44, 1),
  (1, 4000, 29, 45, 1),
  (1, 4000, 30, 45, 1),
  (1, 4000, 31, 45, 1),
  (1, 11000, 32, 46, 1),
  (1, 11000, 32, 46, 1),
  (1, 11000, 32, 46, 1),
  (1, 14000, 32, 46, 1),
  (2, 28000, 32, 47, 1),
  (1, 6000, 32, 47, 1),
  (1, 4000, 32, 47, 1);
  
INSERT INTO db_de_castilla.Sabor_has_Producto (id_Sabor_FK, id_Producto_FK, estado) VALUES
  (1, 1, 1), 
  (2, 1, 1),
  (3, 1, 1),
  (4, 1, 1), 
  (5, 1, 1),
  (1, 2, 1), 
  (2, 2, 1), 
  (3, 2, 1), 
  (4, 2, 1), 
  (5, 2, 1),
  (1, 3, 1), 
  (2, 3, 1), 
  (3, 3, 1), 
  (4, 3, 1), 
  (5, 3, 1),
  (1, 4, 1), 
  (2, 4, 1), 
  (3, 4, 1), 
  (4, 4, 1), 
  (5, 4, 1),
  (1, 5, 1), 
  (2, 5, 1), 
  (3, 5, 1), 
  (4, 5, 1), 
  (5, 5, 1),
  (1, 6, 1), 
  (2, 6, 1), 
  (3, 6, 1), 
  (4, 6, 1), 
  (5, 6, 1),
  (1, 7, 1), 
  (2, 7, 1), 
  (3, 7, 1), 
  (4, 7, 1), 
  (5, 7, 1),
  (1, 8, 1), 
  (2, 8, 1), 
  (3, 8, 1), 
  (4, 8, 1), 
  (5, 8, 1),
  (1, 9, 1), 
  (2, 9, 1), 
  (3, 9, 1), 
  (4, 9, 1), 
  (5, 9, 1),
  (1, 10, 1), 
  (2, 10, 1), 
  (3, 10, 1), 
  (4, 10, 1), 
  (5, 10, 1),
  (6, 11, 1), 
  (7, 11, 1), 
  (8, 11, 1), 
  (9, 11, 1), 
  (10, 11, 1),
  (6, 12, 1), 
  (7, 12, 1), 
  (8, 12, 1), 
  (9, 12, 1), 
  (10, 12, 1),
  (6, 13, 1), 
  (7, 13, 1), 
  (8, 13, 1), 
  (9, 13, 1), 
  (10, 13, 1),
  (6, 14, 1), 
  (7, 14, 1), 
  (8, 14, 1), 
  (9, 14, 1), 
  (10, 14, 1),
  (6, 15, 1), 
  (7, 15, 1), 
  (8, 15, 1), 
  (9, 15, 1), 
  (10, 15, 1),
  (6, 16, 1), 
  (7, 16, 1), 
  (8, 16, 1), 
  (9, 16, 1), 
  (10, 16, 1),
  (6, 17, 1), 
  (7, 17, 1), 
  (8, 17, 1), 
  (9, 17, 1), 
  (10, 17, 1),
  (6, 18, 1), 
  (7, 18, 1), 
  (8, 18, 1), 
  (9, 18, 1), 
  (10, 18, 1),
  (6, 19, 1), 
  (7, 19, 1), 
  (8, 19, 1), 
  (9, 19, 1), 
  (10, 19, 1),
  (6, 20, 1), 
  (7, 20, 1), 
  (8, 20, 1), 
  (9, 20, 1), 
  (10, 20, 1),
  (1, 21, 1), 
  (2, 21, 1), 
  (3, 21, 1),
  (1, 22, 1), 
  (2, 22, 1), 
  (3, 22, 1), 
  (1, 23, 1), 
  (2, 23, 1), 
  (3, 23, 1),
  (1, 24, 1), 
  (2, 24, 1), 
  (3, 24, 1),
  (1, 25, 1), 
  (2, 25, 1), 
  (3, 25, 1),
  (1, 26, 1), 
  (2, 26, 1), 
  (3, 26, 1),
  (1, 27, 1), 
  (2, 27, 1), 
  (3, 27, 1), 
  (1, 28, 1), 
  (2, 28, 1), 
  (3, 28, 1),
  (1, 29, 1), 
  (2, 29, 1), 
  (3, 29, 1),
  (1, 30, 1), 
  (2, 30, 1), 
  (3, 30, 1),
  (4, 31, 1), 
  (5, 31, 1), 
  (6, 31, 1), 
  (7, 31, 1), 
  (8, 31, 1),
  (4, 32, 1), 
  (5, 32, 1), 
  (6, 32, 1), 
  (7, 32, 1), 
  (8, 32, 1);