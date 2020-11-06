""" Class representing a documento
    """
class Documento():

    def __init__(self, name, doc_id, tarifa):
        self.name = name        
        self.doc_id = doc_id
        self.tarifa = tarifa
        
    def get_docName(self):
        return self.name


if __name__ == '__main__':
    client_instance = Client('docName', '12345', '500000')
    print('Se incluyo un nuevo documento ')
