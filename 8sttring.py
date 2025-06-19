text = "Bhagyshri"
pat = "shri"
n = len(text)
m = len(pat)
flag = 0

for i in range(n): 
    if text[i:m+i] == pat:  
        flag = 1
        index = i 

if flag == 1:
    print(f"The '{pat}' is found in '{text}' at starting index --> {index}")
else:
    print(f"The '{pat}' is not found in '{text}'")
