"""
Mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 ate 0 com
uma pausa de 1 segundo entre elas.
"""
import time

for c in range(10, -1, -1):
    time.sleep(1)
    print(c)
print('FIM')