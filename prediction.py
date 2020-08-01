x, y, x2, n, xy = 0, 0, 0, 1, 0

val = eval(input("Enter time interval bw 2 readings(in min) "))
h = eval(input("Enter height of dam "))
print("Starting prediction")
print("Press Enter after entering each water level(in m)")
print("Enter -1 anytime to exit")

while(1):
    level = eval(input())
    if(level == -1):
        break
    n += 1
    time = val*n
    y += level
    x += time
    x2 += time*time
    xy += time*level
    if(n == 2):
        print("Enter Next Reading")
    else:
        d = n*x2 - x*x
        a = (y*x2 - x*xy)/d
        b = (n*xy - x*y)/d
        rem = (h-a)/b - time
        print(rem, "Min till the dam is full")
