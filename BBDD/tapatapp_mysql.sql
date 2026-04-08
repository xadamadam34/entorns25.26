-- phpMyAdmin SQL Dump
-- version 5.1.1deb5ubuntu1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 18-12-2024 a las 19:42:43
-- Versión del servidor: 8.0.40-0ubuntu0.22.04.1
-- Versión de PHP: 8.1.2-1ubuntu2.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `tapatapp`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Child`
--

CREATE TABLE `Child` (
  `id` int NOT NULL,
  `child_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_eo_0900_as_cs NOT NULL,
  `sleep_average` int NOT NULL,
  `treatment_id` int NOT NULL,
  `time` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `Child`
--

INSERT INTO `Child` (`id`, `child_name`, `sleep_average`, `treatment_id`, `time`) VALUES
(1, 'Carol Child', 8, 1, 6),
(2, 'Jaco Child', 10, 2, 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `RelationUserChild`
--

CREATE TABLE `RelationUserChild` (
  `user_id` int NOT NULL,
  `child_id` int NOT NULL,
  `rol_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `RelationUserChild`
--

INSERT INTO `RelationUserChild` (`user_id`, `child_id`, `rol_id`) VALUES
(1, 1, 1),
(1, 1, 2),
(2, 2, 1),
(2, 2, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Rol`
--

CREATE TABLE `Rol` (
  `id` int NOT NULL,
  `type_rol` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_eo_0900_as_cs NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `Rol`
--

INSERT INTO `Rol` (`id`, `type_rol`) VALUES
(1, 'Admin'),
(2, 'Tutor Mare Pare'),
(3, 'Cuidador'),
(4, 'Seguiment');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Status`
--

CREATE TABLE `Status` (
  `id` int NOT NULL,
  `name` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_eo_0900_as_cs NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `Status`
--

INSERT INTO `Status` (`id`, `name`) VALUES
(1, 'sleep'),
(2, 'awake'),
(3, 'yes_eyepatch'),
(4, 'no_eyepatch');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Tap`
--

CREATE TABLE `Tap` (
  `id` int NOT NULL,
  `child_id` int NOT NULL,
  `status_id` int NOT NULL,
  `user_id` int NOT NULL,
  `init` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Treatment`
--

CREATE TABLE `Treatment` (
  `id` int NOT NULL,
  `name` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_eo_0900_as_cs NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `Treatment`
--

INSERT INTO `Treatment` (`id`, `name`) VALUES
(1, 'Hour'),
(2, 'percentage');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `User`
--

CREATE TABLE `User` (
  `id` int NOT NULL,
  `username` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_eo_0900_as_cs NOT NULL,
  `password` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_eo_0900_as_cs NOT NULL,
  `email` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_eo_0900_as_cs NOT NULL,
  `token` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_eo_0900_as_cs DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `User`
--

INSERT INTO `User` (`id`, `username`, `password`, `email`) VALUES
(1, 'mare', 'mare', 'prova@gmail.com'),
(2, 'pare', 'pare', 'prova2@gmail.com');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Child`
--
ALTER TABLE `Child`
  ADD PRIMARY KEY (`id`),
  ADD KEY `treatment_id` (`treatment_id`);

--
-- Indices de la tabla `RelationUserChild`
--
ALTER TABLE `RelationUserChild`
  ADD PRIMARY KEY (`user_id`,`child_id`,`rol_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `child_id` (`child_id`),
  ADD KEY `rol_id` (`rol_id`);

--
-- Indices de la tabla `Rol`
--
ALTER TABLE `Rol`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `Status`
--
ALTER TABLE `Status`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `Tap`
--
ALTER TABLE `Tap`
  ADD PRIMARY KEY (`id`),
  ADD KEY `status_id` (`status_id`),
  ADD KEY `child_id` (`child_id`),
  ADD KEY `Tap_ibfk_3` (`user_id`);

--
-- Indices de la tabla `Treatment`
--
ALTER TABLE `Treatment`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `User`
--
ALTER TABLE `User`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Child`
--
ALTER TABLE `Child`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `Rol`
--
ALTER TABLE `Rol`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `Status`
--
ALTER TABLE `Status`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `Tap`
--
ALTER TABLE `Tap`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Treatment`
--
ALTER TABLE `Treatment`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `User`
--
ALTER TABLE `User`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `Child`
--
ALTER TABLE `Child`
  ADD CONSTRAINT `Child_ibfk_1` FOREIGN KEY (`treatment_id`) REFERENCES `Treatment` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `RelationUserChild`
--
ALTER TABLE `RelationUserChild`
  ADD CONSTRAINT `RelationUserChild_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `RelationUserChild_ibfk_2` FOREIGN KEY (`child_id`) REFERENCES `Child` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `RelationUserChild_ibfk_3` FOREIGN KEY (`rol_id`) REFERENCES `Rol` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `Tap`
--
ALTER TABLE `Tap`
  ADD CONSTRAINT `Tap_ibfk_1` FOREIGN KEY (`status_id`) REFERENCES `Status` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Tap_ibfk_2` FOREIGN KEY (`child_id`) REFERENCES `Child` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Tap_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `User` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;