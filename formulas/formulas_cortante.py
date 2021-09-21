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
Cw = 236422

Ca = 0.34
Gama_a1 = 1.1

#variáveis do cortante
Kv = 5

# Sobre o aço
fy = 34.5 #kN/cm²
E = 20000 #kN/cm²
G = 7700 #kN/cm²
SQRT_E_fy = math.sqrt(E/fy)
SQRT_Kv_E_fy = math.sqrt((Kv * E)/fy)


def esbeltez_em_v(d_t):
    esbeltez_em_v = d_t
    print('=============')
    print(f' Esbeltez é {esbeltez_em_v}')
    print('=============')
    return esbeltez_em_v


def esbeltplast (SQRT_Kv_E_fy):
    esbelt_plast = 1.10*SQRT_Kv_E_fy
    print('=============')
    print(f' Esbeltez Plástica é {esbelt_plast}')
    print('=============')
    return esbelt_plast



esbeltez_em_v(d_t)
esbeltplast(SQRT_Kv_E_fy)