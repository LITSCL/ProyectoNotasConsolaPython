-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-12-2023 a las 22:47:00
-- Versión del servidor: 10.4.17-MariaDB
-- Versión de PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `dbproyectonotasconsolapython`
--
CREATE DATABASE IF NOT EXISTS `dbproyectonotasconsolapython` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `dbproyectonotasconsolapython`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nota`
--

CREATE TABLE `nota` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) DEFAULT NULL,
  `descripcion` mediumtext DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `usuario_correo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `correo` varchar(255) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `apellido` varchar(255) DEFAULT NULL,
  `clave` varchar(255) DEFAULT NULL,
  `fecha` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `nota`
--
ALTER TABLE `nota`
  ADD PRIMARY KEY (`id`,`usuario_correo`),
  ADD KEY `fk_nota_usuario_idx` (`usuario_correo`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`correo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `nota`
--
ALTER TABLE `nota`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `nota`
--
ALTER TABLE `nota`
  ADD CONSTRAINT `fk_nota_usuario` FOREIGN KEY (`usuario_correo`) REFERENCES `usuario` (`correo`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
