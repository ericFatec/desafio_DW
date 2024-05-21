USE clientes;

CREATE TABLE agendamentos(
    id int AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    sobrenome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    telefone CHAR(15) NOT NULL,
    data_visita DATE NOT NULL,
    destino VARCHAR(255) NOT NULL
);

