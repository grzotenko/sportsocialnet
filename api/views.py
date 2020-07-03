from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format=None):

    return Response({
        'TEST': reverse('test-test', request=request),
    })