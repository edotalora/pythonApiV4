import unittest

from service.documento import Documento


class DocumentoTestCase(unittest.TestCase):
    def setUp(self):
        self.test_documento = Documento('docName', '12345', '500000')

    def test_name_docName(self):
        expected_name = 'miDocName'
        self.assertEqual(self.test_client.get_docName(), expected_name)


if __name__ == '__main__':
    unittest.main()
    #unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
    # python -m unittest discover -s test -p "*_test.py"
    # https://stackoverflow.com/questions/11241781/python-unittests-in-jenkins
