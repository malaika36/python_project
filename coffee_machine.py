def exchange(rupees,Sum):
    if(Sum<rupees):
        print("your ammount are not sudiicient")
    elif(Sum>rupees):
        Sum = Sum - rupees
        print(f"your exchange is {Sum}")
        print("heres your coofee")
    else:
        print("no exchange")
def left_ingrediets(t_ingredients,co):
    t_ingredients["milk"] = t_ingredients["milk"]-co["milk"]
    t_ingredients["coffee_beans"] = t_ingredients["coffee_beans"]-co["coffee_beans"]
    t_ingredients["water"] = t_ingredients["water"]-co["water"]
    t_ingredients["sugar"] = t_ingredients["sugar"]-co["sugar"]
def sufficient(total,c):
    for i in total:
        if(total[i]<c[i]):
            print(f"{i} is not enough")
            break

t = True
while t==True: 
    cappucino = {"milk":50,"coffee_beans":20,"water":20,"sugar":5}
    latte = {"milk":40,"coffee_beans":15,"water":18,"sugar":3}
    expresso = {"milk":35,"coffee_beans":12,"water":16,"sugar":2}
    t_ingredients = {"milk":2000,"coffee_beans":150,"water":1000,"sugar":45}
    coffee_type = input("enter the coffee which you want to drink(l for latte/e for expreesso/c for cappucino: ) ")
    fifty = int(input("how many rs 50 you want to enter : "))
    hundred = int(input("how many rs 100 you want to enter : "))
    t_fifty = fifty * 50
    t_hundred = hundred * 100
    add = t_fifty + t_hundred
    c_rupees,l_rupees,e_rupees = 250,200,150
    if(coffee_type=="c"):
       exchange(c_rupees,add)
       left_ingrediets(t_ingredients,cappucino)
       sufficient(t_ingredients,cappucino)
       
    elif(coffee_type=="l"):
       exchange(l_rupees,add)
       left_ingrediets(t_ingredients,latte)
       sufficient(t_ingredients,latte)
    elif(coffee_type=="e"):
       exchange(e_rupees,add)
       left_ingrediets(t_ingredients,expresso)
       sufficient(t_ingredients,expresso)
    elif(coffee_type=="report"):
        print(t_ingredients)
    elif(coffee_type=="off"):
        t=False

    else:
        print("you enter incorrect")
       

