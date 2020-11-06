from .client import ClientsApi, ClientApi
from .documento import DocumentosApi, DocumentoApi, DocumentosUsuarioApi, DocumentosTarifaApi


def initialize_routes(api):
    api.add_resource(ClientsApi, '/api/clients') 
    api.add_resource(ClientApi, '/api/client/<id>')
    api.add_resource(DocumentosApi, '/api/documentos')
    api.add_resource(DocumentoApi, '/api/documento/<id>')
    api.add_resource(DocumentosUsuarioApi, '/api/consultarDocumentosUsuario/<docUsuario>')
    api.add_resource(DocumentosTarifaApi, '/api/consultatTarifa/<id>')

