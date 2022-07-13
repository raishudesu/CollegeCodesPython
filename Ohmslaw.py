connection = int(input('Series(1) or Parallel(2)?: '))

def series():
    try:
        volts = int(input('Input your Volts: '))
        r1 = int(input('Input R1: '))
        r2 = int(input('Input R2: '))
        
        rtotal = r1 + r2
        total_current = volts/rtotal
        v_r1 = total_current*r1
        v_r2 = total_current*r2
        i_r1 = total_current
        i_r2 = total_current
        if r1 and r2 < 0:
            print('Invalid resistor value!')

        elif r1 == 0:
            print('Total resistance: ', rtotal)
            print('Total current: ', total_current)
            print('V_R2: ', v_r2)
            print('I_R2: ', i_r2)
    
        else:
            print('Total resistance: ', rtotal)
            print('Total current: ', total_current)
            print('V_R1: ', v_r1)
            print('V_R2: ', v_r2)
            print('I_R1: ', i_r1)
            print('I_R2: ', i_r2)

    except ValueError:
        print('Invalid input!')


def parallel():
    try:
        volts = int(input('Input your Volts: '))
        r1 = int(input('Input R1: '))
        r2 = int(input('Input R2: '))
        
        rtotal = (r1*r2)/(r1+r2)
        I_R1 = volts/r1
        I_R2 = volts/r2
        total_current = I_R1 + I_R2
        V_R1 = I_R1*r1
        V_R2 = I_R2*r2
        if r1 and r2 < 0:
            print('Invalid resistor value!')
        
        else:
            print('Total resistance: ', rtotal)
            print('Total current: ', total_current)
            print('V_R1 : ', V_R1)
            print('V_R2 : ', V_R2)
            print('I_R1 : ', I_R1)
            print('I_R2 : ', I_R2)

    except ValueError:
        print('Invalid input!')
    except ZeroDivisionError:
        print('Invalid resistor value!')

if connection == 1:
    series()

elif connection == 2:
    parallel()

else:
    print('Invalid Values')
    