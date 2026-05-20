-- Crear base de dades
CREATE DATABASE IF NOT EXISTS reserva_pistes;
USE reserva_pistes;

-- Taula CENTRE
CREATE TABLE IF NOT EXISTS CENTRE (
    id_centre  INT AUTO_INCREMENT PRIMARY KEY,
    nom        VARCHAR(100) NOT NULL,
    ubicacio   VARCHAR(150) NOT NULL,
    ciutat     VARCHAR(100) NOT NULL
);

-- Taula PISTA
CREATE TABLE IF NOT EXISTS PISTA (
    id_pista   INT AUTO_INCREMENT PRIMARY KEY,
    nom        VARCHAR(100) NOT NULL,
    tipus      VARCHAR(50)  NOT NULL,
    disponible TINYINT(1)   NOT NULL DEFAULT 1,
    id_centre  INT          NOT NULL,
    FOREIGN KEY (id_centre) REFERENCES CENTRE(id_centre) ON DELETE CASCADE
);

-- Taula USUARI
CREATE TABLE IF NOT EXISTS USUARI (
    id_usuari  INT AUTO_INCREMENT PRIMARY KEY,
    nom        VARCHAR(100) NOT NULL,
    email      VARCHAR(150) NOT NULL UNIQUE,
    password   VARCHAR(255) NOT NULL
);

-- Taula SCHEDULE
CREATE TABLE IF NOT EXISTS SCHEDULE (
    id_schedule INT  AUTO_INCREMENT PRIMARY KEY,
    data        DATE NOT NULL,
    hora_inici  TIME NOT NULL,
    hora_fi     TIME NOT NULL,
    id_pista    INT  NOT NULL,
    FOREIGN KEY (id_pista) REFERENCES PISTA(id_pista) ON DELETE CASCADE
);

-- Taula RESERVA
CREATE TABLE IF NOT EXISTS RESERVA (
    id_reserva  INT AUTO_INCREMENT PRIMARY KEY,
    data        DATE NOT NULL,
    hora_inici  TIME NOT NULL,
    hora_fi     TIME NOT NULL,
    id_usuari   INT  NOT NULL,
    id_schedule INT  NOT NULL,
    FOREIGN KEY (id_usuari)   REFERENCES USUARI(id_usuari)     ON DELETE CASCADE,
    FOREIGN KEY (id_schedule) REFERENCES SCHEDULE(id_schedule) ON DELETE CASCADE
);

-- Dades de prova
INSERT INTO CENTRE (nom, ubicacio, ciutat) VALUES
    ('Centre Esportiu Nord', 'Carrer Major 10', 'Barcelona'),
    ('Centre Esportiu Sud',  'Avinguda Paral·lel 55', 'Barcelona');

INSERT INTO PISTA (nom, tipus, disponible, id_centre) VALUES
    ('Pista 1 - Futbol',  'Futbol',  1, 1),
    ('Pista 2 - Pàdel',   'Padel',   1, 1),
    ('Pista 3 - Bàsquet', 'Basquet', 1, 2),
    ('Pista 4 - Pàdel',   'Padel',   1, 2);

INSERT INTO SCHEDULE (data, hora_inici, hora_fi, id_pista) VALUES
    ('2026-05-20', '09:00:00', '10:00:00', 1),
    ('2026-05-20', '10:00:00', '11:00:00', 1),
    ('2026-05-20', '09:00:00', '10:00:00', 2),
    ('2026-05-20', '11:00:00', '12:00:00', 3),
    ('2026-05-21', '09:00:00', '10:00:00', 4);
