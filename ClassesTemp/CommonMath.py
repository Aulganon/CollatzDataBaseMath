
from Resources.DataTypes.DataTypes import CommonDataType as CDT




class Collatz_Calc():
    def make_array(self, number: int) -> CDT : 
        CDTv = CDT()
        temp_list = []
        temp_count = 0
        while(number != 1):
            temp_count+=1
            temp_list.append(int(number))
            number = self.__next_number(number)
        CDTv.count_position = temp_count
        CDTv.list_of_args = temp_list
        return CDTv
            
    def __next_number(self, number: int) -> int:
        if (number % 2 == 0):
            number = number / 2
        else:
            number = (number * 3) + 1
        return number
    
   
   
"""def __test_module():
    CDN_k = Collatz_Calc()
    Collatz = CDN_k.make_array(27)
    matplot = range(1,Collatz.count_position+1, 1)
    plt.plot(matplot, Collatz.list_of_args, color = 'aqua', linestyle= 'solid')
    plt.scatter(matplot, Collatz.list_of_args, color = 'red', marker= '*', s= 2.5)
    plt.show()"""
       
if __name__ == "__main__":
    #__test_module() 
    # For debugging purpose only
    pass
