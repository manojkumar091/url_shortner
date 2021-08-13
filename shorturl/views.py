from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from shorturl.tinyurl import make_tiny

# API to get the shortened URL
class GetshortenURl(APIView):

    def get(self,request):
        
        #fetching the query params
        data = request.query_params

        url = data.get('url', None)

        if url is not None:

            #make_tiny function will shrink the URL and return it
            shorturl = make_tiny(url)

            return Response({'status': 'success', 'message': "URL shortened successfully", 'URL': shorturl}, status=status.HTTP_200_OK)

        else:
            return Response({'status': 'error', 'message': 'URL not found'}, status=status.HTTP_400_BAD_REQUEST)