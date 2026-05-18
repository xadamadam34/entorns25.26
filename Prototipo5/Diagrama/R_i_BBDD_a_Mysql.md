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
    string hora_inici
    string hora_fi
    int id_usuari FK
    int id_schedule FK
}

SCHEDULE {
    int id_schedule PK
    date data
    string hora_inici
    string hora_fi
    int id_pista FK
}

PISTA {
    int id_pista PK
    string nom
    string tipus
    boolean disponible
    int id_centre FK
}

CENTRE {
    int id_centre PK
    string nom
    string ubicacio
    string ciutat
}

%% RELACIONS

USUARI ||--o{ RESERVA : fa
RESERVA }o--|| SCHEDULE : usa
SCHEDULE }o--|| PISTA : defineix
PISTA }o--|| CENTRE : pertany
