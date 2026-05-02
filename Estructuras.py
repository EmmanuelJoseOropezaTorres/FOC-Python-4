"""Condicionales y bucles basicos sin magia."""

x = 3 
if x > 0:
        print("Positivo")
elif x == 0:
        print("Cero")
else:
        print("Negativo")   

        """Estructura for"""

        for i in range(3):
                print(f"i={i}") 


        """Estructura while"""                                   
        n = 3
        while n > 0:
                print(n)
                n -= 1
                """"Estructura de control de excepciones"""