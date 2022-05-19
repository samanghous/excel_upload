from hashlib import new
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ExcelDataSerializer
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
            imported_data = dataset.load(new_excel.read(),format='xlsx')

            for data in imported_data:
                if data[0]:
                    excel_data = ExcelData.objects.filter(id=int(data[0])).first()
                    if excel_data:
                        serializer = ExcelDataSerializer(instance=excel_data, data={'name':data[1],'age':int(data[2]),'hobby':data[3]}, partial=True)
                        if serializer.is_valid(raise_exception=True):
                            serializer.save()       
                        else:
                            error = next(iter(serializer.errors))
                            response["messagae"] = serializer.errors[str(error)][0]
                            return Response(response, status=status.HTTP_400_BAD_REQUEST)
                else:
                    excel_data=ExcelData(name=data[1],age=int(data[2]),hobby=data[3])
                    excel_data.save()

            response['message'] = "data base created using excel data"
            return Response(response, status=status.HTTP_201_CREATED)

        except Exception as e:
            response['message'] = str(e)
            response['status'] = False
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
