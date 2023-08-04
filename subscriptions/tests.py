from django.test import TestCase
from subscriptions.forms import SubscriptionForm

class SubscriptionsTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        """GET /inscricao/ must return status_code 200"""
        self.assertEqual(200, self.response.status.code)

    def test_template(self):
        """Must use subscription/subscriptions_form.html"""
        self.assertTemplateUsed(self.response, 'subscription/subscriptions_form.html')

    def test_html(self):
        """HTML must contain input tags"""
        self.assertContains(self.response, "<form")
        self.assertContains(self.response, "<input", 5)
        self.assertContains(self.response, 'type="text"', 3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """HMTL must contain csrf"""
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.response.context("form")
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        form = self.response.context('form')
        self.assertSequenceEqual('name', 'cpf', 'email', 'phone'), list(form.fields)