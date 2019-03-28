from libpythonpro_barthjr.spam.enviador_de_email import Enviador
from libpythonpro_barthjr.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'juniior.barth@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
