from pywebio import start_server
from pywebio.input import *
from pywebio.output import *

def solve_r(Equation) :
    r = Equation.replace(" ","").lower()
    try :
        if 'x^3' in r :
        
            if not '=' in r :
                r += '=0'
            a = list(r.split("x^3"))[0]
            b = r.replace(str(a)+"x^3"+"+","").replace(str(a)+"x^3","").split("x^2")[0]
            c = r.replace(str(a)+"x^3"+str("+"+str(b) if float(b) > 0 else str(b))+"x^2"+"+","").replace(str(a)+"x^3"+str("+"+str(b) if float(b) > 0 else str(b))+"x^2","").split("x")[0].replace("+","")
            d = r.replace(str(a)+"x^3"+str("+"+str(b) if float(b) > 0 else str(b))+"x^2"+str("+"+str(c) if float(c) > 0 else str(c))+"x"+"+","").replace(str(a)+"x^3"+str("+"+str(b) if float(b) > 0 else str(b))+"x^2"+str("+"+str(c) if float(c) > 0 else str(c))+"x","").split("=")[0].replace("+","")
            e = r.split("=")[1]
            a = float(a)
            b = float(b)
            c = float(c)
            d = float(d)
            e = float(e)

            if d == 0 and e == 0 :
                Solve_Cubic_Equation_var_1 = b
                Solve_Cubic_Equation_var_2 = (b * b - 4 * a * c) ** 0.5
                Solve_Cubic_Equation_var_3 = 2 * a
                return 'x = ' + str(-Solve_Cubic_Equation_var_1 + Solve_Cubic_Equation_var_2) / (Solve_Cubic_Equation_var_3)
            else :
                Solve_Cubic_Equation_xess = [x*0.001 for x in range(2*-100000, 2*100000+1)]

                for l in Solve_Cubic_Equation_xess :
                    if ((a*l ** 3) + (b*l**2) + (c * l) + (d) == e) :
                        return 'x = ' + str(l)
                        break
                    else :
                        continue  

        elif 'x^2' in r :
            if not '=' in r :
                r += '=0'

            a = list(r.split("x^2"))[0]
            b = r.replace(str(a)+"x^2+","").replace(str(a)+"x^2","")
            b = b.split("x")[0]
            var2 = "+"+str(b) if float(b) > 0 else str(b)
            c = r.replace(str(a)+"x^2"+str(var2)+"x"+"+","").replace(str(a)+"x^2"+str(var2)+"x","")
            c = c.split("=")[0].replace("+","")
            d = r.split("=")[1]

            a = float(a)
            b = float(b)
            c = float(c)
            d = float(d)


            Solve_Quadratic_Equation_var_0 = c + (-d)
            Solve_Quadratic_Equation_var_1 = -b
            Solve_Quadratic_Equation_var_2 = (b * b - 4 * a * Solve_Quadratic_Equation_var_0) ** 0.5
            Solve_Quadratic_Equation_var_3 = 2 * a
            return 'x = ' + str((Solve_Quadratic_Equation_var_1 + Solve_Quadratic_Equation_var_2) / (Solve_Quadratic_Equation_var_3))

        elif 'x' in r :
            a = r.split('x')[0]
            b = r.replace(str(a)+'x','').split('=')[0]
            c = r.split('=')[1]
            a = float(a)
            b = float(b)
            c = float(c)
        
            var1 = c + (-b)
            return 'x = ' + str(var1/a)
        else :
            return eval(Equation.replace('^','**'))
    except :
        return 'Error'
        

put_html('<h1>zezn Equation</h1>')
eq = input_group('Enter an Equation to Solve it !'
    ,[
        input(name='Eq')
    ]
)

put_text('Result : ' + str(solve_r(eq['Eq'])))
input()
