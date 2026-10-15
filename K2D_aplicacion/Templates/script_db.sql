-- Script de creación de Base de Datos y Usuario para la entrega
CREATE DATABASE IF NOT EXISTS k2d_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'k2d_admin'@'%' IDENTIFIED BY 'TuContrasenaSegura123';

GRANT ALL PRIVILEGES ON k2d_db.* TO 'k2d_admin'@'%';

FLUSH PRIVILEGES;
