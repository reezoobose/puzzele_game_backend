# <editor-fold desc="Import .">
# -*- coding: utf-8 -*-
# Import Flask Rest Full.
from flask_restful import Resource, reqparse
from Model.tournamentmodel import TournamentModel
# </editor-fold>


# <editor-fold desc="Tournament Registration .">
# User class must inherit Resource to implement Post Methods .
class TournamentRegister(Resource):
    """
    Register an tournament to a database.
    """
    # create a parser.
    register_parser = reqparse.RequestParser( )
    # add arguments
    register_parser.add_argument('tournament_id', type=str, required=True, help="This field cannot be blank.")
    register_parser.add_argument('tournament_start_date', type=str, required=True, help="This field cannot be blank.")
    register_parser.add_argument('tournament_end_date', type=str, required=True, help="This field cannot be blank.")

    # post method .
    @staticmethod
    def post(cls):
        """
        Post Method for user registration.
        :return: Success code 1 on successful registration .
        """
        # get data from json.
        input_data = TournamentRegister.register_parser.parse_args( )
        # corresponding Tournament exist in database.
        if TournamentModel.get_tournament(input_data['tournament_id']) is None:
            # create Tournament.
            tournament = TournamentModel(tournament_id=input_data['tournament_id'], tournament_start_date=input_data[
                'tournament_start_date'],tournament_end_date=input_data['tournament_end_date'])
            # save user.
            tournament.save_data()
            return {'message': 'Tournament created ', 'Tournament_details': tournament.json(), 'Success_Code': 1}, 201
        else:
            return {'message': 'Tournament already present with the Tournament id', 'Success_Code': 0}, 400
# </editor-fold>


# ================================== Tournament Details ==================================

#  <editor-fold desc="Tournament Details .">
#  User class must inherit Resource to implement Post Methods .
class TournamentDetails(Resource):
    @staticmethod
    def get(cls):
    """
    Return all tournaments details.
    :param cls:
    :return:
    """
        tournment = TournamentModel.get_all_tornaments();
        if(tournment) is None:
            return {'message': 'No Tournament present', 'Success_Code': 0}, 400
        else:
            fulltournamentdetails = ""
            for item in tournament:
                fulltournamentdetails + = item.json()
        return {'message':'Tournament_details':fulltournamentdetails, 'Success_Code': 1}, 200
# </editor-fold>