# <editor-fold desc="Import .">
# -*- coding: utf-8 -*-
# Import Flask Rest Full.
from flask_restful import Resource, reqparse
from Model.usermodel import UserModel
# </editor-fold>

# ---------------------------------------------------------------------- User Registration---------------------------#


# <editor-fold desc="User Registration .">
# User class must inherit Resource to implement Post Methods .
class UserRegister(Resource):
    """
    Register an user to a database if user do not present with the unique user id .
    """
    # create a parser.
    register_parser = reqparse.RequestParser( )
    # add arguments
    register_parser.add_argument('user_id', type=str, required=True, help="This field cannot be blank.")
    register_parser.add_argument('school_id', type=str, required=True, help="This field cannot be blank.")
    register_parser.add_argument('us_dollar', type=str, required=True, help="This field cannot be blank.")

    # post method .
    @staticmethod
    def post():
        """
        Post Method for user registration.
        :return: Success code 1 on successful registration .
        """
        # get data from json.
        input_data = UserRegister.register_parser.parse_args( )
        # corresponding user exist in database
        if UserModel.find_user(input_data['user_id']) is None:
            # create user.
            user = UserModel(user_unique_identifier=input_data['user_id'], school_id=input_data['school_id'],
                             us_dollar=input_data['us_dollar'])
            # save user.
            user.save_data()
            return {'message': 'user created ', 'user_details': user.json(), 'Success_Code': 1}, 201
        else:
            return {'message': 'user already present with the user id', 'Success_Code': 0}, 400
# </editor-fold>


# ---------------------------------------------------------------------- User Leader Board---------------------------#

# <editor-fold desc="Leader Board">
# Fetch data for leader Board
class LeaderBoard(Resource):
    """
    Leader Board Resources .
    contain  a post method .
    """
    @classmethod
    def post(cls):
        """
        Post method
        """
        # return list of  users
        return UserModel.user_leader_board()
# </editor-fold>

# ---------------------------------------------------------------------- User Money update---------------------------#


# <editor-fold desc="update In game currency">
class UpdateUserMoney(Resource):
    """
    update user Money .
    """
    # create a parser.
    update_user_money = reqparse.RequestParser()
    # add arguments
    update_user_money.add_argument('us_dollar', type=str, required=True, help="This field cannot be blank.")
    update_user_money.add_argument('user_id', type=str, required=True, help="This field cannot be blank.")

    @classmethod
    def post(cls):
        """
        make a post with uuid  and updated money .
        it will update the us_dollar value in the database .
        :return: update user .
        Example: post contain json {'uuid':'420','us_dollar':'1000000000000'}
        """
        # input data.
        input_data = UpdateUserMoney.update_user_money.parse_args()
        # email id .
        user = UserModel.find_user(input_data['user_id'])
        # if user found.
        if user is not None:
            user.us_dollar = input_data['us_dollar']
            user.save_data()
            return {'message': user.json(), 'Success_Code': 1}, 200
        return {'message': 'No user found with this email id ', 'Success_Code': 0}, 404
# </editor-fold>

