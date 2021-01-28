## Projeto-AB2-Redes de Computadores

# Alunos:

Hugo Gabriel de Melo Santos
Larissa Duarte Santana

# Descrição

O projeto se trata de um conversor binário, no qual pode fazer a conversão tanto de texto para binário, quanto de binário para texto.

# Para executar

Após extrair o Zip para uma pasta, apenas execute primeiramente o servidor utilizando o comando :

* **python3 server.py

E após executar o servidor, apenas repita o mesmo processo pro cliente:

* **python3 client.py

# Funcionalidades

Ao executar o servidor, ele irá ficar no aguardo de um cliente fazer a conexão.
Após um cliente fazer a conexão, receberá uma mensagem para escolher o que ele quer fazer.

* Ao escolher 'CODIFICAR' você irá codificar qualquer texto digitado a seguir para o sistema numérico binário
* Ao 'DECODIFICAR' você irá decodificar qualquer número binário em texto. **Cada byte binário deve está separado por espaço, ou seja, 01010000 10100000 00000000.
* Ao desconectar, o cliente será desconectado do servidor.


