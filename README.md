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

- 1.0 criar um ambiente virtual 

- 2.0 instalar as dependências 
- 2.1 $ pip install Flask
- 2.2 $ pip install enigmamachine **biblioteca**

[Site da biblioteca com a documentação da funções](https://pypi.org/project/enigmamachine/)

- 3.0 rodar o arquivo app.py 
- rodar o próprio arquivo ou com o terminal na raiz do projeto inserir o comando $ flask run 

- 4.0 demo.ipynb
arquivo com teste: das funções, da api e da biblioteca

- 5.0 Teste rápidos no último campo da demo

### Modelo matemático

`to_one_hot`

O modelo matemático da função é simplesmente uma operação de transformação do texto original em um vetor binário de tamanho fixo, onde cada linha corresponde a uma letra do alfabeto mais um espaço em branco e cada coluna a um dos carácteres representados na mensagem, sendo que a posição correspondente a letra na mensagem recebe 1 e todas as outras recebem 0.

`to_string`
A função to_string recebe uma matriz no formato one-hot encoding como entrada e retorna a mensagem correspondente. O modelo matemático é o inverso da função to_one_hot: é uma operação que transforma uma matriz de vetores one-hot em uma sequência de caracteres.

`encrypt`
A função irá receber uma mensagem e transformar ela na sua representação matricial one_hot. O outro argumento recebido pela função é a matriz permutação, a matriz permutação é uma matriz identidade onde suas linhas foram trocadas de ordem ou permutadas. Uma vez que uma Matriz Identidade(27) multiplicada por uma matriz M resulta na própria matriz M (mensagem igual), uma matriz permutação irá resultar em uma matriz M_permutada onde cada carácter da mensagem foi permutado para um diferente.
Sendo assim a função ira transformar a matriz M_permutada em sua representação em string e retornar a mensagem cifrada.

M_PERMUTACAO @ M = M_PERMUTADA

`encrypt`
A função irá receber uma mensagem cifrada e a matriz_permutacao que foi utilizada pra cifrar ela.
Tansformar a mensagem cifrada em sua representação matricial e uma vez que para a cifrar vale:

M_PERMUTACAO @ M = M_PERMUTADA

para decifrar vale:

M = M_PERMUTACAO(inversa)  @ M_PERMUTADA

Ao recuperar a matrix original retorna a mensagem original.

`enigma_machine`  
A função enigma_machine recebe uma mensagem, uma matriz de permutação e uma matriz auxiliar como entrada e retorna a mensagem criptografada utilizando a técnica do Enigma Machine. A mensagem é criptografada da seguinte forma: cada caractere da mensagem é criptografado pela matriz de permutação, e em seguida, a mensagem criptografada é criptografada novamente pela matriz auxiliar, repetindo esse processo para cada caractere da mensagem. A função encrypt é utilizada para criptografar cada caractere da mensagem.

Exemplo:

teste mensagem:

--> M_P @ M(t) = M(t)_PERMUTADO 
--> M_A @ M_P @ M(e) = M(e)_PERMUTADO 
--> M_A @  M_A @ M_P @ M(s) = M(s)_PERMUTADO 
--> M_A @ M_A @  M_A @ M_P @ M(t) = M(t)_PERMUTADO 
--> M_A @ M_A @ M_A @  M_A @ M_P @ M(e) = M(e)_PERMUTADO 

`enigma_machine_decrypt`  
A função enigma_machine_decrypt recebe uma mensagem criptografada utilizando o Enigma Machine, uma matriz de permutação e uma matriz auxiliar como entrada e retorna a mensagem original. A mensagem é descriptografada da seguinte forma: cada caractere da mensagem criptografada é descriptografado pela matriz auxiliar, e em seguida, a mensagem descriptografada é descriptografada novamente pela matriz de permutação, repetindo esse processo para cada caractere da mensagem criptografada. A função decrypt é utilizada para descriptografar cada caractere da mensagem criptografada.


Exemplo:

teste mensagem:

--> M(t) = M_P(inv) @  M(t)_PERMUTADO 
--> M(e) = M_A(inv) @  M_P(inv) @  M(e)_PERMUTADO 
--> M(s) = M_A(inv) @  M_A(inv) @  M_P(inv) @  M(s)_PERMUTADO 
--> M(t) = M_A(inv) @ M_A(inv) @  M_A(inv) @  M_P(inv) @  M(t)_PERMUTADO 
--> M(e) = M_A(inv) @ M_A(inv) @ M_A(inv) @  M_A(inv) @  M_P(inv) @  M(t)_PERMUTADO 
