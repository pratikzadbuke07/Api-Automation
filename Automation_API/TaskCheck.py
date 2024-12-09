
class Status:
    SUCCESS=True
    FAILED=False

class TaskStatus:
    def __init__(self,status,erro_discript=''):
        self.status=status
        self.erro_discript=erro_discript

    @classmethod
    def error(cls,erro_discript):
        return cls(Status.FAILED,erro_discript)

    @classmethod
    def success(cls):
        return cls(Status.SUCCESS)

    def is_success(self):
        return self.status==Status.SUCCESS