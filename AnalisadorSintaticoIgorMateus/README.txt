Execute os seguintes comandos no terminal:

alias uai="python3 main.py"
uai sample_code.uai

O segundo comando pode ser modificado para compilar outros arquivos de código substituindo o arquivo "sample_code.uai" pelo arquivo desejado.

Para executar apenas o analisador léxico, basta rodar o comando "python3 lexico.py"
Para executar apenas o analisador sintático, basta rodar o comando "python3 sintatico.py".

O compilador do Mineirin# requer o Python3 instalado com a biblioteca Pandas.

--------------------------------------------------------------------------------------------------------------------------------------------
O arquivo "sample_code.uai" apresenta um exemplo de código sem erros, enquanto o arquivo "sample_code_error.uai" apresenta um exemplo de código com erros sintáticos.

Dentre os erros sintáticos presentes no arquivo "sample_code_error.uai", dois erros são específicos do Mineirin#, estando eles presentes nas linhas 14 e 36. O primeiro se dá pois o Mineirin# não permite que ocorra uma operação lógica, aritmética ou relacional na mesma linha em que uma variável é declarada, devendo-se primeiro declarar uma variável para depois efetuar-se operações com ela. Já o segundo ocorre pois o Mineirin# não aceita a utilização de parênteses redundantes.

Os demais erros sintáticos introduzidos são mais facilmente identificados conforme especificação da linguagem.
