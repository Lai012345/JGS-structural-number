import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from structural_number import FocusedValue, structural_sum, focus_count

coins = [
    FocusedValue(0, True),   # 显现的0
    FocusedValue(0, False),  # 未显现的0
    FocusedValue(1, True),   # 显现的1
    FocusedValue(1, False)   # 未显现的1
]

classical_sum = sum(c.value for c in coins)
struct_sum = structural_sum(coins)
focused = focus_count(coins)

print("---- Raw data (value, focused) ----")
for idx, c in enumerate(coins, 1):
    print(f"coin{idx}: ({c.value}, {c.is_focused})")

print("\n---- Result comparison ----")
print(f"Classical   sum(value)             = {classical_sum}")
print(f"Structural  sum(structural_amount) = {struct_sum}")
print(f"Focus count  (how many in focus)   = {focused}")
