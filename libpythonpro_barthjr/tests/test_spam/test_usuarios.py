from libpythonpro_barthjr.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Barth', email='juniior.barth@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Barth', email='barth@gmail.com'), Usuario(nome='Junior', email='juniior@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
