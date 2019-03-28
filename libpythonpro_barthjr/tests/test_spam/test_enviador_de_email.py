import pytest

from libpythonpro_barthjr.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['email_test@email.com', 'email_remetente@email.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    destinatario = 'email_destinatario@email.com'
    assunto = 'Curso Python Pro'
    corpo = 'Aula sobre TDD no módulo Pytools'
    resultado = enviador.enviar(remetente, destinatario, assunto, corpo)
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'email_remetente']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    destinatario = 'email_destinatario@email.com'
    assunto = 'Curso Python Pro'
    corpo = 'Aula sobre TDD no módulo Pytools'
    with pytest.raises(EmailInvalido):
        enviador.enviar(remetente, destinatario, assunto, corpo)
