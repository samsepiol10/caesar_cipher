import time
from functools import wraps
print("")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("")
print("")
time.sleep(0.1)
print("                            ::::::::  :::    ::: :::::::::  :::   :::     :::           :::::::::  :::::::::: :::     :::")
time.sleep(0.1)
print("                           :+:    :+: :+:    :+: :+:    :+: :+:   :+:   :+: :+:         :+:    :+: :+:        :+:     :+:")
time.sleep(0.1)
print("                           +:+        +:+    +:+ +:+    +:+  +:+ +:+   +:+   +:+        +:+    +:+ +:+        +:+     +:+") 
time.sleep(0.1)
print("                           +#++:++#++ +#+    +:+ +#++:++#:    +#++:   +#++:++#++:       +#+    +:+ +#++:++#   +#+     +:+")  
time.sleep(0.1)
print("                                  +#+ +#+    +#+ +#+    +#+    +#+    +#+     +#+       +#+    +#+ +#+         +#+   +#+")
print("                           #+#    #+# #+#    #+# #+#    #+#    #+#    #+#     #+#       #+#    #+# #+#          #+#+#+#")
time.sleep(0.1)
print("                            ########   ########  ###    ###    ###    ###     ###       #########  ##########     ###")
time.sleep(0.1)
print("")
print("")
print("------------------------------------------------------------------########################------------------------------------------------------------------------")
print("                                                                       CEASEAR CIPHER")
print("------------------------------------------------------------------########################------------------------------------------------------------------------")
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_to_number=dict(zip(alphabet,range(len(alphabet))))
number_to_alpha=dict(zip(range(len(alphabet)),alphabet))
def encryption(p):
    p=p.replace(" ","")
    p=p.upper()
    try:
        numbers=[]
        for i in p:
            temp=alpha_to_number[i]
            value=temp+3
            numbers.append(value)
        cipherlist=[]
        for j in numbers:
            if j > 24 :
                h=j-26
                cipherlist.append(number_to_alpha[h])
            else:
                cipherlist.append(number_to_alpha[j])
        ciphertext=""
        for k in cipherlist:
            ciphertext+=k
        return ciphertext
    except:
        print()
        print("                                                               the text you entered has some integer !!")
        print("                                                               the text should only contain string !!")
        print("                                                               This is how dumbest encryption(ceasear cipher) work :)")
        exit()
def decryption(c):
    c=c.replace(" ","")
    c=c.upper()
    plainlist=[]
    for i in c:
        try:
            temp=alpha_to_number[i]
            if temp < 3:
                a=temp+23
                plainlist.append(number_to_alpha[a])
            else:
                b=temp-3
                plainlist.append(number_to_alpha[b])
        except:
            print()
            print("                                                               the text you entered has some integer !!")
            print("                                                               the text should only contain string !!")
            print("                                                               This is how dumbest encryption(ceasear cipher) work :)")
            exit()
    plaintext=""
    for k in plainlist:
        plaintext+=k
    return plaintext
print()
print()
try:
    response=int(input("                                                        For Encryption press 1 | for Decryption press 2 :"))
    if response==1:
        p=input("                                                                     Enter the PlainText: ")
        print("                                                                       ceasear cipher : ",encryption(p))
    elif response==2:
        c=input("                                                                         Ente the CipherText: ")
        print("                                                                         plain text : ",decryption(c))
    else:
        print("                                                                             wrong keyword provided !!")
except:
    print()
    print("                                                               Invalid input provided !!")