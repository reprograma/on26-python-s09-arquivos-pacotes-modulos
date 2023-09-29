<h1 align="center">
  <img src="assets/reprograma-fundos-claros.png" alt="logo reprograma" width="500">
</h1>

# Tema da Aula

Turma Online 0n26 | Python | Semana 9 | 2023 | Professora Daviny Letícia

# Instruções
Antes de começar, vamos organizar nosso setup.
* Fork esse repositório 
* Clone o fork na sua máquina (Para isso basta abrir o seu terminal e digitar `git clone url-do-seu-repositorio-forkado`)
* Entre na pasta do seu repositório (Para isso basta abrir o seu terminal e digitar `cd nome-do-seu-repositorio-forkado`)
* [Add outras intrucoes caso necessario]

# Resumo
O que veremos na aula de hoje?
* [Tema1](#tema1)
* [Tema2](#tema2)
* [Tema3](#tema3)

Claro, aqui está um texto abrangente sobre manipulação de arquivos em Python que pode ser usado em sala de aula:

---
# Manipulação de Arquivos em Python

## Introdução

A manipulação de arquivos é uma tarefa fundamental em programação. Ela permite que você crie, leia, escreva e manipule informações em arquivos de diversos tipos, como texto, CSV e JSON. Em Python, essa tarefa é realizada de maneira eficaz e simples.

## Abrindo Arquivos

Para começar a trabalhar com arquivos em Python, você precisa abrir o arquivo desejado. Use a função `open()` para isso, especificando o nome do arquivo e o modo de abertura, que pode ser leitura, escrita ou anexação, entre outros.

Exemplo de abertura de um arquivo para leitura:

```python
with open('arquivo.txt', 'r') as arquivo:
    # Código para leitura ou manipulação do arquivo aqui
```

O uso do gerenciador de contexto `with` é recomendado, pois ele garante que o arquivo será fechado corretamente após o uso.

## Leitura de Arquivos de Texto

A leitura de arquivos de texto é uma operação comum. Você pode usar métodos como `read()`, `readline()` e `readlines()` para ler o conteúdo do arquivo.

Exemplo de leitura de um arquivo de texto:

```python
with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo
    linha = arquivo.readline()  # Lê uma linha do arquivo
    linhas = arquivo.readlines()  # Lê todas as linhas do arquivo em uma lista
```

## Escrita em Arquivos de Texto

Para escrever em arquivos de texto, use o modo de abertura `'w'` (escrita) ou `'a'` (anexação) ao abrir o arquivo. Você pode usar o método `write()` para adicionar texto ao arquivo.

Exemplo de escrita em um arquivo de texto:

```python
with open('arquivo.txt', 'w') as arquivo:
    arquivo.write('Este é um exemplo de escrita em arquivo.')
```

## Manipulação de Arquivos CSV

Arquivos CSV (Comma Separated Values) são amplamente usados para armazenar dados tabulares. Em Python, você pode usar a biblioteca `csv` para ler e escrever dados em arquivos CSV.

Exemplo de leitura de um arquivo CSV:

```python
import csv

with open('dados.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        # Trabalhe com os dados da linha aqui
```

Exemplo de escrita em um arquivo CSV:

```python
import csv

dados = [['Nome', 'Idade'], ['Alice', 30], ['Bob', 25]]

with open('pessoas.csv', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerows(dados)
```

## Manipulação de Arquivos JSON

JSON (JavaScript Object Notation) é um formato de dados muito utilizado para armazenar e trocar informações estruturadas. Em Python, você pode usar a biblioteca `json` para trabalhar com arquivos JSON.

Exemplo de leitura de um arquivo JSON:

```python
import json

with open('dados.json', 'r') as arquivo_json:
    dados = json.load(arquivo_json)
    # Trabalhe com os dados carregados aqui
```

Exemplo de escrita em um arquivo JSON:

```python
import json

dados = {'nome': 'Alice', 'idade': 30, 'cidade': 'Exemploville'}

with open('dados.json', 'w') as arquivo_json:
    json.dump(dados, arquivo_json)
```


1. **Abrir um Arquivo:**
   Você pode abrir um arquivo usando a função `open()`. Esta função aceita dois argumentos principais: o nome do arquivo e o modo de abertura (leitura, escrita, etc.). Os modos mais comuns são:
   - `'r'`: Modo de leitura (default).
   - `'w'`: Modo de escrita (cria um novo arquivo ou sobrescreve o existente).
   - `'a'`: Modo de anexação (adiciona ao final do arquivo).
   - `'b'`: Modo binário (para arquivos binários, como imagens ou áudio).
   
   Exemplo de abertura de um arquivo para leitura:
   ```python
   arquivo = open('exemplo.txt', 'r')
   ```

2. **Ler Dados de um Arquivo:**
   Para ler dados de um arquivo, você pode usar o método `read()` ou métodos de iteração como `readline()` ou `readlines()`.

   Exemplo de leitura de todo o conteúdo do arquivo:
   ```python
   conteudo = arquivo.read()
   print(conteudo)
   ```

3. **Escrever Dados em um Arquivo:**
   Para escrever dados em um arquivo, você pode usar o método `write()`.

   Exemplo de escrita em um arquivo:
   ```python
   arquivo = open('exemplo.txt', 'w')
   arquivo.write('Este é um exemplo de escrita em arquivo.')
   arquivo.close()
   ```

4. **Fechar o Arquivo:**
   Sempre é uma boa prática fechar um arquivo após usá-lo com o método `close()`.

   ```python
   arquivo.close()
   ```

5. **Trabalhar com Arquivos Usando o Context Manager (Recomendado):**
   Uma maneira mais segura e recomendada de trabalhar com arquivos é usar o gerenciador de contexto `with`. Isso garante que o arquivo seja fechado automaticamente quando você terminar de usá-lo.

   ```python
   with open('exemplo.txt', 'r') as arquivo:
       conteudo = arquivo.read()
       # Trabalhe com o conteúdo do arquivo dentro deste bloco
   # O arquivo é fechado automaticamente aqui fora do bloco "with"
   ```

6. **Manipulação de Arquivos Binários:**
   Para trabalhar com arquivos binários, como imagens ou áudio, você pode usar o modo de abertura `'rb'` para leitura binária ou `'wb'` para escrita binária.

   Exemplo de leitura de uma imagem binária:
   ```python
   with open('imagem.png', 'rb') as arquivo:
       dados = arquivo.read()
   ```

Lembre-se de tratar exceções ao trabalhar com arquivos, como `FileNotFoundError` ao tentar abrir um arquivo que não existe e `PermissionError` ao tentar escrever em um arquivo sem permissões de escrita.

## Exemplos de Leitura de Arquivos:

1. **`read()`**: Lê todo o conteúdo do arquivo e retorna uma única string com os dados.

   ```python
   with open('exemplo.txt', 'r') as arquivo:
       conteudo = arquivo.read()
   ```

2. **`readline()`**: Lê uma linha do arquivo a cada chamada. Útil para processar arquivos linha por linha.

   ```python
   with open('exemplo.txt', 'r') as arquivo:
       linha = arquivo.readline()
       while linha:
           print(linha)
           linha = arquivo.readline()
   ```

3. **`readlines()`**: Lê todas as linhas do arquivo e retorna uma lista de strings, onde cada string é uma linha do arquivo.

   ```python
   with open('exemplo.txt', 'r') as arquivo:
       linhas = arquivo.readlines()
       for linha in linhas:
           print(linha)
   ```

## Exemplos Escrita em Arquivos:

1. **`write()`**: Escreve uma string no arquivo. Se o arquivo já existir e você usar o modo de escrita `'w'`, ele será sobrescrito.

   ```python
   with open('exemplo.txt', 'w') as arquivo:
       arquivo.write('Este é um exemplo de escrita em arquivo.')
   ```

2. **`writelines()`**: Escreve uma lista de strings no arquivo. Você precisa adicionar manualmente os caracteres de quebra de linha, se desejar.

   ```python
   with open('exemplo.txt', 'w') as arquivo:
       linhas = ['Linha 1\n', 'Linha 2\n', 'Linha 3\n']
       arquivo.writelines(linhas)
   ```

## Exemplos Movendo o Cursor do Arquivo:

O cursor de leitura/escrita do arquivo é uma posição dentro do arquivo onde a próxima operação ocorrerá. Você pode mover o cursor usando o método `seek()`.

```python
with open('exemplo.txt', 'r') as arquivo:
    arquivo.seek(5)  # Move o cursor para a posição 5 (6ª posição, índice base 0)
    dados = arquivo.read()
```

## Exemplos Verificação da Posição do Cursor:

Para verificar a posição atual do cursor no arquivo, você pode usar o método `tell()`.

```python
with open('exemplo.txt', 'r') as arquivo:
    posicao = arquivo.tell()
    print(f'A posição atual do cursor é {posicao}')
```

Lembre-se de que é importante fechar o arquivo após usá-lo, principalmente ao usar o gerenciador de contexto `with`. Isso ajuda a evitar problemas de perda de dados ou bloqueio de arquivo.

## Conclusão

A manipulação de arquivos em Python é uma habilidade essencial para qualquer programador. Ela permite a criação, leitura e escrita de informações em diversos formatos, tornando possível o armazenamento e processamento de dados de forma eficiente. Com as ferramentas e técnicas apresentadas, você estará preparado para lidar com uma variedade de tarefas envolvendo arquivos em seus projetos de programação.


# Pacotes em Python: Organização e Reutilização de Código

## Introdução

Python é uma linguagem de programação poderosa e versátil que oferece suporte à criação de programas complexos e extensíveis. Uma das características essenciais do Python é a capacidade de organizar e reutilizar código de maneira eficaz por meio de pacotes.

## O Que São Pacotes?

Em Python, um pacote é uma maneira de organizar módulos relacionados em um único diretório. Um pacote pode conter módulos Python, bem como outros subpacotes. Essa estrutura hierárquica facilita a organização e a modularização de projetos de grande porte.

Os pacotes são representados como diretórios no sistema de arquivos, e cada diretório contém um arquivo especial chamado `__init__.py`. O `__init__.py` é executado quando o pacote é importado e pode conter código de inicialização.

## Estrutura de um Pacote

A estrutura de um pacote Python típico se parece com isto:

```
meu_pacote/
    __init__.py
    modulo1.py
    modulo2.py
    subpacote/
        __init__.py
        modulo3.py
        modulo4.py
```

Neste exemplo, temos um pacote chamado `meu_pacote` que contém dois módulos (`modulo1.py` e `modulo2.py`) e um subpacote chamado `subpacote`, que também contém módulos (`modulo3.py` e `modulo4.py`). O `__init__.py` em cada diretório é opcional, mas é comumente usado para inicialização e configuração.

## Importação de Pacotes e Módulos

Para usar pacotes e módulos em Python, você precisa importá-los em seu código. Existem várias maneiras de fazer isso:

- Importação de um módulo específico de um pacote:
  ```python
  from meu_pacote import modulo1
  ```

- Importação de um pacote ou subpacote:
  ```python
  import meu_pacote.subpacote
  ```

- Importação com um alias:
  ```python
  import meu_pacote.modulo1 as mod1
  ```

- Importação de todos os módulos de um pacote (não recomendado devido a possíveis conflitos):
  ```python
  from meu_pacote import *
  ```

## Vantagens dos Pacotes

1. **Organização**: Os pacotes ajudam a organizar e estruturar o código de maneira lógica e hierárquica, facilitando a manutenção e a colaboração em projetos maiores.

2. **Reutilização de Código**: Você pode reutilizar módulos e pacotes em diferentes partes do seu projeto ou até mesmo em outros projetos, economizando tempo e esforço.

3. **Isolamento**: Pacotes permitem isolar funcionalidades específicas, reduzindo conflitos de nomes de variáveis e funções em diferentes partes do código.

4. **Facilidade de Distribuição**: Pacotes bem organizados podem ser facilmente compartilhados e distribuídos para outros desenvolvedores por meio do sistema PyPI (Python Package Index).

## Conclusão

Pacotes são uma parte fundamental do ecossistema Python e desempenham um papel crucial na organização e reutilização de código. Ao aprender a criar, usar e distribuir pacotes, você estará equipado para desenvolver projetos mais escaláveis, modulares e de fácil manutenção em Python. Essa habilidade é especialmente importante para aqueles que desejam colaborar em projetos de código aberto e contribuir para a comunidade de desenvolvedores Python.
#
***
### Exercícios 
* [Exercicio para sala](https://github.com/mflilian/repo-example/tree/main/exercicios/para-sala)
* [Exercicio para casa](https://github.com/mflilian/repo-example/tree/main/exercicios/para-casa)

### Material da aula 

### Links Úteis
- [Lorem Ipsum](https://www.lipsum.com/feed/html)
- [Lorem Ipsum](https://www.lipsum.com/feed/html)
- [Lorem Ipsum](https://www.lipsum.com/feed/html)
- [Lorem Ipsum](https://www.lipsum.com/feed/html)


<p align="center">
Desenvolvido com :purple_heart:  
</p>

