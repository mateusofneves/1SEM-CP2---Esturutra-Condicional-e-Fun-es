n1 = float(input("Digite algum numero "))

n2 = float(input("Digite algum numero "))

n3 = float(input("Digite algum numero "))

if(n1 > n2 and n1 > n3):
    A = n1
    if(n2 > n3):
        B = n2
        C = n3
        print(f"O lado A: {n1}. O lado B:{n2}. O lado C: {n3} \n")



    elif(n3 > n2):
        B = n3
        C = n2
        print(f"O lado A: {n1}. O lado B:{n3}. O lado C: {n2} \n")

    elif(n3 == n2):
        B = n3
        C = n2
        print(f"O lado A: {n1}. O lado B:{n3}. O lado C: {n2} \n")




elif(n2 > n1 and n2 > n3):
    A = n2
    if (n1 > n3):
        B = n1
        C = n3

        print(f"O lado A: {n2}. O lado B:{n1}. O lado C: {n3} \n")

    elif (n3 > n1):
        B = n3
        C = n1

        print(f"O lado A: {n2}. O lado B:{n3}. O lado C: {n1} \n")

elif(n3 > n1 and n3 > n2):
    A = n3
    if (n1 > n2):
        B = n1
        C = n2

        print(f"O lado A: {n3}. O lado B:{n1}. O lado C: {n2} \n")

    elif (n2 > n1):
        B = n2
        C = n1

        print(f"O lado A: {n3}. O lado B:{n2}. O lado C: {n1} \n")