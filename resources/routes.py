from .client import ClientsApi, ClientApi
from .documento import DocumentosApi, DocumentoApi


def initialize_routes(api):
    api.add_resource(ClientsApi, '/api/clients') 
    api.add_resource(ClientApi, '/api/client/<id>')
    api.add_resource(DocumentoApi, '/api/documentos')
    api.add_resource(DocumentoApi, '/api/documento/<id>')

