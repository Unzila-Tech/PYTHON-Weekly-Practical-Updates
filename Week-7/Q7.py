routing_table = {"A": 0,"B": 1,"C": 1,"D": 5}
print("Initial Routing Table:", routing_table)
updates = [{"E": 1, "D": 2},{"F": 2, "E": 1},{"G": 3}]
for round_no in range(1, 4):
    print(f"\n--- Round {round_no} ---")
    received = updates[round_no-1]
    for dest, hop in received.items():
        new_hop = hop + 1 
        if dest not in routing_table or new_hop < routing_table[dest]:
            routing_table[dest] = new_hop
            print(f"Updated {dest} with hop count {new_hop}")
        else:
            print(f"No update for {dest}")
    print(f"Table after Round {round_no}: {routing_table}")
print("\nFinal Routing Table:")
for dest, hop in routing_table.items():
    print(f"Destination {dest} -> Hop {hop}")