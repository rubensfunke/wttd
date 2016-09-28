from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Rubens Funke', cpf='12345678901',
                    email='rubens@funke.net', phone='41-8469-9559')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]


    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_to(self):
        expect = ['contato@eventex.com.br', 'rubens@funke.net']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Rubens Funke',
            '12345678901',
            'rubens@funke.net',
            '41-8469-9559',
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
