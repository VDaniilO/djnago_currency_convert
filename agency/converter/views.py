from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

import requests as req


class ConvertView(APIView):

    @staticmethod
    def convert(value_from: str, value_to: str) -> int:
        url = f'https://api.exchangerate.host/convert?from={value_from}&to={value_to}'
        return req.get(url).json()["result"]

    def get(self, request, format=None):

        if request.query_params:
            value_from = self.request.query_params.get('from')
            value_to = self.request.query_params.get('to')
            response = self.convert(value_from, value_to)

            if self.request.query_params.get('value'):
                count = int(self.request.query_params.get('value'))
                return Response({'result': response * count})

            return Response({'result': response})

        else:
            return Response('Value is empty')
