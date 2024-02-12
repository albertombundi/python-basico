"""import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {} tem seno de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ângulo, tangente))"""

from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('O angulo de {} tem seno de {:.2f}'.format(ângulo, seno))
print('O ângulo de {} tem cosseno de {:.2f}'.format(ângulo, cosseno))
print(' O ângulo de {} tem tangente de {:.2f}'.format(ângulo, tangente))









