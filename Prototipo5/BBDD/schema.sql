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

CREATE TABLE SCHEDULE (
  id_schedule INT AUTO_INCREMENT PRIMARY KEY,
  id_pista INT,
  hora_inici TIME,
  hora_fi TIME,
  disponible BOOLEAN,
  FOREIGN KEY (id_pista) REFERENCES PISTA(id_pista)
);

CREATE TABLE CENTRE (
  id_centre INT AUTO_INCREMENT PRIMARY KEY,
  id_usuari INT,
  id_pista INT,
  id_schedule INT,
  data DATE,
  hora_inici TIME,
  hora_fi TIME,
  FOREIGN KEY (id_usuari) REFERENCES USUARI(id_usuari),
  FOREIGN KEY (id_pista) REFERENCES PISTA(id_pista),
  FOREIGN KEY (id_schedule) REFERENCES SCHEDULE(id_schedule)
);
