import logging

from django.http import HttpRequest, HttpResponse
from rest_framework import permissions, viewsets
from rest_framework.authentication import BasicAuthentication

from .decorators import track_db_latency
from .models import Student
from .serializer import StudentSerializer

logger = logging.getLogger(__name__)


@track_db_latency("index")
def index(request):
    logger.info("ПОООН")
    return HttpResponse("Hello, this is the kvali_app index page.")



def create_viewset(model_class, serializer):
    class ViewSet(viewsets.ModelViewSet):
        queryset = model_class.objects.all()
        serializer_class = serializer

        @track_db_latency(f"{model_class.__name__}_create")
        def create(self, request, *args, **kwargs):
            return super().create(request, *args, **kwargs)

        @track_db_latency(f"{model_class.__name__}_list")
        def list(self, request, *args, **kwargs):
            return super().list(request, *args, **kwargs)

        @track_db_latency(f"{model_class.__name__}_retrieve")
        def retrieve(self, request, *args, **kwargs):
            return super().retrieve(request, *args, **kwargs)

        @track_db_latency(f"{model_class.__name__}_update")
        def update(self, request, *args, **kwargs):
            return super().update(request, *args, **kwargs)

        @track_db_latency(f"{model_class.__name__}_destroy")
        def destroy(self, request, *args, **kwargs):
            return super().destroy(request, *args, **kwargs)

    return ViewSet


StudentViewSet = create_viewset(Student, StudentSerializer)
