#Number 1
my_list = ['a', 'b', 'c', 'e', 'f', 'g', 'h' ]

for i in range(len(my_list) // 2):
    my_list[i], my_list[-i-1] = my_list[-i-1],my_list[i] 
print(my_list) 
    


 






#number2
n=int(input("input a number : "))
i=0
while(i<=n):
      if i%2==0:
         print(i)
      i=i+1
       