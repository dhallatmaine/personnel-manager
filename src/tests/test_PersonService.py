from mongoengine import connect
from person import Person
from person_service import PersonService


class TestPersonService:

    def setup_method(self):
        self.person_service = PersonService('testdb', host="mongomock://localhost", port=27017)
        self.db = connect('testdb', host="mongomock://localhost", port=27017)

    def teardown_method(self):
        self.db.drop_database('testdb')
        self.db.close()

    def test_create(self):
        person = self._create("Fred", "123")
        self._create("Bill", "123")
        assert 1 == Person.objects.count()
        assert Person.objects.first().name == person.name

    def test_update(self):
        self.test_create()
        self.person_service.update("123", "Updated")
        assert 1 == Person.objects.count()
        assert Person.objects.first().name == "Updated"

    def test_delete(self):
        self.test_create()
        self.person_service.delete("123")
        assert 0 == Person.objects.count()

    def test_get_all(self):
        self._create("Fred", "123")
        self._create("Tina", "456")
        results = self.person_service.get_all()
        assert 2 == len(results)

    def test_get(self):
        self._create("Fred", "123")
        self._create("Tina", "456")
        results = self.person_service.get("456")
        assert 1 == len(results)

    def _create(self, name, ssn):
        person = Person(name, ssn)
        self.person_service.create(person)
        return person
