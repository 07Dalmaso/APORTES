#Progama para cacular 
import matplotlib.pyplot as plt

pmt = float(input("Digite o valor mensal que deseja economizar: "))
years = 10
rate = 0.12
n = years * 12
fv = 0

fv_list = []
for i in range(1, years+1):
    fv = (fv + pmt) * (1 + rate/12)**12
    fv_list.append(fv)

plt.bar(range(1, years+1), fv_list)
plt.xlabel('Anos')
plt.ylabel('Valor Futuro (R$)')
plt.title('Evolução do valor ao longo de 10 anos')
plt.show()
print("O valor futuro é de R${:.2f}".format(fv))
#Progama para cacular 