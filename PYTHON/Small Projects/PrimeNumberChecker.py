#Write your code below this line 👇

def prime_checker(number):
    if number==0:
        print("This is not a prime!0")
    else:
        for i in range(2,number):
            is_prime= True

            if number%i==0:
                is_prime=False
    
    
        if is_prime==True:
            print("This is a Prime!")
        else:
            print("This is NOT a Prime!")    




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



