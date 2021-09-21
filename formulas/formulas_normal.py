import math
from formulas.variaveis import *



#Validadores dos valores passados serão nas funcoes

#Verificação de Esbeltez
def esbeltez_em_x(lb, Kx, ix):
    esbeltez_x = (Kx * lb) / ix
    return esbeltez_x
    

def esbeltez_em_y(lb, Ky, iy):
    esbeltez_y = (Ky * lb) / iy
    return esbeltez_y

#TODO
def esbeltez_em_z(jooj):
    # TODO
    return -1

#Cálculo da força axial de flambagem elástica
def b_tlim_alma(SQRT_E_fy, d_t, Ca, to, Ag, ho):
    b_tlim = 1.49 * (SQRT_E_fy)
    if d_t <= b_tlim:
        Qa = 1
        print('=============')
        print(f'Qa é: {Qa}')
        print(f'b/t limite da Alma é: {b_tlim}')
        print('=============')
        return Qa
    else: 
        Bef = 1.92 * to * SQRT_E_fy * (1-(Ca/to) * SQRT_E_fy)
        Aef = Ag-((to-Bef)*ho) # TODO PERGUNTAR AO ORIENTADOR
        Qa = Aef/Ag
        print('=============')
        print(f'Qa é: {Qa}')
        print(f'b/t limite da Alma é: {b_tlim}')
        print('=============')
        return Qa


def b_tlim_mesa(Qa, SQRT_E_fy, bf_2t, E, fy):
    b_tlim = 0.56 * (SQRT_E_fy)
    if bf_2t <= b_tlim:
        Qs = 1
        print('=============')
        print(f'Qs é: {Qs}')
        print(f'b/t limite da Mesa é: {b_tlim}')
        print('=============')
    else: 
        if bf_2t <= 1.03 * SQRT_E_fy:
            Qs = 1.415 - (0.74 * bf_2t * SQRT_E_fy) #TODO PERGUNTAR AO ORIENTADOR O VALOR CORRETO
            print('=============')
            print(f'Qs é: {Qs} e Q = {Qs}')
            print(f'b/t limite da Mesa é: {b_tlim}')
            print('=============')
        else:
            Qs = (0.69 * E) / (fy * (bf_2t ** 2))
            print('=============')
            print(f'Qs é: {Qs} e Q = {Qs}')
            print(f'b/t limite da Mesa é: {b_tlim}')
            print('=============')
    Q = Qs * Qa
    return Q

def Ne_x(E, Ix, Kx, lb):
    pi = math.pi
    ne_x = ((pi**2) * E * Ix) / (Kx * lb)**2
    print('=============')
    print(f'Nex é: {ne_x}')
    print('=============')
    return ne_x

def Ne_y(E, Iy, Ky, lb):
    pi = math.pi
    ne_y = ((pi**2) * E * Iy) / (Ky * lb)**2
    print('=============')
    print(f'Ney é: {ne_y}')
    print('=============')
    return ne_y


def Ne_z(Cw, G, J, E, ix, iy, Kz, lb):
    pi = math.pi
    ro_2 = (ix ** 2) + (iy ** 2)
    print('=============')
    print(f'ro2 é: {ro_2}')
    print('=============')
    ne_z = (1 / ro_2) * (((pi **2) * E * Cw) / ((Kz * lb) **2) + G * J)
    print('=============')
    print(f'Nez é: {ne_z}')
    print('=============')
    return ne_z


def Nc(Ne_x, Ne_y, Ne_z):
    print('=============')
    print(f'Nc é: {min(Ne_x, Ne_y, Ne_z)}')
    print('=============')
    return min(Ne_x,Ne_y,Ne_z)


def lambda_0(Q, Ag, fy, Nc):
    lambda_0 = math.sqrt((Q * Ag * fy) / Nc)
    print('=============')
    print(f'Lambda0 é: {lambda_0}')
    print('=============')
    return lambda_0


def Chi(lambda_0):
    lambda_0_2 = lambda_0 ** 2
    if lambda_0 <= 1.5:
        chi = 0.658 ** lambda_0_2
        print('=============')
        print(f'Chi é: {chi}')
        print('=============')
    else:
        chi = 0.877 / lambda_0_2
        print('=============')
        print(f'Chi é: {chi}')
        print('=============')
    return chi


def Nc_Rd(Chi, Q, Ag, fy, Gama_a1):
    Nc_Rd = (Chi * Q * Ag * fy) / Gama_a1
    print('=============')
    print(f'Nc_Rd é: {Nc_Rd}')
    print('=============')
    return Nc_Rd


def resiste(normalsd, lb, Kx, Ky, Kz):
    Qa = b_tlim_alma(SQRT_E_fy, d_t, Ca, to, Ag, ho)
    Q = b_tlim_mesa(Qa, SQRT_E_fy, bf_2t, E, fy)
 
    Ne_x1 = Ne_x(E, Ix, Kx, lb)
    Ne_y1 = Ne_y(E, Iy, Ky, lb)
    Ne_z1 = Ne_z(Cw, G, J, E, ix, iy, Kz, lb)
 
    Nc1 = Nc(Ne_x1, Ne_y1, Ne_z1)
 
    lambda_01 = lambda_0(Q, Ag, fy, Nc1)
    Chi1 = Chi(lambda_01)
    Nc_Rd1 = Nc_Rd(Chi1, Q, Ag, fy, Gama_a1)
 
    if normalsd <= Nc_Rd1:
        return "resiste"
    else: 
        return "não resiste"

esbeltez_em_x(Kx,lb,ix)
esbeltez_em_y(Ky,lb,iy)