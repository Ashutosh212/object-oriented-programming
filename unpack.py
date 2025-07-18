def fn(a, *args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)

# fn(100, 50 ,70)
# fn(galleons = 100, sickles = 50, knuts = 25)

fn(100, 50 ,70, galleons = 100, sickles = 50, knuts = 25)

'''
def total(galleons, sickles, knuts):
    return (galleons*5 + sickles) * 2 + knuts
# 1. Simply passing
# print(total(100,50,25), "Knuts")

# 2. using list to send value
# coins = [100, 50, 25]
# print(total(*coins), "Knuts")  #UNPACKING

# 3. using dict to pass value
# coins = {"galleons": 100, "sickles":50, "knuts":25}
# print(total(**coins), "Knuts")  #UNPACKING
'''

'''

a, b, *rest = [1, 2, 3, 4]  # rest will be list
a, b, *rest = (1, 2, 3, 4)  # rest will be list
a, b, *rest = "hello"
a, *rest = {1, 2, 3}
a, *keys = {'a': 1, 'b': 2}
a, *nums = range(5)


print(a, b, rest)
print(keys)
print(nums)

'''