things = ["MOZZARELLA", "Cinderella"]
print(things[0])
print(things[1])

#Capitalizing did indeed change things
#Deleting the element then proceeding to try and print it resulted in an error, which is expected

def good():
    goodguys = ["Harry", "Ron", "Hermoine"]
    return goodguys

#Am I the only person I know that didn't particularly like Harry Potter?

def get_odds():
    count = 0
    for x in range(10):
        if x % 2 != 0:
            count += 1
            if count == 3:
                print(x)
                return

# Call the function
get_odds()
