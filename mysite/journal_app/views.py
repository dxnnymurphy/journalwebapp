from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import Max, Q
from .models import journal 
from .serializers import *
import operator
from functools import reduce

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

@api_view(['GET', 'POST'])
def journals_list(request, filter=None):
    if request.method == 'GET':
        if(filter):
            print('I am being called')
            data = journal.objects.filter(title__contains=filter)
        else:
            data = journal.objects.all()
        serializer = journalSerializer(
            data, context={'request': request}, many=True)
        print(serializer.data)

        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        data['id'] = journal.objects.all().aggregate(Max('id'))['id__max'] + 1
        techList = []
        for i in range(len(data['technologies'])):
            techList.append(data['technologies'][i]['label'])
        data['technologiesList'] = techList
        serializer = journalSerializer(data=data)
        print(data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def journals_detail(request, pk):
    try:
        entry = journal.objects.get(pk=pk)
    except journal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        data = request.data
        techList = []
        for i in range(len(data['technologies'])):
            techList.append(data['technologies'][i]['label'])
        data['technologiesList'] = techList
        print(data)
        serializer = journalSerializer(
            entry, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        print('we are deleting')
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def journals_filter(request, filter=None):
    if request.method == 'POST':
        if(filter):
            searchterm = request.data['term']
            techList = []
            for i in range(len(request.data['techList'])):
                techList.append(request.data['techList'][i]['label'])
            print(techList)
            if techList and searchterm:
                data = journal.objects.filter(title__contains=searchterm).filter(reduce(operator.or_, (Q(technologiesList__contains=x) for x in techList)))
                print('both')
            elif searchterm:
                data = journal.objects.filter(title__contains=searchterm)
            elif techList:
                data = journal.objects.filter(reduce(operator.or_, (Q(technologiesList__contains=x) for x in techList)))
        else:
            data = journal.objects.all()
        serializer = journalSerializer(data, context={'request': request}, many=True)
        print(serializer.data)

    return Response(serializer.data)

