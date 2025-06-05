prompt = '\nEscribe algo para que el loro repita'
prompt += '\nIngresa "Salir" para finalizar el programa'

active = True

while active:
    mensaje = input(prompt)

if mensaje == 'salir':
    active = False
else:
    print(mensaje)