INSERT INTO PET(NOME_PET, RACA_PET, FK_CLIENTE_ID_CLIENTE)
VALUES(
        'CIGARRO',
        'SHITZU',
        (
            SELECT ID_CLIENTE
            FROM CLIETE
            WHERE NOME_CLIENTE = 'MURILO'
        )
    );
