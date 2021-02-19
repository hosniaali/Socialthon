from .models import *
from rest_framework.response import Response
from rest_framework import generics, permissions
from .serializers import *


class ChatbotAPI(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = [UserInfoSerializer, DonationsSerializer, ]

    def post(self, request):
        action = request.data.get('action')

        if action == 'get_user':
            id_no = request.data.get('id_no')
            user = Users.objects.get(id_no=id_no)
            if user:
                return Response({
                    'is_exsist': True,
                    'user': UserInfoSerializer(user).data,
                })
            else:
                return Response({
                    'is_exsist': False,
                })

        elif action == 'add_user':
            id_no = request.data.get('id_no')
            phone_no = request.data.get('phone_no')
            region = request.data.get('region')
            age = request.data.get('age')
            gender = request.data.get('gender')

            donated_type = request.data.get('donated_type')
            segment_type = request.data.get('segment_type')
            status = 1

            user = Users.objects.get_or_create(id_no=id_no, phone_no=phone_no, region=region, age=age, gender=gender)
            donated = Donations.objects.create(user=user[0], donated_type_id=donated_type, segment_type_id=segment_type,
                                               status=status)

            if user and donated:
                return Response({
                    'message': 'user has been added successfully',
                })
            else:
                return Response({
                    'message': 'user has not added',
                })

        elif action == 'get_status':
            id = request.data.get('id')
            status = Donations.objects.get(id=id)

            if status:
                return Response({
                    'status': DonationsSerializer(status).data,
                })

