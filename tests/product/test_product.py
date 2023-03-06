from inventory_report.inventory.product import Product


def test_cria_produto():
    data = Product(
        1,
        "star_industries",
        "mark_04",
        "2015",
        "2017",
        "sexta-feira",
        "cuidado possui o poder do sol",
    )

    assert data.id == 1
    assert data.nome_da_empresa == "star_industries"
    assert data.nome_da_empresa == "star_industries"
    assert data.data_de_fabricacao == "2015"
    assert data.data_de_validade == "2017"
    assert data.numero_de_serie == "sexta-feira"
    assert data.instrucoes_de_armazenamento == "cuidado possui o poder do sol"
