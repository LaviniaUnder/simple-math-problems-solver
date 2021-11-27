aviso = '''\nEsse programa vai te ajudar a fazer o calculo de velocidade média
cuja estrutura é assim:
Vm = ΔS/Δt
Para isso vc deve digitar qual valor deseja encontrar:
Digite vm para encontrar a velocidade média
Digite s para encontrar a variação de espaço
ou digite t para encontrar a variação de tempo
vamos começar?'''

print(aviso)

def vel_M (s, t):
    resultado_vm = (s / t)
    return resultado_vm

def espaco (vm,t):
    resultado_s = (vm * t)
    return resultado_s

def tempo (vm, s):
    resultado_t = (s / vm)
    return resultado_t

oq_calcular = (input("\ndigite a opção correspondente ao que deseja encontrar, (vm , s ou t):"))

aviso2 = "\nAo escrever os números com casas decimais, utilize pontos e não virgulas"

if oq_calcular == "vm":
    print (aviso2)
    vari_espaco = float(input("\ndigite a variação de espaço,\n a variação de espaço é o resultado do Intervalo do deslocamento posição final – posição inicial: "))
    vari_tempo = float(input("\ndigite a variação de tempo,\n a variação de tempo é o resultado do Intervalo de tempo final – tempo inicial: "))
    resultadov = vel_M(vari_espaco, vari_tempo)
    print("\nO resultado Vm é: ", resultadov)
elif oq_calcular == "s":
    print (aviso2)
    velocidade_media = float(input("\ndigite a velocidade média:"))
    vari_tempo = float(input("\ndigite a variação de tempo,\n a variação de tempo é o resultado do Intervalo de tempo final – tempo inicial: "))
    resultados = espaco(velocidade_media, vari_tempo)
    print("\nO resultado ΔS é: ", resultados)
elif oq_calcular == "t":
    print (aviso2)
    velocidade_media = float(input("\ndigite a velocidade média:"))
    vari_espaco = float(input("\ndigite a variação de espaço,\n a variação de espaço é o resultado do Intervalo do deslocamento posição final – posição inicial: "))
    resultadot = tempo(velocidade_media, vari_espaco)
    print("\nO resultado Δt é: ", resultadot)
else :
    print("\ndigite uma das opções válidas")