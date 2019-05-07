"""
__author__ = "Rahul kumar"
__version__ ="1.0"
__date__ = "May 7 15:48:15 2019"
__copyright__ = "©2019 rahul_kumar"

"""


import logging
from UserDetailsApp.models import User
from json import loads, dumps
import os
import sys

logger = logging.getLogger(__name__)


class DbQueries:

    @staticmethod
    def get_all_users():
        """
        this function gets all users from db

        :return:
        """
        user_details = None
        try:
            user_details = list(User.objects.filter().values())
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.error(str([exc_type, fname, exc_tb.tb_lineno]))
            logger.error(str(e))
        return user_details

    @staticmethod
    def get_selected_users(page, limit_item, name, age):
        """
        this function return a query data based on conditions

        :param page: page_number
        :param limit: max_limit or records
        :param name: first or last name
        :param sort: sort accending or decending
        :return:
        """
        user_selection_details_list = None
        try:
            query_dict = {"$or": [{"first_name": {"$regex" : ".*" + name + ".*"}}, {"last_name": {"$regex" : ".*" + name + ".*"}}]}
            projection_dict = {'_id': 0, 'id': 1,
                               'first_name': 1, 'last_name': 1,
                               'company_name': 1, 'city': 1,
                               'age': 1, 'state': 1,
                               'zip': 1, 'email': 1}
            order = 1
            sort_par = age
            if "-" in age:
                sort_par_list = age.split("-")
                sort_par = sort_par_list[1]
                order = -1
            user_selection_details = User.objects.mongo_find(query_dict, projection_dict).sort(sort_par, order).skip(limit_item*(page-1)).limit(limit_item)
            if user_selection_details:
                user_selection_details_list = [loads(dumps(data)) for data in user_selection_details]

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.error(str([exc_type, fname, exc_tb.tb_lineno]))
            logger.error(str(e))
        return user_selection_details_list

    @staticmethod
    def get_user_details_by_id(id):
        """
        this function gets user record by id

        :param id:
        :return:
        """
        user_data = None
        try:
            user_data = list(User.objects.filter(id=id).values())
            print(len(user_data))
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.error(str([exc_type, fname, exc_tb.tb_lineno]))
            logger.error(str(e))
        return user_data

    @staticmethod
    def update_user(id, data):
        """
        this function update user details

        :param id:
        :param data:
        :return:
        """
        status = 1000
        try:
            query_dict = {'$set': data}
            status = User.objects.mongo_update({'id': int(id)}, query_dict)
            if status['nModified']:
                status = 200
            else:
                status = "no records are in db for id " + str(id)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.error(str([exc_type, fname, exc_tb.tb_lineno]))
            logger.error(str(e))
        return status

    @staticmethod
    def delete_user(id):
        status =  1000
        try:
            status = User.objects.filter(id=id).delete()
            if status[1]['UserDetailsApp.User']:
                status = 200
            else:
                status = "no records are in db for id " + str(id)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logger.error(str([exc_type, fname, exc_tb.tb_lineno]))
            logger.error(str(e))
        return status
