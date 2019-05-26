# <editor-fold desc="Import">
# -*- coding: utf-8 -*-
# import sql alchemy object .
from sql_alchemy_extension import sql_alchemy as db
from sqlalchemy import desc
# </editor-fold>


# class must inherit Model from sql Alchemy .
class UserModel(db.Model):
    # <editor-fold desc="Database Table Connection and Coloumn Details">
    """
    object representation of the user .
    user is a model stored in database as an object .
    inherit from Sql_alchemy model .
    """
    #  crete the table to store user model.
    __tabalename_ = 'users'
    # unique not null uuid .
    uuid = db.Column(db.String(30), primary_key=True)
    # school id
    school_id = db.Column(db.String(30))
    # user in game money
    us_dollar = db.Column(db.BigInteger)
    # </editor-fold>

    # <editor-fold desc="Constructor">
    # constructor
    def __init__(self, user_unique_identifier, school_id, us_dollar=0):
        """
        :param user_unique_identifier: uuid given by the server .
        :param school_id: School id given by the user .
        :param us_dollar: Earn points .
        """
        self.school_id = school_id
        self.uuid = user_unique_identifier
        self.us_dollar = us_dollar

    # </editor-fold>

    # <editor-fold desc="Class Methods">
    # region for classMethod

    # Find All User With school id
    @classmethod
    def find_all_users(cls, school_id):
        """
        Find all user with the same school id .
        It gives you a list of user those who ae registered with same school id .
        :param school_id: provide school id .
        :return: None if user not found or UserModel instance with all data .
        """
        # Select from the table users where  email_id = email_id limit 1 .
        # return a UserModel Object .
        return cls.query.order_by(User.username).all()

    # Find a single user with a user_unique_identifier
    @classmethod
    def find_user(cls, user_unique_identifier):
        """
         # Find a single user with a user_unique_identifier
        :param user_unique_identifier: user identification.
        :return: None if user not found or UserModel instance with all data .
        """
        # Select from the table users where  email_id = email_id limit 1 .
        # return a UserModel Object .
        return cls.query.filter_by(uuid=user_unique_identifier).first( )

    # Find leader board
    @classmethod
    def user_leader_board(cls):
        """
        :return: all users according to money .
        """
        # store all user .
        all_user = cls.query.order_by(desc(cls.us_dollar)).all()
        # return the all user json format .
        return {'Leader Board': "User Leader Board", 'Users': [x.json() for x in all_user],
                "Success_Code": 1}, 200

    # find school leader board.
    @classmethod
    def school_leader_board(cls):
        """
        :return: school leader board .
        """
        # select all schools .
        all_user = cls.query.order_by(cls.school_id).all()
        # iterate over schools id .
        school_id_list = []
        for user in all_user:
            if user.school_id in school_id_list:
                continue
            else:
                school_id_list.append(user.school_id)
        # now I have all school id .
        # select all user of that school .
        school_obtained_coin_list = []
        for school in school_id_list:
            same_school_user = cls.query.filter_by(school_id=school).all()
            total_coin = 0
            for user in same_school_user:
                total_coin += total_coin + user.us_dollar
            school_obtained_coin_list.append(total_coin)
        #all details dict.
        resultDict = { }
        # iterate to createa dictionary .
        for num,item in enumerate(school_id_list, start=0):
            resultDict[item] = school_obtained_coin_list[int(num)]
        #Sort the dictionary.
        sorted_list = sorted(resultDict.items( ), key=lambda kv: kv[1])
        # make it json serialize
        return {'Leader Board':'School Leader Board','School':[{"School_id":k,"Total_Coin":str(v)} for (k,v) in sorted_list ]}
    # </editor-fold>

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
        return {'User_uuid': self.uuid, 'School_id': self.school_id, 'Earned_points': self.us_dollar}
    # </editor-fold>
