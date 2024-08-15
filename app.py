# flask_backend/app.py
from flask import Flask, request
import requests
from rdflib import Graph

app = Flask(__name__)

def connect_blazegraph():
    g = Graph()
    g.open("https://github.com/blazegraph/blazegraph-python")
    return g

def create_database():
    url = "https://github.com/blazegraph/bigdata/create"
    payload = {"namespace": "assignment_database"}
    response = requests.post(url, data=payload)
    return response.text

@app.route('/create_database', methods=['POST'])
def create_database():
    if request.method == 'POST':
        create_database()
        return "Assignment Database created successfully."

@app.route('/add_namespace', methods=['POST'])
def add_namespace():
    if request.method == 'POST':
        prefix = request.form.get('prefix')
        uri = request.form.get('uri')

        graph = connect_blazegraph()
        add_namespace(graph, prefix, uri)

        return "Namespace added successfully."
        
if __name__ == '__main__':
    app.run(debug=True)