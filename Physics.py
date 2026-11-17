print("COS 101 Assignment")
print("Physics Formula")
print("1. Period")
print("2. Speed")
print("3. Force")
print("4.  Resistance")
print("5. Momentum")	
def Period():
    f = float(input("Enter Frequency: "))
    #let period be represented by the symbol T
    T = 1/f
    print("Period =", T , "sec")
def Speed():
    d= float(input("Enter Distance: "))
    t= float(input("Enter Time taken: "))
    S= d / t
    print("Speed =", S, "m/s")
def Force():
    m = float(input("Enter mass: "))
    a = float(input("Enter acceleration: "))
    F = m * a
    print("Force =", F, "N")
def Resistance():
    I = float(input("Enter current: "))
    V = float(input("Enter Potential difference: "))
    R= V/I
    print("Resistance =", R, "ohm(s)")
def Momentum():
    m = float(input("Enter mass: "))
    v= float(input("Enter velocity: "))
    p = m * v
    print("momentum =", p, "kg/ms")
while True:
	choice = int(input("Choose a formula (1-5): "))
	if choice ==1:
  	 Period( )
	elif choice ==2:
		Speed( )
	elif choice==3:
		Force( )
	elif choice ==4:
		Resistance( )
	elif choice ==5:
		Momentum( )
	else:
		 print("invalid option")
	answer= input("would you like to perform another calculation?(Yes/No:")
	if answer.lower() !="Yes":
		print("End of Physics Formula Calculator")
	break
