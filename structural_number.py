from dataclasses import dataclass
from typing import Generic, TypeVar, Iterable

T = TypeVar('T')

@dataclass
class FocusedValue(Generic[T]):
    """A minimal structural-number unit (value + focus)."""
    value: T
    is_focused: bool

    def structural_amount(self):
        """Return `value` only if in focus, else 0/None-equivalent."""
        return self.value if self.is_focused else 0

def structural_sum(items: Iterable['FocusedValue[int]']) -> int:
    """Sum of structural amounts (counts only focused items)."""
    return sum(i.structural_amount() for i in items)

def focus_count(items: Iterable['FocusedValue']) -> int:
    """Count how many items are in focus."""
    return sum(1 for i in items if i.is_focused)
