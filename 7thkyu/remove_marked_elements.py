class List:
    def remove_(self, integer_list, values_list):
        # set up results variable
        res = []
        #iterate over list
        for num in integer_list:
            #only add to results if the number is not in the values list.
            if num not in values_list:
                res.append(num)
                
        return res