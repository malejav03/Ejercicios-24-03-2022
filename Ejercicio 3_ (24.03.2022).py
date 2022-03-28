from tkinter.ttk import Label


letras="QWRTYPSDFGHJKLZXCVBNM"
nif="12345678"
digitos= letras[int (nif)%23]
nif= nif+ digitos

print(nif)