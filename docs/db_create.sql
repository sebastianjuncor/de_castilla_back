/*__________________________________________________________

    CREACIÓN DE LA BASE DE DATOS
__________________________________________________________*/-- Creación de la base de datos
DROP DATABASE IF EXISTS db_de_castilla;
CREATE DATABASE IF NOT EXISTS db_de_castilla;
USE db_de_castilla;-- -----------------------------------------------------
-- Tabla estadopedido
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS estado_pedido (
    id_estado_pedido BIGINT NOT NULL AUTO_INCREMENT,
    nombre_estado VARCHAR(255),
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_estado_pedido)
    );

-- -----------------------------------------------------
-- Tabla rol
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS rol (
    id_rol BIGINT NOT NULL AUTO_INCREMENT,
    nombre_rol VARCHAR(255),
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_rol)
    );

-- -----------------------------------------------------
-- Tabla usuario
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS usuario (
    no_documento_usuario BIGINT NOT NULL AUTO_INCREMENT,
    apellido_usuario VARCHAR(255),
    celular_usuario BIGINT,
    email VARCHAR(255),
    nombre_usuario VARCHAR(255),
    password VARCHAR(255),
    id_rol_fk BIGINT,
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (no_documento_usuario),
    FOREIGN KEY (id_rol_fk) REFERENCES rol (id_rol)
    );



-- -----------------------------------------------------
-- Tabla proveedor
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS proveedor (
    id_proveedor BIGINT NOT NULL AUTO_INCREMENT,
    celular_proveedor BIGINT,
    celular_respaldo_proveedor BIGINT,
    correo_proveedor VARCHAR(255),
    empresa_proveedor VARCHAR(255),
    estado_proveedor BIT(1),
    nit_proveedor BIGINT,
    nombre_proveedor VARCHAR(255),
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_proveedor)
    );

-- -----------------------------------------------------
-- Tabla categoria
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS categoria (
    id_categoria BIGINT NOT NULL AUTO_INCREMENT,
    descripcion_categoria VARCHAR(255),
    nombre_categoria VARCHAR(255),
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_categoria)
    );

-- -----------------------------------------------------
-- Tabla producto
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS producto (
    id_producto BIGINT NOT NULL AUTO_INCREMENT,
    nombre_producto VARCHAR(255),
    imagen_producto VARCHAR(255),
    precio_producto INT,
    id_categoria_fk BIGINT,
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_producto),
    FOREIGN KEY (id_categoria_fk) REFERENCES categoria (id_categoria)
    );

-- -----------------------------------------------------
-- Tabla pedido
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS pedido (
    id_pedido BIGINT NOT NULL AUTO_INCREMENT,
    descripcion_pedido VARCHAR(255),
    fecha_pedido DATE,
    id_estado_pedido_fk BIGINT,
    no_documento_usuario_fk BIGINT,
    estrellas_pedido INT,
    comentario_pedido VARCHAR(100),
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_pedido),
    FOREIGN KEY (id_estado_pedido_fk) REFERENCES estado_pedido (id_estado_pedido),
    FOREIGN KEY (no_documento_usuario_fk) REFERENCES usuario (no_documento_usuario)
    );

-- -----------------------------------------------------
-- Tabla detalle_pedido
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS detalle_pedido (
    id_detalle_pedido BIGINT NOT NULL AUTO_INCREMENT,
    cantidad_producto INT,
    subtotal_detalle_pedido BIGINT,
    id_producto_fk BIGINT,
    id_pedido_fk BIGINT,
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_detalle_pedido),
    FOREIGN KEY (id_producto_fk) REFERENCES producto (id_producto),
    FOREIGN KEY (id_pedido_fk) REFERENCES pedido (id_pedido)
    );

-- -----------------------------------------------------
-- Tabla calificacion
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS calificacion (
    id_calificacion BIGINT NOT NULL AUTO_INCREMENT,
    comentario_calificacion VARCHAR(255),
    estrallas_calificacion INT,
    id_proveedor_fk BIGINT,
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_calificacion),
    FOREIGN KEY (id_proveedor_fk) REFERENCES proveedor (id_proveedor)
    );

-- -----------------------------------------------------
-- Tabla venta
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS venta (
    id_venta BIGINT NOT NULL AUTO_INCREMENT,
    fecha_venta DATE,
    hora_venta TIME,
    total_venta BIGINT,
    id_pedido_fk BIGINT,
    no_documento_usuario_fk BIGINT,
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_venta),
    FOREIGN KEY (id_pedido_fk) REFERENCES pedido (id_pedido),
    FOREIGN KEY (no_documento_usuario_fk) REFERENCES usuario (no_documento_usuario)
    );

-- -----------------------------------------------------
-- Tabla detalle_venta
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS detalle_venta (
    id_detalle_venta BIGINT NOT NULL AUTO_INCREMENT,
    cantidad_producto INT,
    subtotal_detalle_venta BIGINT,
    id_producto_fk BIGINT,
    id_venta_fk BIGINT,
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_detalle_venta),
    FOREIGN KEY (id_producto_fk) REFERENCES producto (id_producto),
    FOREIGN KEY (id_venta_fk) REFERENCES venta (id_venta)
    );

-- -----------------------------------------------------
-- Tabla estado_oc
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS estado_oc (
    id_estado_oc BIGINT NOT NULL AUTO_INCREMENT,
    nombre_estado_oc VARCHAR(255),
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_estado_oc)
    );

-- -----------------------------------------------------
-- Tabla orden_compra
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS orden_compra (
    id_oc BIGINT NOT NULL AUTO_INCREMENT,
    fecha_oc DATE,
    hora_oc TIME,
    id_estado_oc_fk BIGINT,
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_oc),
    FOREIGN KEY (id_estado_oc_fk) REFERENCES estado_oc (id_estado_oc)
    );

-- -----------------------------------------------------
-- Tabla estado_insumo
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS estado_insumo (
    id_estado_insumo BIGINT NOT NULL AUTO_INCREMENT,
    nombre_estado_insumo VARCHAR(255),
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_estado_insumo)
    );

-- -----------------------------------------------------
-- Tabla insumo
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS insumo (
    id_insumo BIGINT NOT NULL AUTO_INCREMENT,
    nombre_insumo VARCHAR(255),
    id_estado_insumo BIGINT,
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_insumo),
    FOREIGN KEY (id_estado_insumo) REFERENCES estado_insumo (id_estado_insumo)
    );

-- -----------------------------------------------------
-- Tabla detalleoc
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS detalle_oc (
    id_detalle_oc BIGINT NOT NULL AUTO_INCREMENT,
    cantidad_insumo INT,
    id_insumo_fk BIGINT,
    id_oc_fk BIGINT,
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_detalle_oc),
    FOREIGN KEY (id_oc_fk) REFERENCES orden_compra (id_oc),
    FOREIGN KEY (id_insumo_fk) REFERENCES insumo (id_insumo)
    );

-- -----------------------------------------------------
-- Tabla tipo_movimiento
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS tipo_movimiento (
    id_tipo_movimiento BIGINT NOT NULL AUTO_INCREMENT,
    nombre_tipo_movimiento VARCHAR(255),
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_tipo_movimiento)
    );

-- -----------------------------------------------------
-- Tabla historico
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS historico (
    id_historico BIGINT NOT NULL AUTO_INCREMENT,
    cantidad_historico INT,
    fecha_caducidad DATE,
    fecha_movimiento DATE,
    tipo_historico VARCHAR(255),
    id_insumo_fk BIGINT,
    id_producto_fk BIGINT,
    id_tipo_movimiento_fk BIGINT,
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_historico),
    FOREIGN KEY (id_producto_fk) REFERENCES producto (id_producto),
    FOREIGN KEY (id_tipo_movimiento_fk) REFERENCES tipo_movimiento (id_tipo_movimiento),
    FOREIGN KEY (id_insumo_fk) REFERENCES insumo (id_insumo)
    );

-- -----------------------------------------------------
-- Tabla inventario
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS inventario (
    id_inventario BIGINT NOT NULL AUTO_INCREMENT,
    stock_inventario INT,
    tipo_inventario VARCHAR(255),
    id_insumo_fk BIGINT,
    id_producto_fk BIGINT,
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_inventario),
    FOREIGN KEY (id_producto_fk) REFERENCES producto (id_producto),
    FOREIGN KEY (id_insumo_fk) REFERENCES insumo (id_insumo)
    );

-- -----------------------------------------------------
-- Tabla oc_has_proveedor
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS oc_has_proveedor (
    id_oc_has_proveedor BIGINT NOT NULL AUTO_INCREMENT,
    id_oc_fk BIGINT,
    id_proveedor_fk BIGINT,
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_oc_has_proveedor),
    FOREIGN KEY (id_oc_fk) REFERENCES orden_compra (id_oc),
    FOREIGN KEY (id_proveedor_fk) REFERENCES proveedor (id_proveedor)
    );

-- -----------------------------------------------------
-- Tabla permiso
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS permiso (
    id_permiso BIGINT NOT NULL AUTO_INCREMENT,
    descripcion_permiso VARCHAR(255),
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_permiso)
    );

-- -----------------------------------------------------
-- Tabla rol_has_permiso
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS rol_has_permiso (
    id_rol_has_permiso BIGINT NOT NULL AUTO_INCREMENT,
    id_permiso_fk BIGINT,
    id_rol_fk BIGINT,
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_rol_has_permiso),
    FOREIGN KEY (id_rol_fk) REFERENCES rol (id_rol),
    FOREIGN KEY (id_permiso_fk) REFERENCES permiso (id_permiso)
    );

-- -----------------------------------------------------
-- Tabla sabor
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS sabor (
    id_sabor BIGINT NOT NULL AUTO_INCREMENT,
    nombre_sabor VARCHAR(255),
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_sabor)
    );

-- -----------------------------------------------------
-- Tabla sabor_has_producto
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS sabor_has_producto (
    id_sabor_has_producto BIGINT NOT NULL AUTO_INCREMENT,
    id_producto_fk BIGINT,
    id_sabor_fk BIGINT,
    estado BIT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id_sabor_has_producto),
    FOREIGN KEY (id_sabor_fk) REFERENCES sabor (id_sabor),
    FOREIGN KEY (id_producto_fk) REFERENCES producto (id_producto)
    );
