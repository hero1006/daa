#smallest weight
def knapsack(wt, profit, cap):
    items = [(i, wt[i], profit[i], wt[i]/profit[i]) for i in range(len(wt))]
    items.sort(key = lambda x:x[1])

    total_profit = 0
    include_items = []

    for i, wt, profit, ratio in items:
        if cap >= wt:
            include_items.append((i, 1))
            total_profit = total_profit + profit
            cap = cap - wt
        
        else:
            frac = cap / wt
            total_profit = total_profit + (frac*profit)
            include_items.append((i, frac))

    return total_profit, include_items

wt = [30, 20, 10]
profit = [60, 50, 40]
cap = 50

total_profit, include_items = knapsack(wt, profit, cap)
print("\n Total profit is:", total_profit)
print("include items are:",include_items)

#larget ratio
def knapsack(wt, profit, cap):
    items = [(i, wt[i], profit[i], wt[i]/profit[i]) for i in range(len(wt))]
    items.sort(key = lambda x:x[3], reverse=True)

    total_profit = 0
    include_items = []

    for i, wt, profit, ratio in items:
        if cap >= wt:
            include_items.append((i, 1))
            total_profit = total_profit + profit
            cap = cap - wt
        
        else:
            frac = cap / wt
            total_profit = total_profit + (frac*profit)
            include_items.append((i, frac))

    return total_profit, include_items

wt = [30, 20, 10]
profit = [60, 50, 40]
cap = 50

total_profit, include_items = knapsack(wt, profit, cap)
print("\n Total profit is:", total_profit)
print("include items are:",include_items)

#largest profit
def knapsack(wt, profit, cap):
    items = [(i, wt[i], profit[i], wt[i]/profit[i]) for i in range(len(wt))]
    items.sort(key = lambda x:x[2], reverse=True)

    total_profit = 0
    include_items = []

    for i, wt, profit, ratio in items:
        if cap >= wt:
            include_items.append((i, 1))
            total_profit = total_profit + profit
            cap = cap - wt
        
        else:
            frac = cap / wt
            total_profit = total_profit + (frac*profit)
            include_items.append((i, frac))

    return total_profit, include_items

wt = [30, 20, 10]
profit = [60, 50, 40]
cap = 50

total_profit, include_items = knapsack(wt, profit, cap)
print("\n Total profit is:", total_profit)
print("include items are:",include_items)
