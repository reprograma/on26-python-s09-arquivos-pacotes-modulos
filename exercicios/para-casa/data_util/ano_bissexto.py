import datetime

def eh_ano_bissexto(ano):
  return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0

if __name__ == "__main__":
  ano = 2024
  eh_bissexto = eh_ano_bissexto(ano)
  print(f"O ano {ano} é bissexto? {eh_bissexto}")