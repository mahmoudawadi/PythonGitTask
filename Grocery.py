groceries = {'apple':2,
             'banana':1,
             'milk':3,
             'bread':2} 

cart = []
while True:
    user_input = input('What do want to duy ? = ').lower().split()
    if user_input=='done':
        break
    parts = user_input.split()
    if user_input  in groceries:
        cart.append(user_input)
    else:
        print('Sorry we do not have that item')
total = 0
for item in cart:
    total += groceries[item]
print('\nYou bought:', cart)
print('Total = $',total)

if total > 10 :
    print('You spent a lot!')
else:
    print('You spent a little!')
