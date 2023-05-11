class List:
    def remove_(self, integer_list, values_list):
        res = []
        for num in integer_list:
            if num not in values_list:
                res.append(num)
                
        return res