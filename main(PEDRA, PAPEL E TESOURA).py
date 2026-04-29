import random
vitoriaDoJogador=0
vitoriaDoPC=0

def jogadas():
  jogador = input("Entre sua escolha (pedra, papel, tesoura): ")
  opções = ["pedra", "papel","tesoura"]
  computador = random.choice(opções)
  escolhas = {"Jogador": jogador, "computador":computador}
  return escolhas

def verificarVitoria(jg, pc):
  print(f"Você: {jg}. Computador: {pc}.")
  if jg == pc:
   return "EMPATE!" 
  elif jg == "pedra":
    if pc == "tesoura":
      
      return "pedra derrota tesoura! FATALITY!"
    else:
      
      return "papel cobre pedra. Se FU***."
  elif  jg == "papel":
    if pc == "pedra":
      
      return "papel cobre pedra! FATALITY!"
    else:
      
      return "papel foi triturado pelas tesouras. Se FU***."    
  elif jg == "tesoura":
    if pc == "papel":
      
      return "tesoura tritura o papel! FATALITY!"
  else:
    
    return "tesouras foi esmagada pela pedra. Se FU***."
   
escolhas = jogadas()
result = verificarVitoria(escolhas["Jogador"], escolhas["computador"])
print(result)
print(f'Pontuação:\
    Jogador:{vitoriaDoJogador} PC:{vitoriaDoPC}')



  