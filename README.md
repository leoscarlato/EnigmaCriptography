# EnigmaCriptography

## Funções para criptografia com máquina Enigma
As funções a seguir são utilizadas para criptografar e descriptografar mensagens com a máquina Enigma. A máquina Enigma foi uma máquina de criptografia usada principalmente durante a Segunda Guerra Mundial pela Alemanha para proteger suas comunicações militares.

### Função to_one_hot(message)
Esta função converte uma mensagem em uma matriz unidimensional de one-hot encoding. Cada caracter da mensagem é transformado em um vetor que contém um 1 na posição correspondente do alfabeto em que se encontra e zeros em todas as outras posições. O alfabeto inclui as 26 letras maiúsculas e minúsculas do inglês, além do espaço em branco.

A função retorna uma matriz bidimensional em que cada coluna representa um caracter da mensagem.

### Função to_string(matrix)
Esta função converte uma matriz gerada pela função ***to_one_hot(message)*** em uma string correspondente à mensagem original. A matriz deve ser bidimensional, onde cada coluna representa um caracter da mensagem.

A função procura o índice em cada coluna que contém o valor 1 e retorna a letra correspondente a esse índice no alfabeto.

### Função encrypt(message, permutation_matrix)
Esta função criptografa uma mensagem utilizando uma matriz de permutação. A mensagem é primeiro convertida em uma matriz unidimensional usando a função ***to_one_hot(message)***. Em seguida, a matriz de permutação é multiplicada pela matriz unidimensional para obter a matriz criptografada.

A função retorna a mensagem criptografada como uma string, usando a função ***to_string(matrix)*** para converter a matriz criptografada de volta em uma string.

### Função decrypt(encrypted_message, permutation_matrix)
Esta função descriptografa uma mensagem criptografada com a função ***encrypt()***. A mensagem criptografada é primeiro convertida em uma matriz unidimensional usando a função ***to_one_hot(message)***. Em seguida, a matriz de permutação inversa é multiplicada pela matriz unidimensional para obter a matriz original.

A função retorna a mensagem original como uma string, usando a função ***to_string(matrix)*** para converter a matriz original de volta em uma string.

### Função enigma_machine(message, permutation_matrix, auxiliary_matrix)
Esta função criptografa uma mensagem usando a máquina Enigma. A mensagem é criptografada usando a matriz de permutação especificada na função ***encrypt()*** e, em seguida, a mensagem criptografada é criptografada novamente várias vezes usando a matriz auxiliar especificada.

A função retorna a mensagem criptografada como uma string.

### Função enigma_machine_decrypt(encrypted_message, permutation_matrix, auxiliary_matrix)
Esta função descriptografa uma mensagem criptografada com a função ***enigma_machine()***. A mensagem criptografada é descriptografada várias vezes usando a matriz auxiliar especificada e, em seguida, é descriptografada usando a matriz de permutação inversa especificada na função ***decrypt()***.

A função retorna a mensagem original como uma string.

### Instruções 
Primeiros passos

- 1. criar um ambiente virtual 

- 2. instalar as dependências 
- 2.1 $ pip install Flask
- 2.2 $ pip install enigmamachine **biblioteca**

[Site da biblioteca com a documentação da funções](https://pypi.org/project/enigmamachine/)

- 3. rodar o arquivo app.py 
- rodar o próprio arquivo ou com o terminal na raiz do projeto inserir o comando $ flask run 

- 4. demo.ipynb
arquivo com teste: das funções, da api e da biblioteca

- 5. Teste rápidos no último campo da demo
