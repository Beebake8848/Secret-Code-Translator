# Secret Code Language

import random
while(True):
    st = input("Enter a Message: ")
    if st.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break
    words = st.split(" ")
    coding = input("1 for coding and 0 for decoding")
    coding = True if (coding=="1") else False
    if(coding):
        nwords = []
        for word in words:
            if(len(word)>=1):
                r1 = random.choice(["ghf","696","jkl","wsq"])
                r2 = random.choice(["cvx","098","dfg","rtg"])
                stnew = r1 + word[1:]+word[0] + r2
                nwords.append(stnew)
            else:
                nwords.append(word[::-1])
        print(" ".join(nwords))


    else:
        nwords = []
        for word in words:
            if(len(word)>=3):
                stnew = word[3:-3]
                stnew = stnew[-1] + stnew[:-1]
                nwords.append(stnew)
            else:
                nwords.append(word[::-1])
        print(" ".join(nwords))


