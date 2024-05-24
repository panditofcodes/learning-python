import random, time

letters = ['a','e','i','o','l']



while 1>0:
    random.shuffle(letters)
    
    print("".join(letters))

    time.sleep(1)