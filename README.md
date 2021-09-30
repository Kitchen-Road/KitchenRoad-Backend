# KitchenRoad-Backend

## Versão utilizada do Django será a 3.2.7

para instalar no ubuntu necessário ter python3 na máquina e colocar o seguinte comando.

```
pip install Django==3.2.7
```

### Baixando e rodando o projeto:

#### 1. Clone o repositório:

```
$ git clone https://github.com/Kitchen-Road/KitchenRoad-Backend.git
```

#### 2. Acesse o diretório do repositório:

```
$ cd kitch-road
```

#### 3. Crie um ambiente virtual e logo em seguida o ative:

```
$ python3 -m virtualenv venv
```

```
$ source venv/bin/activate
```

#### 4. O arquivo requirements.txt deve listar todas as bibliotecas que você vai precisar, você pode instalar todas elas com o comando:

```
(venv) $ pip install -r requirements.txt
```

#### 5. Em seguida, você deve fazer as migrações do banco de dados:

```
(venv) $ python3 manage.py makemigrations
```
```
(venv) $ python3 manage.py migrate
```


#### 7. Então, rode o servidor:

```
(venv) $ python3 manage.py runserver
```


Pronto! Agora o servidor deve estar rodando em: http://127.0.0.1:8000
