from rest_framework import pagination
from rest_framework.response import Response
import decimal
import ipdb


class CustomPagination(pagination.PageNumberPagination):

    def get_sum_all(self, files_up):
        sum = 0
        for info in files_up:
            if (
                    info['type'] != 2 and
                    info['type'] != 3 and
                    info['type'] != 9):
                sum += decimal.Decimal(info['value'])
            else:
                sum -= decimal.Decimal(info['value'])

        return sum

    def get_paginated_response(self, data):

        param = list(self.request.query_params.keys())
        if len(param) != 0:
            return Response({
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'count': self.page.paginator.count,
                'sum_all_transactions': self.get_sum_all(data),
                'results': data
            })
        else:
            return Response({
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'count': self.page.paginator.count,
                'results': data
            })
