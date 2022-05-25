    def ascii_prime(self):
        primeAscii = []
        for char in self.s:
            if not SString.primChecker(ord(char)):
                primeAscii.append(char)
        str_ing = "" 
        for i in primeAscii:
                str_ing += i
        return i
        

    def __add__(self, __other_obj):
        return SString( __other_obj.s + self.s)

    def __imul__(self, __other_obj):
        cartesian_product = [i + j for i in self.s for j in __other_obj.s]
        str_ing = "" 
        for i in cartesian_product:
                str_ing += i
        return i        

    def __eq__(self, __o):
        return len(self.s) == len(__o.s)

    def __ne__(self, __o):
        return len(self.s) != len(__o.s)