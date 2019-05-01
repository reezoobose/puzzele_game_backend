# <editor-fold desc="Import">
# -*- coding: utf-8 -*-
# import sql alchemy object .
from sql_alchemy_extension import sql_alchemy as db
# </editor-fold>

class TournamentModel(db.Model):
    # <editor-fold desc="Database Table Connection and Coloumn Details">
    """
    object representation of the tournament .
    inherit from Sql_alchemy model .
    """
    #  crete the table to store user model.
    __tabalename_ = 'tournament'
    # tournament Id.
    tournament_id = db.Column(db.String(30), primary_key=True)
    # tournament start date .
    tournament_start_date = db.Column(db.String(30))
    # tournament end date .
    tournament_end_date = db.Column(db.String(30))
    # </editor-fold>

    # <editor-fold desc="Class Methods">
    # region for classMethod



    # <editor-fold desc="Constructor">
    # constructor
    def __init__(self,tournament_id,tournament_start_date,tournament_end_date):
        """
        create a tornament .
        :param tournament_id: Tornament unique id .
        :param tournament_start_date: Tournament Start date .
        :param tournament_start_date: Tournament End date .
        """
        self.tournament_id = tournament_id
        self.tournament_start_date = tournament_start_date
        self.tournament_end_date = tournament_end_date
    # </editor-fold>


    # </editor-fold>

    # <editor-fold desc="Class Methods">
    # region for classMethod
    # Find All tournament
    @classmethod
    def get_all_tournaments(cls):
        return  cls.query.order_by(cls.tournament_id).all()

    # get particular tournament .
    @classmethod
    def get_tournament(cls,tournament_id):
        return cls.query.filter_by(tournament_id=tournament_id).all( )


    # <editor-fold desc="Instance Methods">
    # Save the Object in the data base .
    def save_data(self):
        """
        Save data to database .
        :return: null .
        """
        db.session.add(self)
        db.session.commit( )

    #  Remove the data from the data base .
    def remove_data(self):
        """
        Remove data from the database .
        :return: null.
        """
        db.session.delete(self)
        db.session.commit( )

    # To json
    def json(self):
        """
        convert in to json format .
        :return: json formatted user data .
        """
        return {'tournament_id': self.tournament_id,
                'tournament_start_date': self.tournament_start_date,
                'tournament_end_date': self.tournament_end_date
                }
    # </editor-fold>