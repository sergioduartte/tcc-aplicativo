import math

#valores de entrada
momentord = 100
cortanterd = 79.8
axialrd = 36.93
lb = 780
Kx = 1
Ky = 1
Kz = 1


#sobre o perfil w310x52
m = 52
h = 317
Ag = 67.0
to = 7.6
ho = 291
tf = 13.20
bf = 167
Ix = 11909
Wx = 751.4
ix = 13.33
Zx = 852.5
Iy = 1026
Wy = 122.9
iy = 3.91
Zy = 31.8
J = 31.81
bf_2t = 6.33
d_t = 35.61
Cw = 236.422

Ca = 0.34
Gama_a1 = 1.1


# Sobre o aço
fy = 345
E = 200000
G = 77000
SQRT_E_fy = math.sqrt(E/fy)

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
        print('=============')
    else: 
        if bf_2t <= 1.03 * SQRT_E_fy:
            Qs = 1.415 - (0.74 * bf_2t * SQRT_E_fy) #TODO PERGUNTAR AO ORIENTADOR O VALOR CORRETO
            print('=============')
            print(f'Qs é: {Qs} e Q = {Qs}')
            print('=============')
        else:
            Qs = (0.69 * E) / (fy * (bf_2t ** 2))
            print('=============')
            print(f'Qs é: {Qs} e Q = {Qs}')
            print('=============')
    Q = Qs * Qa
    return Q

def Ne_x(E, Ix, Kx, lb):
    pi = math.pi
    ne_x = ((pi**2) * E * Ix) / (Kx * lb)**2
    return ne_x

def Ne_y(E, Iy, Ky, lb):
    pi = math.pi
    ne_y = ((pi**2) * E * Iy) / (Ky * lb)**2
    return ne_y

def Ne_z(Cw, G, J, E, ix, iy, Kz, lb):
    pi = math.pi
    ro_2 = (ix * iy) ** 2
    ne_z = (1 / ro_2) * (((pi **2) * E * Cw) / ((Kz * lb) **2)) + G * J
    return ne_z

def Nc(Ne_x, Ne_y, Ne_z):
    return min(Ne_x,Ne_y,Ne_z)

def lambda_0(Q, Ag, fy, Nc):
    lambda_0 = math.sqrt((Q * Ag * fy) / Nc)
    return lambda_0

def Chi(lambda_0):
    lambda_0_2 = lambda_0 ** 2
    if lambda_0 <= 1.5:
        chi = 0.658 ** lambda_0_2
    else:
        chi = 0.877 / lambda_0_2
    return chi

def Nc_Rd(Chi, Q, Ag, fy, Gama_a1):
    Nc_Rd = (Chi * Q * Ag * fy) / Gama_a1
    return Nc_Rd

esbeltez_em_x(Kx,lb,ix)
esbeltez_em_y(Ky,lb,iy)

Qa = b_tlim_alma(SQRT_E_fy, d_t, Ca, to, Ag, ho)
Q = b_tlim_mesa(Qa, SQRT_E_fy, bf_2t, E, fy)

Ne_x = Ne_x(E, Ix, Kx, lb)
Ne_y = Ne_y(E, Iy, Ky, lb)
Ne_z = Ne_z(Cw, G, J, E, ix, iy, Kz, lb)

Nc = Nc(Ne_x, Ne_y, Ne_z)

lambda_0 = lambda_0(Q, Ag, fy, Nc)
Chi = Chi(lambda_0)
Nc_Rd = Nc_Rd(Chi, Q, Ag, fy, Gama_a1)

print(Nc_Rd)