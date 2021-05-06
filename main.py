import os 


def start():
  print('Olá, bem-vindo ao simulado')
  name = input('Qual é seu nome: ')
  email = input('Digite seu email: ')
  #oferecer o menu de opções
  os.system('clear')
  
  def processar(resposta):
    if resposta == '1':
      print('Aqui está o link: https://docs.python.org/3/tutorial/')
    elif resposta == '2':
      print('Aqui está o link: https://docs.djangoproject.com/en/3.1/intro/tutorial01/')
    elif resposta == '3':
      print('Aqui está o link: https://selenium-python.readthedocs.io/getting-started.html ')  
    elif resposta == '4':
      print('Aqui está o link: https://github.com/GustavoGomes9')
    else:
      print('Digite 1, 2, 3 ou 4')
  
  while True:
    resposta = input(f"Oque gostaria de encontrar hoje? {os.linesep}[1] - Python tutorial {os.linesep}[2] - Django tutorial {os.linesep}[3] - Selenium tutorial {os.linesep}[4] - Meu github {os.linesep}")
  #processar os dados 

  processar(resposta)

if __name__ == '__main__':
  start()