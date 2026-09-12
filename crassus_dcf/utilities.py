from enum import Enum
from dataclasses import dataclass

class ValueFormat(Enum):
    SCALED_INTEGER = 0 # float representation of integer scaled in billions, millions, or thousands
    RATIO = 1 # float value
    INTEGER = 2 # unscaled integer value
    PERCENTAGE = 3 # float value with '%' suffix
    OTHER = 4 # other datatypes (e.g. strings) which will not be formatted

@dataclass
class FinancialRepKeyFormatting:
    value_format: ValueFormat = ValueFormat.SCALED_INTEGER
    indent: int = 0
    # TODO: add bool params default_to_NaN, replace_NaN_with_zero, omitted_key, required_key

FINANCIAL_REPS_MASTER_STRUCTURE = {
    "Year": FinancialRepKeyFormatting(value_format=ValueFormat.OTHER),
    "Revenue": FinancialRepKeyFormatting(),
        "Revenue growth": FinancialRepKeyFormatting(value_format=ValueFormat.PERCENTAGE, indent=1),
    # TODO: add the rest
}