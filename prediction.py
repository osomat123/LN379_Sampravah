x, y, x2, n, xy = 0, 0, 0, 0, 0

# Taking height of dam and time interval bm values from user
val = eval(input("Enter time interval bw 2 readings(in min) "))
h = eval(input("Enter height of dam "))

print("Starting prediction")
print("Press Enter after entering each water level(in m)")
print("Enter -1 anytime to exit")

while(1):

    level = eval(input())
    if(level == -1):
        break

    # Manipulating variables used for calculation of reression
    n += 1
    time = val*n
    y += level
    x += time
    x2 += time*time
    xy += time*level

    # Regression cant work on one input we need atleast two
    if(n == 1):
        print("Enter Next Reading")

    #
    else:

        d = n*x2 - x*x
        a = (y*x2 - x*xy)/d
        b = (n*xy - x*y)/d

        # rem is the time after which water level will reach 100% FRL
        rem = int((h-a)/b - time)
        print(rem, "Min till the dam is full")
