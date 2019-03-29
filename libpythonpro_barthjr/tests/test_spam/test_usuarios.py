from libpythonpro_barthjr.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Barth')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Barth'), Usuario(nome='Junior')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
