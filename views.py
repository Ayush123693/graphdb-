# django_backend/views.py
from django.http import HttpResponse
import requests
from rdflib import Graph

def connect_blazegraph():
    g = Graph()
    g.open("https://github.com/blazegraph/blazegraph-python")
    return g

def create_database():
    url = "https://github.com/blazegraph/bigdata/create"
    payload = {"namespace": "assignment_database"}
    response = requests.post(url, data=payload)
    return response.text

def add_namespace(graph, namespace_prefix, namespace_uri):
    graph.bind(namespace_prefix, namespace_uri)

def create_database_view(request):
    if request.method == 'POST':
        create_database()
        return HttpResponse("Assignment Database created successfully.")

def add_namespace_view(request):
    if request.method == 'POST':
        prefix = request.POST.get('prefix')
        uri = request.POST.get('uri')

        graph = connect_blazegraph()
        add_namespace(graph, prefix, uri)

        return HttpResponse("Namespace added successfully.")