import os
from flask import Flask, jsonify, request, make_response
from person import Person
from person_service import PersonService

app = Flask(__name__)


@app.route('/', methods=['GET'])
def all():
    output = person_service.get_all()
    return jsonify({"result": output})


@app.route('/person/<ssn>', methods=['GET'])
def get(ssn):
    output = person_service.get(ssn)
    return jsonify({"result": output})


@app.route('/person/<ssn>', methods=['PUT'])
def put(ssn):
    output = person_service.update(ssn, request.json['name'])
    return jsonify({"result": output})


@app.route('/person/<ssn>', methods=['DELETE'])
def delete(ssn):
    count = person_service.delete(ssn)
    return jsonify({"result": {"deleted_count": count}})


@app.route('/person', methods=['POST'])
def post():
    person = Person(name=request.json['name'], ssn=request.json['ssn'])
    output = person_service.create(person)
    return make_response(jsonify({"result": output}), 400 if output.get('message') else 201)


if __name__ == '__main__':
    host = "mongodb://localhost"

    if os.environ.get('IN_DOCKER_CONTAINER', False):
        host = os.environ['DB_PORT_27017_TCP_ADDR']

    person_service = PersonService('peopledb', host=host, port=27017)

    app.run(debug=True, host='0.0.0.0')
