from mongoengine import connect
from person import Person

class PersonService():
    def __init__(self, db, host, port):
        connect(db, host=host, port=port)

    def get_all(self):
        return [{"name": p.name, "ssn": p.ssn} for p in Person.objects]

    def get(self, ssn):
        return [{"name": p.name, "ssn": p.ssn} for p in Person.objects(ssn=ssn)]

    def update(self, ssn, name):
        updated = []
        for person in Person.objects(ssn=ssn):
            person.name = name
            person.save()
            updated.append({"name": person.name, "ssn": person.ssn})
        return updated

    def delete(self, ssn):
        count = 0
        for person in Person.objects(ssn=ssn):
            person.delete()
            count += 1
        return count

    def create(self, person):
        if Person.objects(ssn=person.ssn).count() == 1:
            return {"message": "Person with ssn {} already exists.".format(person.ssn)}
        person.save()
        return {"name": person.name, "ssn": person.ssn}
