def is_conflict_serializable(schedule):
    operations = schedule.split(',')
    transactions = set()
    conflicts = []

   
    for i, op in enumerate(operations):
        t1 = op[1]  
        transactions.add(t1)
        if op[0] == 'w': 
            for j in range(i + 1, len(operations)):
                t2 = operations[j][1]
                if t1 != t2 and (operations[j][0] == 'r' or operations[j][0] == 'w') and operations[j][2] == op[2]:
                    conflicts.append((t1, t2))
        elif op[0] == 'r':  
            for j in range(i + 1, len(operations)):
                t2 = operations[j][1]
                if t1 != t2 and operations[j][0] == 'w' and operations[j][2] == op[2]:
                    conflicts.append((t1, t2))

    
    graph = {t: [] for t in transactions}
    for t1, t2 in conflicts:
        graph[t1].append(t2)

    def has_cycle(v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True

        for neighbor in graph[v]:
            if not visited[neighbor]:
                if has_cycle(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[v] = False
        return False

    visited = {t: False for t in transactions}
    rec_stack = {t: False for t in transactions}

    for node in transactions:
        if not visited[node]:
            if has_cycle(node, visited, rec_stack):
                return True

    return False



schedule = input().strip()

transactions = set(op[1] for op in schedule.split(','))
num_transactions = len(transactions)

serializable = 1 if not is_conflict_serializable(schedule) else 0

print(num_transactions)
print(serializable)

