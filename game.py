"""
Game class - dataclass for lottery game info
"""

from dataclasses import dataclass, field

import lottery_data_api as api
from drawing import Drawing
from number_analysis import NumberAnalysis


@dataclass
class Game:
    """
    Class definition for lottery game information
    """
    name: str
    start_date: str
    field_num_max: int
    bonus_ball_max: int
    days_drawn: list[str]
    last_draw_date: str = field(init=False)
    drawing_history: list[Drawing] = field(init=False, default_factory=list)
    field_num_analysis: list[NumberAnalysis] = field(init=False,
                                                     default_factory=list)
    field_nums_overdue: list[list] = field(init=False, default_factory=list)

    async def init(self):
        await self.get_history()
        self.find_last_draw_date()
        self.analyze_field_nums()

    async def get_history(self):
        """Get game history from data api and set drawing_history field"""
        results = await api.get_lottery_data(self.name, self.start_date)
        self.drawing_history = Drawing.to_drawings_list(results)

    def find_last_draw_date(self):
        """Find last draw date in drawing history list and set last_draw_date field"""
        self.last_draw_date = self.start_date
        for drawing in self.drawing_history:
            if drawing.draw_date > self.last_draw_date:
                self.last_draw_date = drawing.draw_date

    def analyze_field_nums(self):
        """Analize each ball numer and append to analysis field"""
        for ball_num in range(1, self.field_num_max + 1):
            self.field_num_analysis.append(
                (NumberAnalysis(f'{ball_num:0>2}', self.drawing_history)))

    def get_field_nums_overdue(self) -> list[list]:
        """Set field numbers overdue field"""
        field_nums_overdue = [[],[]]
        sorted_analysis = sorted(self.field_num_analysis, key=lambda number: number.draws_overdue, reverse=True)
        
        for field_num in sorted_analysis:
            if field_num.draws_overdue > 0:
                field_nums_overdue[0].append(field_num.number)
                field_nums_overdue[1].append(field_num.draws_overdue)
        return field_nums_overdue
        # self.field_nums_overdue.sort(key=lambda num: num[1], reverse=True)
