
# Sqlite - Banco de Dados 1
## Nomes
Gustavo Leão Nogueira de Oliveira, Daniel Christofolli, Tiago Landi

## Histórico
Criado por D. Richard Hipp, é uma biblioteca desenvolvida em linguagem C que é acessa diretamente banco, e que já vem previamente configurada, assim, não necessitando a configuração e conexão com o servidor.
D. Richard Hipp trabalhava com sua equipe da força naval dos estados unidos em um projeto de mísseis teleguiados, onde o banco de dados era o Informix da Ibm, e gerava problemas na inicialização. Por este motivo foi trocado pelo PostgreSQL que ficou extremamente complexo, assim, surgindo a ideia de criar um banco de dados sql que fosse o mais simples possível para leitura e gravação de dados.

## Prós
Esta biblioteca é simples ao máximo, portável por ser feita em linguagem C, pode ser executado no Windows, Linux, Android, IOS, Mac.
Também é Open Source, ou seja, é muito testada, e ainda, pode ser editado o código e feitas outras versões.
A instalação da biblioteca é inferior a 500 KB, o que para um banco de dados é muito leve.
As transações seguem o conceito de ACID (atomicidade, consistência, isolamento e durabilidade).
Não necessita configurações para ser executada.
Armazena os dados em um arquivo no disco.
Prós - Questões de Relacionamento

### Bancos comuns
Os bancos de dados relacionais comuns utilizam-se de um servidor para salvar as informações e os clientes acessam a partir de uma conexão cliente-servidor como na imagem abaixo:
### SQLite
Já o SQLite (a biblioteca) se comunica diretamente com o arquivo que já está juntamente com o programa, assim. ganhando agilidade no acesso e excluindo as configurações que são necessárias nos outros tipos de bancos de dados relacionais.

## Contras
Não é recomendado quando o é necessário controle de acesso (pois o mesmo não tem).
A quantidade de dados a ser armazenados  não podem ser maiores que 2TB.
Não utilizado para grandes projetos,onde há necessidade de gravar conteúdos extensos de dados.
Não tem cliente/servidor nativo.
Não possui chave estrangeira.
Limitação em cláusulas WHERE aninhadas.
Organizações que utilizam
As principais organizações que utilizam são:
Adobe: No Photoshop e no Adobe Reader.
Apple: No Apple Mail e no Safari Web Browser.
McAfee: Nos programas de anti-vírus.
Google: Na plataforma móvel android, e nos aplicativos Google Desktop e Google Gears.
Onde usar
É muitíssimo recomendado para sites com até 100000 requisições por dia, sistemas embarcados, aplicativos desktop e aprendizado de banco de dados. Ou seja, se no projeto for necessária a simplicidade de implementação, manutenção, e administração.

## Exemplo

## Conclusão
Concluímos que a biblioteca SQLite pode ser aplicada em diversas áreas por empresas de pequeno a grande porte, e é uma das mais utilizadas por ser de fácil implementação, ocupar pouquíssimo espaço físico e ser altamente confiável para casos com poucas requisições simultâneas (até 100000 diárias) e com um armazenamento de até 2TB e de fácil implementação. Além de ser multiplataforma e implementada diretamente da linguagem com a importação.


# Referências
https://pt.slideshare.net/theze86/aula-06-tep-introduo-sqlite
https://pt.slideshare.net/apps4ucoza/hands-on-using-sq-lite-database?next_slideshow=1
https://medium.com/opensanca/o-que-%C3%A9-acid-59b11a81e2c6
https://www.sqlite.org/
https://www.sqlite.org/cvstrac/wiki?p=UnsupportedSql
