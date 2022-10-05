def my_roman_numerals_converter(nbr):
        son = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        rim = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
      
        jovob = ''
        i = 0
        
        while nbr > 0:
            for _ in range(nbr // son[i]):
              
                jovob += rim[i]
                nbr -= son[i]
            i += 1
            
        return jovob
