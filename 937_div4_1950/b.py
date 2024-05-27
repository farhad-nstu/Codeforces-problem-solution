t = int(input())
while t > 0:
    t -= 1

    hash_print = False
    n = int(input())
    for i in range(n*2):
        for j in range(n*2):
            if hash_print:
                print("..")
                hash_print = False
            else:
                print("##")
                hash_print = True 
