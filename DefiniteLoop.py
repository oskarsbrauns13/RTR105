for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')
for i in [5,4,3,2,1]:
    print(i)
print('Blastoff!')

for i in[5,4,3,2,1]:
	print(i)
print('Before')
for thing in [9,41,12,3,74,15]:
        print(thing)
print('After')

largest_so_far=-1
print('Before',largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num>largest_so_far:
        largest_so_far=the_num
    print(largest_so_far,the_num)
    
print('After',largest_so_far)

zork=0
print('Before',zork)
for thing in [9,41,12,3,74,15]:
    zork=zork+1
    print(zork,thing)
print('After',zork)    
    
