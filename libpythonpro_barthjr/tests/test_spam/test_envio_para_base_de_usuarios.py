import pytest

from libpythonpro_barthjr.spam.enviador_de_email import Enviador
from libpythonpro_barthjr.spam.main import EnviadorDeSpam
from libpythonpro_barthjr.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Barth', email='barth@gmail.com'),
            Usuario(nome='Junior', email='juniior@gmail.com')
        ],
        [
            Usuario(nome='Barth', email='barth@gmail.com'),
        ]
    ]
)
def test_qtde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'juniior.barth@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados
