
class Assertions:
    @staticmethod
    def is_not_null(obj):
        if obj is None:
            raise Exception('Null value in object')
        return obj