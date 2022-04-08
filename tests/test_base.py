from flask_testing import TestCase
from flask import current_app, url_for

from main import app


class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False  # no vamos a usar el CSR Token de las forms porque no tenemos una seccion activa de usuario

        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)  # Valida si la aplicacion de flask existe

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])  # ver que la app esta en modo de testing

    def test_index_redirects(self):
        response = self.client.get(url_for('index'))  # queremos obtener la url de index

        self.assertRedirects(response, url_for('hello')) # redirige a hello

    def test_hello_get(self):
        response = self.client.get(url_for('hello'))  

        self.assert200(response)  # hello devuelve un 200 al hacer un get

    def test_hello_post(self):
        fake_form = {
            'username': 'fake',
            'password': 'fake-password'
        }
        response = self.client.post(url_for('hello'), data=fake_form)
        # import pdb; pdb.set_trace() # extra para prueba debugger: dir(response) y por ejemplo response.data
        self.assertRedirects(response, url_for('index'))  # al enviar un post redirects to index

    # Alguien dijo que algo asi para probar flashes
    def test_user_registered_flashed_message(self):
        fake_form = {
            'username': 'vijoin',
            'password': '123456'
        }
        self.client.post(url_for('index'), data=fake_form)
        message = 'User registered successfully'
        self.assert_message_flashed(message)
