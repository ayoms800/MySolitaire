class Player:
    def __init__(self):
        self.__id = None
        self.__username = None
        self.__email = None
        self.__password = None
        self.__score = None

    # =============getter method=================#
    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_score(self):
        return self.__score

    # =================setter method================#
    def set_if(self, id):
        self.__id = id

    def set_user_name(self, username):
        self.__username = username

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    def set_score(self, score):
        self.__score = score
