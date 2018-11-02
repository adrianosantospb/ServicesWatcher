#  Services Watch
### Por Adriano Santos

## Informações

O ServicesWatch foi desenvolvido para ajudar no processo de deployment automático dos serviços. Sua arquitetura é genérica e foi pensada de forma a se integrar com o Jenkins ou com qualquer ferramenta de deployment automático. Eu o criei para que ele verificasse se determinado serviço estava em funcionamento em uma máquina e que decisões pudessem ser realizados. Ex: instalação do serviço, deployment de novas versão, tentativas de reiniciar o serviço etc.

## Funcionamento básico

O ServicesWatch possui um arquivo de configuração (settings.json) composto por três chaves: Names (nome da máquina), Processess (nome do processo a ser verificado) e Files (arquivo que contém os procedimentos a serem executados caso o serviço não esteja em funcionamento).
O Jenkins (ou você mesmo) executará o GASIS-SW chamando o arquivo de execução *main.py* com o parâmetro -m (máquina), seguindo do nome da máquina. Ex:

```python
main.py -m Servidor
```

O nome utilizado como parâmetro deve ser reconhecido pelo arquivo de configuração. O ServicesWatch foi configurado para procurar um arquivo correspondente na pasta **scripts**. 

Ex: Se você possui uma máquina chamada de Skywalker e nela, um serviço chamado StarWars. Você também preparou um script que contém um conjunto de operações, tais como: baixar o projeto de um repositório do git, executar comando de instalação de pacotes, e iniciar o serviço, etc. ele deve ser inserido na pasta **scripts**.
No arquivo **settings.json**, você irá configurar da seguinte forma:

```json
Machines": { 
            "Names": ["Skywalker"], 
            "Processes": ["StarWars""],
            "Files" : ["skywalker.py""]
        },
```
Para chamar o serviço ServicesWatch, faça:

```python
main.py -m Skywalker
```

## Tecnologias

python 3.7
dynaconf - https://dynaconf.readthedocs.io
getopt - https://www.gnu.org/software/libc/manual/html_node/Getopt.html
psutil - https://pypi.org/project/psutil/
