from tinydb import TinyDB


class DataBase(TinyDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

