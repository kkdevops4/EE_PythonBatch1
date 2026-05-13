# Bengal Election 2026

parties = ("NOTA", "BJP", "TMC", "INC", "CPI")
voters = ("a", "b", "c", "d", "e", "f", "g", "h",
          "i", "j", "k", "n", "q", "s", "t", "w")

votes = {party: [] for party in parties}

total = int(input("Enter number of voters = "))

for i in range(total):
    name = input("Enter your name = ")
    if name in voters:
        print("Valid voter")

        n = int(input("""
Choose your vote for party:
  Press 0 for NOTA
  Press 1 for BJP
  Press 2 for TMC
  Press 3 for INC
  Press 4 for CPI
= """))

        if 0 <= n < len(parties):
            print("You voted for =", parties[n])
            votes[parties[n]].append(name)
        else:
            print("Invalid choice")
    else:
        print("Invalid Voter")

print("\nFinal Result :")

for party in votes:
    print(party, ":", len(votes[party]))

max_votes = max(len(votes[p]) for p in votes)

winners = [p for p in votes if len(votes[p]) == max_votes]

if len(winners) == 1:
    print("\nWinner is :", winners[0])
else:
    print("\nIt's a tie between :", winners)
