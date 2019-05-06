"""
__author__ = "Rahul kumar"
__version__ ="1.0"
__date__ = "May 7 15:48:15 2019"
__copyright__ = "©2019 rahul_kumar"

"""

from rest_framework.response import Response
from rest_framework.views import APIView
import os
import sys
import logging
from UserDetailsApp.seri import UserSerializer
from UserDetailsApp.information_retrival import DbQueries
from django.utils.datastructures import MultiValueDictKeyError


logger = logging.getLogger(__name__)


class UserDetails(APIView):

    def post(self, request):
        """

        :param request:
        :return:
        """
        status = 404
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                status = 200
            else:
                status = serializer.errors
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.error(str([exc_type, fname, exc_tb.tb_lineno]))
            logger.error(str(e))
        return Response(status)

    def get(self, request):
        """

        :param request:
        :return:
        """
        user_data = None
        try:
            try:
                name = request.GET['name']
                limit = int(request.GET['limit'])
                page = int(request.GET['page'])
                sort = request.GET['sort']
                user_data = DbQueries.get_selected_users(page, limit, name, sort)
            except MultiValueDictKeyError:
                user_data = DbQueries.get_all_users()
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.error(str([exc_type, fname, exc_tb.tb_lineno]))
            logger.error(str(e))
        return Response(user_data)


class UserQueryWithId(APIView):

    def get(self, request, id):
        """

        :param request:
        :return:
        """
        user_data = None
        try:
            user_data = DbQueries.get_user_details_by_id(id)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.error(str([exc_type, fname, exc_tb.tb_lineno]))
            logger.error(str(e))
        return Response(user_data)

    def put(self, request, id):
        """

        :param request:
        :param id:
        :return:
        """
        status = 1000
        try:
            data = request.data
            status = DbQueries.update_user(id, data)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.error(str([exc_type, fname, exc_tb.tb_lineno]))
            logger.error(str(e))
        return Response(status)

    def delete(self, request, id):
        """

        :param request:
        :param id:
        :return:
        """
        status = 1000
        try:
            data = request.data
            print(data)
            status = DbQueries.delete_user(id)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.error(str([exc_type, fname, exc_tb.tb_lineno]))
            logger.error(str(e))
        return Response(status)