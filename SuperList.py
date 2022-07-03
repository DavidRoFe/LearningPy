class SuperList(list):

    def __len__(self):
        
        return 1000
    
super_list_00 = SuperList()
super_list_00.append(5)
print(super_list_00)
print(len(super_list_00))