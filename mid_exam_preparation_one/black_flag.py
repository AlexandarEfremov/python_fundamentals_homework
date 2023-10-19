plundering_days = int(input())
daily_loot = int(input())
expected_plunder = int(input())

accumulated_loot = 0
for day in range(1, plundering_days + 1):
    accumulated_loot += daily_loot
    if day % 3 == 0:
        extra_loot = daily_loot * 0.5
        accumulated_loot += extra_loot
    if day % 5 == 0:
        lost_loot = accumulated_loot * 0.3
        accumulated_loot -= lost_loot

if accumulated_loot >= expected_plunder:
    print(f"Ahoy! {accumulated_loot:.2f} plunder gained.")
else:
    print(f"Collected only {(accumulated_loot / expected_plunder) * 100:.2f}% of the plunder.")

