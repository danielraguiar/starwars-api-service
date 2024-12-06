# Star Wars API Service

Star Wars API Service é um serviço REST que fornece dados sobre planetas e filmes do universo Star Wars.

## Tecnologias Utilizadas

- Python 3.8+
- Flask (Framework Web)
- MongoDB (Banco de Dados)
- PyTest (Testes)

## Estrutura do Projeto

```
holocron-api/
├── app.py
├── config.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── models/
│   ├── __init__.py
│   ├── planet.py
│   └── film.py
├── routes/
│   ├── __init__.py
│   ├── planets.py
│   └── films.py
└── tests/
    ├── __init__.py
    ├── test_planets.py
    └── test_films.py
```

## Configuração do Ambiente

### Pré-requisitos

- Python 3.8 ou superior
- MongoDB 4.4 ou superior

### Instalação Local

1. Clone o repositório:
```bash
git clone https://github.com/your-username/starwars-api-service.git
cd starwars-api-service
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas configurações:
```
MONGO_URI=mongodb://localhost:27017/starwars
FLASK_ENV=development
FLASK_APP=app.py
```

## Executando o Projeto

### Localmente

1. Inicie o MongoDB:
```bash
mongod
```

2. Execute a aplicação:
```bash
flask run
```

A API estará disponível em `http://localhost:5000`


## Endpoints da API

### Planetas

- `GET /planets` - Lista todos os planetas
- `GET /planets/<id>` - Obtém um planeta específico
- `POST /planets` - Cria um novo planeta
- `PUT /planets/<id>` - Atualiza um planeta
- `DELETE /planets/<id>` - Remove um planeta

Exemplo de payload para criar/atualizar planeta:
```json
{
    "name": "Tatooine",
    "climate": "Arid",
    "diameter": "10465",
    "population": "120000",
    "films": ["1", "2"]
}
```

### Filmes

- `GET /films` - Lista todos os filmes
- `GET /films/<id>` - Obtém um filme específico
- `POST /films` - Cria um novo filme
- `PUT /films/<id>` - Atualiza um filme
- `DELETE /films/<id>` - Remove um filme

Exemplo de payload para criar/atualizar filme:
```json
{
    "title": "A New Hope",
    "release_date": "1977-05-25",
    "director": "George Lucas",
    "planets": ["1", "2", "3"]
}
```

## Testes

Execute os testes com:
```bash
pytest
```

Para testes com cobertura:
```bash
pytest --cov=. tests/
```
