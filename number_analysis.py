"""
Analysis class definition
"""

from dataclasses import InitVar, dataclass, field

from drawing import Drawing


@dataclass
class NumberAnalysis:
    """NumberAnalysis class"""
    number: str
    drawing_history: InitVar[list[Drawing]]
    last_hit_date: str = field(init=False, default='')
    hit_freq: int = field(init=False, default=0)
    total_hits: int = field(init=False, default=0)
    no_hit_count: int = field(init=False, default=0)
    draws_overdue: int = field(init=False, default=0)

    def __post_init__(self, drawing_history: list[Drawing]):
        self.analyze_number(drawing_history)

    def analyze_number(self, drawing_history: list[Drawing]):
        """Calculate total number of hits for a ball number in the provided history."""
        total_hits, no_hit_count, last_hit_date = 0, 0, ''
        for drawing in drawing_history:
            if self.number in drawing.field_nums:
                total_hits += 1
                no_hit_count = 0
                last_hit_date = drawing.draw_date
            else:
                no_hit_count += 1

        self.total_hits = total_hits
        self.no_hit_count = no_hit_count
        self.last_hit_date = last_hit_date

        if self.total_hits != 0:
            self.hit_freq = round(len(drawing_history) / self.total_hits)
        else:
            self.hit_freq = 0

        overdue = self.no_hit_count - self.hit_freq
        self.draws_overdue = overdue if overdue >= 0 else 0
