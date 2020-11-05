from flask import Response, request
from database.models import Documento
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource


class DocumentosApi(Resource):
    def get(self):
        documentos = Documento.objects().to_json()
        return Response(documentos, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        documento = Documento(**body).save()
        id = documento.id
        return {'id': str(id)}, 200


class DocumentoApi(Resource):
    def get(self, id):
        try:
            documento = Documento.objects.get(id=id).to_json()
            return Response(documento, mimetype="application/json", status=200)
        except Exception as error:
            return Response(error, status=400, mimetype='application/json')
        
class DocumentosUsuarioApi(Resource):
    def get(self, docUsuario):
        try:
            documento = Documento.objects.get(userDoc=docUsuario).to_json()
            return Response(documento, mimetype="application/json", status=200)
        except Exception as error:
            return Response(error, status=400, mimetype='application/json')
