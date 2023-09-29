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

# Arquivo 

Em Python, um arquivo é uma representação em disco de um conjunto de dados organizados. Você pode usar arquivos para armazenar informações, como texto, imagens, áudio, vídeo e muito mais. A manipulação de arquivos em Python é feita usando funções e métodos fornecidos pela linguagem, principalmente usando objetos do tipo `file`.

Aqui estão os passos básicos para trabalhar com arquivos em Python:

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

Manipular arquivos em Python é uma tarefa essencial para muitos tipos de aplicativos e oferece a flexibilidade de armazenar e recuperar dados de forma persistente. Certifique-se de sempre fechar arquivos corretamente e seguir as práticas recomendadas para evitar problemas de manipulação de arquivos.


## Leitura de Arquivos:

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

## Escrita em Arquivos:

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

## Movendo o Cursor do Arquivo:

O cursor de leitura/escrita do arquivo é uma posição dentro do arquivo onde a próxima operação ocorrerá. Você pode mover o cursor usando o método `seek()`.

```python
with open('exemplo.txt', 'r') as arquivo:
    arquivo.seek(5)  # Move o cursor para a posição 5 (6ª posição, índice base 0)
    dados = arquivo.read()
```

## Verificação da Posição do Cursor:

Para verificar a posição atual do cursor no arquivo, você pode usar o método `tell()`.

```python
with open('exemplo.txt', 'r') as arquivo:
    posicao = arquivo.tell()
    print(f'A posição atual do cursor é {posicao}')
```

Lembre-se de que é importante fechar o arquivo após usá-lo, principalmente ao usar o gerenciador de contexto `with`. Isso ajuda a evitar problemas de perda de dados ou bloqueio de arquivo.

 

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

