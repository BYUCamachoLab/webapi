# from django.shortcuts import render

# from rest_framework import viewsets, permissions

# from .serializers import MachineSerializer
# from .models import Machine

# class MachineViewSet(viewsets.ModelViewSet):
#     queryset = Machine.objects.all().order_by('alias')
#     serializer_class = MachineSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]





# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from .models import Machine
# from .serializers import MachineSerializer

# @api_view(['GET', 'POST'])
# def machine_list(request):
#     """
#     List all machines.
#     """
#     if request.method == 'GET':
#         machines = Machine.objects.all()
#         serializer = MachineSerializer(machines, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = MachineSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT'])
# def machine_detail(request, id):
#     '''
#     Retrieve or update a machine.
#     '''
#     try:
#         machine = Machine.objects.get(pk=id)
#     except Machine.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = MachineSerializer(machine)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = MachineSerializer(machine, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




from django.http import Http404

from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Machine
from .serializers import MachineSerializer

class MachineList(mixins.ListModelMixin, 
                  mixins.CreateModelMixin, 
                  generics.GenericAPIView): #(APIView)
    '''
    List all machines.
    '''
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

    def get(self, request, *args, **kwargs):
        # machines = Machine.objects.all()
        # serializer = MachineSerializer(machines, many=True)
        # return Response(serializer.data)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # serializer = MachineSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)

class MachineDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView): #(APIView)
    '''
    Retrieve or update a machine.
    '''
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

    # def get_object(self, id):
    #     try:
    #         return Machine.objects.get(pk=id)
    #     except Machine.DoesNotExist:
    #         raise Http404

    def get(self, request, *args, **kwargs):
        # machine = self.get_object(id)
        # serializer = MachineSerializer(machine)
        # return Response(serializer.data)        
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # machine = self.get_object(id)
        # serializer = MachineSerializer(machine, data=request.data, partial=True)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return self.update(request, *args, **kwargs)
