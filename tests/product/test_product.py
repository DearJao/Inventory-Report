from inventory_report.inventory.product import Product


def test_cria_produto():
    data = Product(
        1,
        "mark_04",
        "star_industries",
        "22/02/2022",
        "23/03/2023",
        "0007",
        "cuidado possui o poder do sol",
    )

    assert data.id == 1
    assert data.nome_do_produto == "mark_04"
    assert data.nome_da_empresa == "star_industries"
    assert data.data_de_fabricacao == "22/02/2022"
    assert data.data_de_validade == "23/03/2023"
    assert data.numero_de_serie == "0007"
    assert data.instrucoes_de_armazenamento == "cuidado possui o poder do sol"
