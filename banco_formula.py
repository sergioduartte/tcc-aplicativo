#Verificação de Esbeltez
def esbeltezEmX(lb, Kx, ix):
    esbeltezx = (Kx * lb)/ix    
    print(f'Esbeltez em x: {esbeltezx}')
    return esbeltezx
    

def esbeltezEmY(lb, Ky, iy):
    esbeltezy = (Ky * lb)/iy
    print(f'Esbeltez em y: {esbeltezy}')
    return esbeltezy

#Cálculo da força axial de flambagem elástica
""" def b_tlimAlma(SQRT_E_fy, d_t, Qa, Ca, to, Aef, Bef, Ag, ho):
    b_tlim = 1.49 * (SQRT_E_fy)
    if b_tlim > d_t:
        Bef = 1
        Aef = 1
        Qa = 1
        print(f'Qa é: {Qa}')
    else: 
        Bef = 1.92*to*SQRT_E_fy*(1-(Ca/to)*SQRT_E_fy)
        Aef = Ag-((to-Bef)*ho)
        Qa = Aef/Ag
        print(f'Qa é: {Qa}')
        print(f'b/t limite da Alma é: {b_tlim}')


def b_tlimMesa(SQRT_E_fy, bf_2t, Qs, Ca, to):
    b_tlim = 0.56 * (SQRT_E_fy)
    if b_tlim > bf_2t:
        Qs = 1
    else: 
        Qs = 1.92*to*SQRT_E_fy*(1-(Ca/to)*SQRT_E_fy)
        print(f'Qs é: {Qs} e Q = {Qs}')
        print(f'b/t limite da Mesa é: {b_tlim}') """


#valores de entrada
momentord = 100
cortanterd = 79.8
axialrd = 36.93
lb = 780
Kx = 1
Ky = 1
Kz = 1


#sobre o perfil
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

Qs = 1 
Qa = 1
Bef = 1
Aef = 1
Ca = 0.34


# Sobre o aço
fy = 250
E = 200000
G = 77000
SQRT_E_fy = 24.07717062

esbeltezEmX(Kx,lb,ix)
esbeltezEmY(Ky,lb,iy)
""" b_tlimAlma(SQRT_E_fy, d_t, Qa, Ca, to)
b_tlimMesa(SQRT_E_fy, d_t, Qa, Ca, to, Ag, Bef, Aef, ho) """