import random

with open("./hyakunin1.txt", encoding="utf-8") as f:
    wakas = [s.strip() for s in f.readlines()]
    print(wakas[random.randrange(len(waks))])
    
if __name__=='__main__':
    main()
    
