CREATE TABLE USUARI (
  id_usuari INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(100),
  email VARCHAR(100),
  password VARCHAR(100)
);

CREATE TABLE PISTA (
  id_pista INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(100),
  tipus VARCHAR(50),
  disponible BOOLEAN
);

CREATE TABLE RESERVA (
  id_reserva INT AUTO_INCREMENT PRIMARY KEY,
  data DATE,
  hora VARCHAR(20),
  id_usuari INT,
  id_pista INT,
  FOREIGN KEY (id_usuari) REFERENCES USUARI(id_usuari),
  FOREIGN KEY (id_pista) REFERENCES PISTA(id_pista)
);