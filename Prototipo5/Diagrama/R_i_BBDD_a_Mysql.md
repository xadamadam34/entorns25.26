```mermaid
erDiagram

USUARI {
    int id_usuari PK
    string nom
    string email
    string password
}

RESERVA {
    int id_reserva PK
    date data
    string hora
    int id_usuari FK
    int id_pista FK
}

PISTA {
    int id_pista PK
    string nom
    string tipus
    boolean disponible
}

USUARI ||--o{ RESERVA : fa
PISTA ||--o{ RESERVA : te
