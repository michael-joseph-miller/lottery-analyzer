"""Class defining lottery drawing data and methods"""
from dataclasses import InitVar, dataclass, field


@dataclass
class Drawing():
    """Drawing class definition"""
    draw_date: str
    field_num_str: InitVar[str]
    field_nums: list[str] = field(init=False, default_factory=list)
    multiplier: str = ''
    bonus_ball: str = ''

    def __post_init__(self, field_num_str: str):
        field_nums = field_num_str.split(' ')
        if len(field_nums) == 6:
            self.field_nums = field_nums[:5]
            self.bonus_ball = field_nums[5]
        else:
            self.field_nums = field_nums

    @staticmethod
    def to_drawings_list(data) -> list:
        """Static method to convert data from NY Lottery database to list of Drawing objects"""
        drawings = []
        for drawing in data:
            if 'mega_ball' in drawing:
                temp_drawing = Drawing(drawing['draw_date'],
                                       drawing['winning_numbers'],
                                       drawing['mega_ball'],
                                       drawing['multiplier'])
            elif 'multiplier' in drawing:
                temp_drawing = Drawing(drawing['draw_date'],
                                       drawing['winning_numbers'],
                                       drawing['multiplier'])
            else:
                temp_drawing = Drawing(drawing['draw_date'],
                                       drawing['winning_numbers'])
            drawings.append(temp_drawing)
        return drawings
