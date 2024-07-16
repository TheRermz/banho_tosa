try:
    from connection.conn import Connection
except ModuleNotFoundError:
    from db.connection.conn import Connection
import pandas as pd


def start_connection():
    conn = Connection()
    return conn


def select_all_from_cliente():
    conn = start_connection()
    table = pd.read_sql_query(
        "SELECT ID_CLIENTE, NOME_CLIENTE, TELEFONE_CLIENTE, RUA, BAIRRO, NUMERO FROM CLIENTE",
        con=conn.connection,
    )
    new_table = table.to_dict()
    df = pd.DataFrame(new_table)
    json_table = df.to_json(orient="records")
    print(table)

    return json_table


def select_all_from_pet():
    conn = start_connection()
    table = pd.read_sql_query(
        """
SELECT P.ID_PET, C.NOME_CLIENTE, C.TELEFONE_CLIENTE  , P.NOME_PET , RACA_PET  FROM PET P
JOIN CLIENTE C ON C.ID_CLIENTE = P.FK_CLIENTE_ID_CLIENTE
""",
        con=conn.connection,
    )
    new_table = table.to_dict()
    df = pd.DataFrame(new_table)
    json_table = df.to_json(orient="records")
    print(table)

    return json_table


def select_all_from_venda():
    conn = start_connection()
    table = pd.read_sql_query(
        """
SELECT V.ID_VENDA ,V.TIPO_VENDA , V.DATA_VENDA , C.NOME_CLIENTE , P.NOME_PET  FROM VENDA V
JOIN CLIENTE C ON V.FK_CLIENTE_ID_CLIENTE = C.ID_CLIENTE
JOIN PET P ON P.ID_PET = V.FK_PET_ID_PET
ORDER BY ID_VENDA ASC""",
        con=conn.connection,
    )
    new_table = table.to_dict()
    df = pd.DataFrame(new_table)
    json_table = df.to_json(orient="records")
    print(table)

    return json_table


def select_cliente_pet():
    conn = start_connection()
    table = pd.read_sql_query(
        """
SELECT C.NOME_CLIENTE,
P.NOME_PET
FROM CLIENTE C
JOIN PET P ON P.FK_CLIENTE_ID_CLIENTE = C.ID_CLIENTE
""",
        con=conn.connection,
    )
    new_table = table.to_dict()
    df = pd.DataFrame(new_table)
    json_table = df.to_json(orient="records")
    print(table)

    return json_table


def select_cliente_by_nome(nome: str):
    conn = start_connection()
    table = pd.read_sql_query(
        f"""
SELECT C.NOME_CLIENTE, C.TELEFONE_CLIENTE, C.RUA, C.BAIRRO, C.NUMERO, P.NOME_PET FROM CLIENTE C JOIN PET P
ON P.FK_CLIENTE_ID_CLIENTE = C.ID_CLIENTE WHERE NOME_CLIENTE = '{nome}'
""",
        con=conn.connection,
    )
    new_table = table.to_dict()
    df = pd.DataFrame(new_table)
    json_table = df.to_json(orient="records")
    print(table)

    return json_table


def select_cliente_by_pet(nome_pet: str):
    conn = start_connection()
    table = pd.read_sql_query(
        f"""
SELECT C.NOME_CLIENTE, C.TELEFONE_CLIENTE, C.RUA, C.BAIRRO, C.NUMERO, P.NOME_PET FROM CLIENTE C
JOIN PET P
ON P.FK_CLIENTE_ID_CLIENTE = C.ID_CLIENTE
WHERE NOME_PET = '{nome_pet}'
""",
        con=conn.connection,
    )
    new_table = table.to_dict()
    df = pd.DataFrame(new_table)
    json_table = df.to_json(orient="records")
    print(table)

    return json_table


def select_pet_by_nome_cliente(nome_cliente: str):
    conn = start_connection()
    table = pd.read_sql_query(
        f"""
SELECT  C.NOME_CLIENTE, C.TELEFONE_CLIENTE, C.RUA, C.BAIRRO, C.NUMERO, P.NOME_PET FROM CLIENTE C
JOIN PET P
ON P.FK_CLIENTE_ID_CLIENTE = C.ID_CLIENTE
WHERE C.NOME_CLIENTE = '{nome_cliente}'
""",
        con=conn.connection,
    )
    new_table = table.to_dict()
    df = pd.DataFrame(new_table)
    json_table = df.to_json(orient="records")
    print(table)

    return json_table


def select_venda_by_cliente(nome_cliente: str):
    conn = start_connection()
    table = pd.read_sql_query(
        f"""

SELECT C.NOME_CLIENTE, P.NOME_PET, V.TIPO_VENDA, V.DATA_VENDA FROM VENDA V
JOIN CLIENTE C ON C.ID_CLIENTE = V.FK_CLIENTE_ID_CLIENTE
JOIN PET P ON V.FK_PET_ID_PET = P.ID_PET
WHERE C.NOME_CLIENTE = '{nome_cliente}'

""",
        con=conn.connection,
    )
    new_table = table.to_dict()
    df = pd.DataFrame(new_table)
    json_table = df.to_json(orient="records")
    print(table)

    return json_table


def select_venda_by_pet(nome_pet: str):
    conn = start_connection()
    table = pd.read_sql_query(
        f"""

SELECT C.NOME_CLIENTE, P.NOME_PET, V.TIPO_VENDA, V.DATA_VENDA FROM VENDA V
JOIN CLIENTE C ON C.ID_CLIENTE = V.FK_CLIENTE_ID_CLIENTE
JOIN PET P ON V.FK_PET_ID_PET = P.ID_PET
WHERE P.NOME_PET = '{nome_pet}'

""",
        con=conn.connection,
    )

    new_table = table.to_dict()
    df = pd.DataFrame(new_table)
    json_table = df.to_json(orient="records")
    print(table)

    return json_table


def insert_cliente(
    nome_cliente: str, telefone_cliente: str, rua: str, bairro: str, numero: int
):

    engine = start_connection().connection
    connection = engine.raw_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            f"""
        INSERT INTO CLIENTE (NOME_CLIENTE, TELEFONE_CLIENTE, RUA, BAIRRO, NUMERO)
        VALUES('{nome_cliente}', '{telefone_cliente}', '{rua}', '{bairro}', {numero})
        """
        )
        cursor.commit()
        return "Cliente inserido com sucesso!"
    except TypeError as e:
        cursor.rollback()
        return f"Erro ao inserir cliente: {e}"
    except KeyError as e:
        return f"Erro ao inserir cliente: {e}"


def insert_pet(nome_pet: str, raca_pet: str, nome_cliente: str):
    engine = start_connection().connection
    connection = engine.raw_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            f"""
        INSERT INTO PET (NOME_PET, RACA_PET, FK_CLIENTE_ID_CLIENTE)
        VALUES('{nome_pet}', '{raca_pet}', (SELECT ID_CLIENTE FROM CLIENTE WHERE NOME_CLIENTE = '{nome_cliente}'))
        """
        )
        cursor.commit()

        return "Pet inserido com sucesso!"
    except TypeError as e:
        return f"Erro ao inserir pet: {e}"
    except KeyError as e:
        return f"Erro ao inserir pet: {e}"


def insert_venda(tipo_venda: str, nome_cliente: str, nome_pet: str):
    engine = start_connection().connection
    connection = engine.raw_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            f"""
        INSERT INTO VENDA (TIPO_VENDA, FK_CLIENTE_ID_CLIENTE, FK_PET_ID_PET)
        VALUES('{tipo_venda}', (SELECT ID_CLIENTE FROM CLIENTE WHERE NOME_CLIENTE = '{nome_cliente}'), (SELECT ID_PET FROM PET WHERE NOME_PET = '{nome_pet}'))
        """
        )
        cursor.commit()
        return "Venda inserida com sucesso!"
    except TypeError as e:
        return f"Erro ao inserir venda: {e}"
    except KeyError as e:
        return f"Erro ao inserir venda: {e}"
