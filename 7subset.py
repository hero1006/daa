def find_subsets(S, M):
    result = []
    def backtrack(start, subset, current_sum):
        if current_sum == M:
            result.append(subset[:])
            return
        
        if current_sum > M:
            return
        
        for i in range(start,len(S)):
            subset.append(S[i])
            backtrack(i+1, subset, current_sum + S[i])
            subset.pop()

    backtrack(0,[],0)
    return result

S = [1, 3, 4, 5]
M = 8

solutions = find_subsets(S,M)
if solutions:
    print(f"subsets of {S} whose sum is = {M} are:")
    for subset in solutions:
        print(subset)

else:
    print(f" No subsets of {S} whose sum is = {M}")



    