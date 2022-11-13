# Bem-vindo a “Dragon Adventures”!

*O jogo Dragon Adventure segue um modelo clássico de jogos de role-play onde o jogador controla um grupo de aventureiros com uma serie de características diferentes (i.e. classes).*

![Dragon](https://images6.fanpop.com/image/photos/36700000/Toothless-the-Dragon-image-toothless-the-dragon-36773955-500-210.gif)

###### Projeto realizado por:
* David Mendes (22203255)
* Guilherme Negrinho (22207383)

###### Implementação das mecânicas:
    » David Mendes:
        Criação do Sistema de Combate
        Adição de Novos Personagens

    » Guilherme Negrinho:
        Implmentação do Inventário
        Introdução ao Jogo
        Limpeza da Interface
        Criação do Markdown
    
###### Repositório git:
https://github.com/ArKynn/TextCombat

###### Arquitetura do código:
O código foi orgânizado por 4 partes:
1. Introdução e UI
2. Character stats
3. Auxiliary functions
4. Main function

###### Introdução e UI
Nesta parte, foram criadas duas funções principais responsáveis pelos visuais do jogo.

A introdução consiste numa série de prints para inicializar o jogo.

O UI, com o auxilio da função alive, mostra-nos dinamicamente os stats de cada personagem no momento, bem como quais personagens já morreram.

Também existem pedaços de UI dentro da função principal para dar um feedback melhor ao player ao longo do jogo

###### Character stats
Nesta parte, criou-se uma clase onde foram definidos os diversos stats necessários para cada personagem funcionar dinamicamente no programa.
Estes stats estão interligados a diversas outras funções e variam dinamicamente ao longo ddo jogo.

###### Auxiliary functions
Estas funções consistem em diveros sistemas necessários para que a função principal funcione corretamente.
Dentro destas funções estão as seguintes:
1. Alive: Esta função controla o estado de vida de cada jogador. Esta verifica se os personagens estão vivos ou mortos e separa-os. Também termina o jogo se detetar
    que todos os aliados ou inimigos já morreram. 

2. End_action: Esta função pausa o jogo até o jogador primir a tecla "down", dando melhor controle e feedback do jogo ao jogador.

3. Name_into_variable: Esta função transforma uma string referente ao nome de um personagem na respetiva função de presonagem. Isto é necessário pois algums processos,
    por exemplo: referir o HP do personagem, necessitam da função em si e não de uma string.

###### Main function
Esta é a grande função que consite em todos os sitemas diretamente relacionados ao combate.
Dentro desta existem as seguintes subfunções:
1. d20, d6 e d4: Funções de dado para o sistema de initiative e spell effects

2. Initiative: Esta função agarra em todos os personagens, calcula a soma do init e d20 para cada personagem e ordena-os pela mesma

3. dmg_calc:  Esta função clacula o dano final apartir do ataque e defesa dos personagens envolvidos.

4. rushdown, exorcism e mend: Estas funções fazem os calculos para cada spell

5. item_use: Esta função realiza os efeitos de cada item para os personagens envolvidos

Com o auxilio destas funções todas, o código primeiro retira um personagem da initiative, verifica se é inimigo ou aliado e dependendo da equipa:
    - se for da equipa enimiga, escolhe um aliado e ataca,
    - se for um aliado, dá à escolha atacar, usar item ou magia e processa os calculos para cada. 

###### Referências:
    - Lançar um dado de 20 para Iniciativa;
    - Classificação em ordem de maior para menor Init;
    Recurso: Resposta de "user jws1"
    https://stackoverflow.com/questions/60193710/python-d20-dice-rolling-program
    
    - Personagens vivos não seja desqualificados da lista original;
    Recurso: Reposta de "user Art"
    https://stackoverflow.com/questions/67750705/python-sorting-based-on-class-attribute
    
    - Criar uma segunda simulação sem encerramento total do sistema;
    Recurso:
    https://maschituts.com/how-to-restart-a-program-in-python-explained/
