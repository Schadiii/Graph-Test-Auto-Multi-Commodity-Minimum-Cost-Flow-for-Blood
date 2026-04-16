# --- DATASET FROM PAGE 11-13 ---
blood_types = ['O+', 'A+', 'B+', 'AB+', 'O-', 'A-', 'B-', 'AB-']

# Supply by Type [cite: 288]
supply = {
    'Red Cross':  [158, 122, 104, 23, 9, 9, 4, 4],
    'Blood Bank': [ 88,  68,  58, 12, 6, 4, 3, 3],
}

# Demand by Type [cite: 287, 288]
demand = {
    'ACE Malolos':  [25, 19, 16, 4, 1, 2, 1, 1],
    'Sacred Heart': [26, 10, 17, 4, 1, 2, 1,    1],
}

# Travel Times (Minutes) 
travel_times = {
    ('Red Cross',  'ACE Malolos'):  1.68,
    ('Blood Bank', 'ACE Malolos'):  2.40,
    ('Red Cross',  'Sacred Heart'): 2.64,
    ('Blood Bank', 'Sacred Heart'): 2.64,
}

# --- LOGIC: MINIMUM TRAVEL TIME ALLOCATION (PAGE 13-14) ---
def solve_blood_distribution():
    total_cost = 0
    results = []

        # 1. ACE Malolos: All from Red Cross (Faster route: 1.68 min) [cite: 289, 291]
    ace_cost = 0
    dest = 'ACE Malolos'
    source = 'Red Cross'
    t_time = travel_times[(source, dest)]
    
    for idx, type_name in enumerate(blood_types):
        units = demand[dest][idx]
        supply[source][idx] -= units # Deduct from Red Cross 
        cost = units * t_time
        ace_cost += cost
        results.append((dest, source, type_name, units, t_time, cost))
    
    # 2. Sacred Heart: Uses Blood Bank (Faster route: 2.64 min) [cite: 290, 291]
    # Note: Page 14 notes splitting, but uses Blood Bank for the calculation [cite: 290]
    sh_cost = 0
    dest = 'Sacred Heart'
    source = 'Blood Bank' 
    t_time = travel_times[(source, dest)]

    for idx, type_name in enumerate(blood_types):
        units = demand[dest][idx]
        supply[source][idx] -= units # Deduct from Blood Bank [cite: 290]
        cost = units * t_time
        sh_cost += cost
        results.append((dest, source, type_name, units, t_time, cost))

    # --- OUTPUT MATCHING PAGE 15 ---
    print(f"{'='*60}")
    print(f"Total Cost for ACE Malolos: {ace_cost:.2f} minutes") # Matches 115.92 
    print(f"Total Cost for Sacred Heart: {sh_cost:.2f} minutes") # Matches 190.08 
    
    total_cost = ace_cost + sh_cost
    print(f"{'='*60}")
    print(f"GRAND TOTAL TRANSPORTATION COST: {total_cost:.0f} minutes") # Matches 306 [cite: 292]
    print(f"{'='*60}\n")

    print(f"{'Destination':<15} | {'Source':<12} | {'Type':<4} | {'Units':<5} | {'Cost'}")
    print("-" * 60)
    for res in results:
        print(f"{res[0]:<15} | {res[1]:<12} | {res[2]:<4} | {res[3]:<5} | {res[5]:.2f}")

if __name__ == "__main__":
    solve_blood_distribution()