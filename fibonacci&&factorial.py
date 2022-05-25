#fibonacci series




#factorial
# num=int(input('enter a number'))
# fact=1
# for i in range(num,0,-1):
#     fact=fact*i
# print(fact)

# #nested loop
#multiplication from 1-10
# for i in range(1,11):
#     for j in range(1,11):
#         # print(i,'x',j,'=',i*j)
#         print(f'{i}x{j}={i*j}',end='')
#     print()


# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()

# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(j,end='')
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()


# for i in range(1,7):
#     for j in range(1,7):
#         if (i+j)%2==0:
#             print('*',end='')
#         else:
#             print('#',end='')
#     print()

#print factors of a given number
#20:1,2,4,5,10,20

# num=int(input('enter a number')
# num=20
# if num%
#print multiples of a user given number upto user given boundary
#num=3 bound=20 output:3,6,9,12,15,18
num=3
bound=20
for i in range(1,bound+1):
    if  num*i<=20:
        print(num*i)
    else:
        break



i=1
while num*i<bound:
    print(num*i)
    i+=1

