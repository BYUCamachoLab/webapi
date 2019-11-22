from django.http import Http404

from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Machine
from .serializers import MachineSerializer
from .permissions import IsOwnerOrReadOnly

class MachineList(mixins.ListModelMixin, 
                  generics.GenericAPIView):
    '''
    List all machines.
    '''
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class MachineDetail(APIView):
    '''
    Retrieve or update a machine.
    '''
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, id):
        try:
            return Machine.objects.get(pk=id)
        except Machine.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        machine = self.get_object(kwargs['pk'])
        serializer = MachineSerializer(machine)
        return Response(serializer.data)        

    def put(self, request, *args, **kwargs):
        machine = self.get_object(kwargs['pk'])
        serializer = MachineSerializer(machine, data=request.data, partial=True)
        self.check_object_permissions(self.request, machine)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
