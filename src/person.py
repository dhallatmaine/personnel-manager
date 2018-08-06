from mongoengine import Document, StringField

class Person(Document):
    name = StringField(required=True)
    ssn = StringField(require=True)
