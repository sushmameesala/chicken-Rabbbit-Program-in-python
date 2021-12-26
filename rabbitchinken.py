#Write a python program to solve a classic ancient Chinese puzzle.
#We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
#Sample Input
#Expected Output
#heads-150 legs-400
#100 50
#heads-3 legs-11
#No solution
#heads-3 legs-12
#0 3
#heads-5 legs-10
#5 0

def surya(heads,legs):
    rabbit_count=0
    chicken_count=0
    error_msg="tappu rareyyy.."

    if(heads>=legs):
        print(error_msg)
    elif(legs%2!=0):
        print(error_msg)
    else:
        rabbit_count = (legs - 2*heads) / 2
        chicken_count = heads - rabbit_count
        print(int(chicken_count),int(rabbit_count))

surya(150,400)

