hat_list = [1,2,3,4,5]
timothy_input = int(input("Please Enter"))
hat_list[len(hat_list)//2]= timothy_input
print(hat_list)
hat_list.pop(-1)
print(len(hat_list))