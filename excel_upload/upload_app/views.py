from hashlib import new
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from tablib import Dataset
from .models import ExcelData

class UploadApi(APIView):
    """ API for uploading excel file"""

    authentication_classes = []
    permission_classes = []

    def post(self, request):
        """ API method for uploading excel file """
        response = {}
        try:
            dataset = Dataset()
            new_excel = request.FILES['myfile']
            print(new_excel.name)
            imported_data = dataset.load(new_excel.read(),format='xlsx')

            for data in imported_data:
                excel_data=ExcelData(name=data[0],age=int(data[1]),hobby=data[2])
                excel_data.save()

            response['message'] = "data base created using excel data"
            return Response(response, status=status.HTTP_200_OK)
                     
           
        except Exception as e:
            response['message'] = str(e)
            response['status'] = False
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
