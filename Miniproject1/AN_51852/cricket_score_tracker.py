print("CRICKET SCORE TRACKER")

overs = int(input("Enter number of overs: "))  

# Team 1
print(f"{'-'*50}")
print(f"Team 1 ({overs} overs):")
team1 = 0
for i in range(overs):
    team1 += int(input(f"Enter runs for Over {i+1}: "))
    print(int(input(f"Enter wickets for Over {i+1}: ")))

# Team 2  
print(f"{'-'*50}")
print(f"Team 2 ({overs} overs):")
team2 = 0
for i in range(overs):
    team2 += int(input(f"Enter runs for Over {i+1}: "))
    print(int(input(f"Enter wickets for Over {i+1}: ")))

# Winner
print(f"{'-'*20}")
print(f"{'='*20}")
print(f"Team 1: {team1} runs")
print(f"Team 2: {team2} runs")
print(f"{'='*20}")

if team1 > team2:
    print("TEAM 1 WINS!")
elif team2 > team1:
    print("TEAM 2 WINS!")
else:
    print("DRAW!")