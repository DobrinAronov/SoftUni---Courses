def checking_target_plunger(days: int, daily_plunder: int, target: float) -> str:
    day = 0
    total_plunder = 0
    while day < days:
        day += 1
        total_plunder += daily_plunder

        if day % 3 == 0:
            total_plunder += daily_plunder * 0.5
        if day % 5 == 0:
            total_plunder -= total_plunder * 0.3
    if total_plunder >= target:
        return f"Ahoy! {total_plunder:.2f} plunder gained."

    percentage_left = (total_plunder / target) * 100
    return f"Collected only {percentage_left:.2f}% of the plunder."




days_of_the_plunder  = int(input())
plunder_per_day = int(input())
expected_plunder = float(input())

print(checking_target_plunger(days_of_the_plunder, plunder_per_day, expected_plunder))
