class Card:
    def __init__(self):
        self.__card_name = None
        self.__card_type = None
        self.__card_color = None
        self.__card_status = None
        self.__card_location = None
        self.__card_image = None

    # =============getter method=================#
    def get_card_name(self):
        return self.__card_name

    def get_card_type(self):
        return self.__card_type

    def get_card_color(self):
        return self.__card_color

    def get_card_status(self):
        return self.__card_status

    def get_card_location(self):
        return self.__card_location

    def get_card_image(self):
        return self.__card_image

    # =================setter method================#
    def set_card_name(self, card_name):
        self.__card_name = card_name

    def set_card_type(self, card_type):
        self.__card_type = card_type

    def set_card_color(self, card_color):
        self.__card_color = card_color

    def set_card_status(self, card_status):
        self.__card_status = card_status

    def set_card_location(self, card_location):
        self.__card_location = card_location

    def set_card_image(self, card_image):
        self.__card_image = card_image
