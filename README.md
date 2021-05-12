# API Rest para Sensores

Esta API permite o envio e recebimento de informações de oito sensores de temperatura e consumo espalhados pela casa. Estas informações ficam armazenadas em um arquivo csv e podem ser alteradas caso necessário.


## Criação de ambiente virtual

Para o exemplo será considerado o OS Windows

```sh
virtualenv env
./env/Scripts/activate
pip install -r requirements.txt
```


## Lista de Sensores

Foram considerados oito sensores, sendo eles quatro de temperatura e quatro de consumo

* Seus nome são:
	* TempQuarto1
	* TempQuarto2
	* TempSala
	* TempCozinha
	* ConsuQuarto1
	* ConsuQuarto2
	* ConsuSala
	* ConsuCozinha



## Lista de métodos

* Listar todos

Permite listar todos os sensores de Temperatura ou Consumo da seguinte forma:

```sh
/ListarTodos/Temperatura
/ListarTodos/Consumo
```

* Listar especifico

Permite listar um sensor específico a partir de seu id:

```sh
/ListarEspecifico/1
```

* Listar maior consumo

Permite listar o sensor de consumo com maior valor

```sh
/MaiorConsumo
```

* Mudar nome

Permite mudar o nome de um sensor a partir do id

```sh
/MudarNome/1
```

* Mudar nome

Permite mudar a disposição de um sensor a partir do id

```sh
/MudarDisposicao/1
```


## Armazenamento

* Os atributos armazenados de cada sensor são:
    * id (inteiro)
    * nome (string)
    * valor (float)
    * tipo (string)
    * disposicao (inteiro binario)

O correto seria armazenar essas informações em um banco de dados mas devido à simplisidade e à escala do problema optou-se por utilizar apenas um csv


## Trabalhos Futuros

* Adicionar Documentação Automática utilizando o Sphinx

* Adicionar testes unitários