from dataclasses import dataclass


@dataclass
class Expense:
    item: str
    cost: float
    tax: float
    split_between: str

    def __post_init__(self):
        self.total_cost = self.cost + self.tax
