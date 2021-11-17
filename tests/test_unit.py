from flask_testing import TestCase
from application import app, db
from flask import url_for
from application.models import Tasks

class TestBase(TestCase):
    
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app


    def setUp(self):
        # Will be called before every test
        db.create_all()
        
        db.session.add(Tasks(description="Run unit tests"))
        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):
    #test whether we get correct response from routes 
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)

    def test_add_get(self):
        response = self.client.get(url_for('add'))
        self.assert200(response)

    def test_read_get(self):
        response = self.client.get(url_for('read_tasks'))
        self.assert200(response)

    def test_update_get(self):
        response = self.client.get(url_for('update', id=1))
        self.assert200(response)

    def test_all_complete_get(self):
        response = self.client.get(url_for('all_complete'))
        self.assert200(response)

    def test_incomplete_list_get(self):
        response = self.client.get(url_for('incomplete_list'))
        self.assert200(response)

class TestRead(TestBase):

    def test_read_home_tasks(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b"Run unit tests", response.data)

    def test_read_tasks_dict(self):
        response = self.client.get(url_for('read_tasks'))
        self.assertIn(b"Run unit tests", response.data)

class TestCreate(TestBase):

    def test_create_task(self):
        response = self.client.post(url_for('add'), data={"description": "Testing create functionality"}, 
        follow_redirects=True
        )
        self.assertIn(b"Testing create functionality", response.data)


