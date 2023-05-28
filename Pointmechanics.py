def earn_points_enemy(enemy_type):
    if enemy_type == "Infantry":
        points_earned = 10
    elif enemy_type == "Armored Infantry":
        points_earned = 20
    elif enemy_type == "Special Forces":
        points_earned = 50
    elif enemy_type == "Tank":
        points_earned = 250
    elif enemy_type == "Attack Helicopter":
        points_earned = 1500
    else:
        points_earned = 0
    
    player.points += points_earned
    print(f"You earned {points_earned} points by defeating an enemy {enemy_type}!")
    print(f"Your current point balance is: {player.points}")
