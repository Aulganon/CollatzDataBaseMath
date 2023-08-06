
class CommonDataType():
    
    def __init__(self) -> None:
        self.list_of_args = []
        self.count_position = 0
        self.large_bool_flag = False
    

class ExtraDataType(CommonDataType):
    
    def __init__(self) -> None:
        super().__init__()
        # commited
