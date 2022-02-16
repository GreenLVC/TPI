CREATE DATABASE  IF NOT EXISTS `myplaylists` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `myplaylists`;
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: myplaylists
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `albums`
--

DROP TABLE IF EXISTS `albums`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `albums` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `fechaSalida` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `albums`
--

LOCK TABLES `albums` WRITE;
/*!40000 ALTER TABLE `albums` DISABLE KEYS */;
/*!40000 ALTER TABLE `albums` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artistas`
--

DROP TABLE IF EXISTS `artistas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artistas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `popularidad` double NOT NULL,
  `tipo_artista` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artistas`
--

LOCK TABLES `artistas` WRITE;
/*!40000 ALTER TABLE `artistas` DISABLE KEYS */;
/*!40000 ALTER TABLE `artistas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `canciones`
--

DROP TABLE IF EXISTS `canciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `canciones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(45) NOT NULL,
  `pista` varchar(45) NOT NULL,
  `mood` varchar(45) DEFAULT NULL,
  `duracion` time NOT NULL,
  `reproducciones` int NOT NULL,
  `explicita` tinyint NOT NULL,
  `popularidad` double NOT NULL,
  `tipo_cancion` varchar(45) DEFAULT NULL,
  `idAlbum` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idAlbum_idx` (`idAlbum`),
  CONSTRAINT `idAlbum` FOREIGN KEY (`idAlbum`) REFERENCES `albums` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `canciones`
--

LOCK TABLES `canciones` WRITE;
/*!40000 ALTER TABLE `canciones` DISABLE KEYS */;
/*!40000 ALTER TABLE `canciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cuentas`
--

DROP TABLE IF EXISTS `cuentas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cuentas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(45) NOT NULL,
  `explicito` tinyint NOT NULL,
  `display_name` varchar(45) NOT NULL,
  `tipoCuenta` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cuentas`
--

LOCK TABLES `cuentas` WRITE;
/*!40000 ALTER TABLE `cuentas` DISABLE KEYS */;
/*!40000 ALTER TABLE `cuentas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genero_cancion`
--

DROP TABLE IF EXISTS `genero_cancion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genero_cancion` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idArtista` int NOT NULL,
  `idCancion` int NOT NULL,
  `idGenero` int NOT NULL,
  `artista_principal` tinyint NOT NULL,
  `fecha_publicacion` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idArtsta_idx` (`idArtista`),
  KEY `idCancion_idx` (`idCancion`),
  KEY `idGenero_idx` (`idGenero`),
  CONSTRAINT `idArtsta` FOREIGN KEY (`idArtista`) REFERENCES `artistas` (`id`) ON DELETE CASCADE,
  CONSTRAINT `idCancion` FOREIGN KEY (`idCancion`) REFERENCES `canciones` (`id`) ON DELETE CASCADE,
  CONSTRAINT `idGenero` FOREIGN KEY (`idGenero`) REFERENCES `generos` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genero_cancion`
--

LOCK TABLES `genero_cancion` WRITE;
/*!40000 ALTER TABLE `genero_cancion` DISABLE KEYS */;
/*!40000 ALTER TABLE `genero_cancion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `generos`
--

DROP TABLE IF EXISTS `generos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `generos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `descripcion` varchar(100) DEFAULT NULL,
  `idSubGenero` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idSubGenero_idx` (`idSubGenero`),
  CONSTRAINT `idSubGenero` FOREIGN KEY (`idSubGenero`) REFERENCES `generos` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `generos`
--

LOCK TABLES `generos` WRITE;
/*!40000 ALTER TABLE `generos` DISABLE KEYS */;
/*!40000 ALTER TABLE `generos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `playlist_cancion`
--

DROP TABLE IF EXISTS `playlist_cancion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `playlist_cancion` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idPlaylist` int NOT NULL,
  `idCancion` int NOT NULL,
  `total` int NOT NULL,
  `limite` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idCancion_idx` (`idCancion`),
  KEY `idPlaylistS_idx` (`idPlaylist`),
  CONSTRAINT `idCancionS` FOREIGN KEY (`idCancion`) REFERENCES `canciones` (`id`) ON DELETE CASCADE,
  CONSTRAINT `idPlaylistS` FOREIGN KEY (`idPlaylist`) REFERENCES `playlists` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `playlist_cancion`
--

LOCK TABLES `playlist_cancion` WRITE;
/*!40000 ALTER TABLE `playlist_cancion` DISABLE KEYS */;
/*!40000 ALTER TABLE `playlist_cancion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `playlists`
--

DROP TABLE IF EXISTS `playlists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `playlists` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `fechaCreacion` datetime NOT NULL,
  `privacidad` tinyint NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `playlists`
--

LOCK TABLES `playlists` WRITE;
/*!40000 ALTER TABLE `playlists` DISABLE KEYS */;
/*!40000 ALTER TABLE `playlists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_playlist`
--

DROP TABLE IF EXISTS `usuario_playlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario_playlist` (
  `id` int NOT NULL AUTO_INCREMENT,
  `idUsuario` int NOT NULL,
  `idPlaylist` int NOT NULL,
  `tipo_usuario` varchar(45) NOT NULL,
  `fechaUso` datetime DEFAULT NULL,
  `fechaModificacion` datetime DEFAULT NULL,
  `fechaEliminacion` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idUsuario_idx` (`idUsuario`),
  KEY `idPlaylist_idx` (`idPlaylist`),
  CONSTRAINT `idPlaylist` FOREIGN KEY (`idPlaylist`) REFERENCES `playlists` (`id`) ON DELETE CASCADE,
  CONSTRAINT `idUsuario` FOREIGN KEY (`idUsuario`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_playlist`
--

LOCK TABLES `usuario_playlist` WRITE;
/*!40000 ALTER TABLE `usuario_playlist` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario_playlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `alias` varchar(45) NOT NULL,
  `contrasenia` varchar(45) NOT NULL,
  `fotoPerfil` varchar(45) DEFAULT NULL,
  `pais` varchar(45) DEFAULT NULL,
  `idCuenta` int DEFAULT NULL,
  `email` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  UNIQUE KEY `alias_UNIQUE` (`alias`),
  KEY `idCuenta_idx` (`idCuenta`),
  CONSTRAINT `idCuenta` FOREIGN KEY (`idCuenta`) REFERENCES `cuentas` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Homero','e10adc3949ba59abbe56e057f20f883e',NULL,NULL,NULL,'homero@gmail.com');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-16 15:18:21
