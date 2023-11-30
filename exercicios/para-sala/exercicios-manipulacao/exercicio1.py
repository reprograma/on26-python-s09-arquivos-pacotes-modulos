with open('.testeCriandoArquivoDoZero.txt', 'w') as teste:
    teste.write("Eu vou conseguir entregar todas as tarefas da Reprograma e vou realizar esse sonho porque eu mereço e foda-se tudo.")
    
with open('.testeCriandoArquivoDoZero.txt', 'r') as teste:
    conteudo = teste.read()
    print (conteudo)