# Exercício de Casa 🏠 


## Exercício: Criação de Pacote de Manipulação de Datas


Objetivo: Criar um pacote Python chamado "data_util" que contenha módulos para realizar operações relacionadas a datas, como cálculo de idade, verificação de ano bissexto e formatação de datas.

**Parte 1: Criação do Pacote e Módulos**

Crie um diretório chamado "data_util" no mesmo diretório em que você está trabalhando.

Dentro do diretório "data_util", crie os seguintes módulos:

`calculo_idade.py`: Contém uma função calcular_idade(data_nascimento) que recebe uma data de nascimento como argumento e retorna a idade da pessoa.

`ano_bissexto.py`: Contém uma função eh_ano_bissexto(ano) que verifica se um ano é bissexto e retorna True ou False.

`formatar_data.py`: Contém uma função formatar_data(data) que recebe uma data no formato "dd/mm/aaaa" e a formata como "aaaa-mm-dd".

**Parte 2: Uso do Pacote**

Crie um programa principal fora do diretório "data_util" para testar o pacote.

Importe os módulos do pacote "data_util" e use as funções para realizar as seguintes tarefas:

Solicite ao usuário que insira sua data de nascimento no formato "dd/mm/aaaa" e use a função do módulo `calculo_idade.py` para calcular a idade da pessoa.

Verifique se o ano atual é bissexto ou não usando a função do módulo `ano_bissexto.py`.

Solicite ao usuário que insira uma data no formato "dd/mm/aaaa" e use a função do módulo formatar_data.py para exibir a data no formato "aaaa-mm-dd".


```
- Dicas:

Você pode usar a biblioteca datetime para manipular datas em Python.

Certifique-se de organizar seu código de forma que os módulos estejam dentro do diretório "data_util" e o programa principal esteja fora desse diretório.

Teste o seu programa com diferentes datas para garantir que as funções do pacote estejam funcionando corretamente.

Este exercício permitirá às alunas praticar a criação de pacotes em Python e a organização de módulos dentro deles, bem como o uso de funções para realizar tarefas relacionadas a datas.
```

---

Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [ ] Fiz o fork do repositório.
- [ ] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [ ] Resolvi o exercício.
- [ ] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [ ] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [ ] Pushei os commits na minha branch (`git push origin nome-da-branch`)
- [ ] Criei um Pull Request seguindo as orientaçoes que estao nesse [documento](https://github.com/mflilian/repo-example/blob/main/exercicios/para-casa/instrucoes-pull-request.md).
