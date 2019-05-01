# <editor-fold desc="Imports.">
# -*- coding: utf-8 -*-
# import flask .
from flask import Flask
#  Import Flask RestFull
from flask_restful import Api
# get access to os variable .
import os
# </editor-fold>


# assign a flask app name .
app = Flask(__name__)
# add Flask restFull.
api = Api()

# <editor-fold desc="App configuration ">
# ---------App configuration-----------
# allow app to debug .
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['TRAP_HTTP_EXCEPTIONS '] = True
app.config['TRAP_BAD_REQUEST_ERRORS '] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# ----------App configuration-----------
# </editor-fold>


# Register all Resources .
def register_api():
    """attaches api routes to the flask app"""
    api.app = app
    # import user register
    from Resources.user import UserRegister, LeaderBoard, UpdateUserMoney, UerUniqueId , SchoolLeaderBoard
    from Resources.tournament import  TournamentRegister,TournamentDetails, RemoveTournament
    api.add_resource(UserRegister, '/Register')
    api.add_resource(LeaderBoard, '/LeaderBoard')
    api.add_resource(UpdateUserMoney, '/SetMoney')
    api.add_resource(UerUniqueId, '/Getid')
    api.add_resource(SchoolLeaderBoard,'/SchoolLeaderBoard')
    api.add_resource(TournamentRegister, '/TournamentRegister')
    api.add_resource(TournamentDetails, '/TournamentDetails')
    api.add_resource(RemoveTournament, '/RemoveTournament')



# register all end points .
register_api()

# if tha app is run from this file app,py then name will be assigned as __main__ .
if __name__ == '__main__':
    # import sql alchemy object from sql alchemy extension .
    from sql_alchemy_extension import sql_alchemy
    # initialize the alchemy
    sql_alchemy.init_app(app)
    app.run(port=5000, debug=True)
