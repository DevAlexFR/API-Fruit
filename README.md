
# Apple Fruit API 🍎
Uma API desenvolvida com **FastAPI** para gerenciar frutas. Esta API oferece rotas para criar, listar, atualizar e deletar frutas de forma simples e eficiente.

---

## 📋 **Descrição**
A API "Apple Fruit" permite a interação com um banco de dados fictício de frutas. Com uma interface intuitiva, é possível realizar operações de CRUD (Create, Read, Update, Delete) em frutas, além de ter acesso a uma interface gráfica para documentação gerada automaticamente pelo FastAPI.

---

## 🚀 **Funcionalidades**
- **Rota principal**: Página inicial HTML com informações básicas sobre a API.
- **Criação de frutas**: Adicione novas frutas ao banco de dados.
- **Listagem de frutas**: Obtenha todas as frutas cadastradas.
- **Atualização de frutas**: Atualize informações de frutas existentes.
- **Deleção de frutas**: Remova frutas cadastradas.
- **Documentação interativa**: Acesse as rotas via `/docs` ([Swagger UI](https://crud-fruit.fly.dev/)) ou `/redoc`.

---

## 📜 **Rotas Disponíveis**
### **1. Página Inicial**
- **`GET /`**
  - Exibe uma página HTML com informações sobre a API e links para a documentação.

### **2. Criar Fruta**
- **`POST /fruit/`**
  - Cria uma nova fruta.
  - **Request Body**: Informações da fruta (exemplo abaixo).
  - **Response**: A fruta criada.

### **3. Listar Frutas**
- **`GET /fruits/`**
  - Retorna uma lista com todas as frutas cadastradas.
  - **Response**: Lista de frutas.

### **4. Atualizar Fruta**
- **`PUT /fruits/{fruit_id}`**
  - Atualiza as informações de uma fruta específica.
  - **Request Body**: Informações atualizadas da fruta.
  - **Response**: A fruta atualizada ou erro caso não exista.

### **5. Deletar Fruta**
- **`DELETE /fruits/{fruit_id}`**
  - Remove uma fruta pelo ID.
  - **Response**: Mensagem de sucesso ou erro.

---

## 🛠️ **Tecnologias Utilizadas**
- **Python**: Linguagem principal do projeto.
- **FastAPI**: Framework para construção de APIs rápidas e intuitivas.
- **Uvicorn**: Servidor ASGI para execução da aplicação.

---

## 🗂️ **Estrutura do Projeto**
```
apple_fruit_api/
│
├── project/
│   └── data/
│       ├── crud.py       # Operações CRUD para frutas
│       └── models.py     # Modelos de dados para frutas
├── main.py               # Arquivo principal da aplicação
└── README.md             # Documentação do projeto
```

---

## 📜 **Como Usar**
### **1. Clone o Repositório**
```bash
git clone https://github.com/SeuUsuario/SeuRepositorio.git
cd apple_fruit_api
```

### **2. Crie um Ambiente Virtual**
```bash
# Para Linux/MacOS
python3 -m venv .venv
source .venv/bin/activate

# Para Windows
python -m venv .venv
.venv\Scripts\activate
```

### **3. Instale as Dependências**
```bash
pip install -r requirements.txt
```

### **4. Execute o Servidor**
```bash
uvicorn main:app --reload
```

### **5. Acesse a API**
https://crud-fruit.fly.dev/
- Documentação Swagger: https://crud-fruit.fly.dev/docs
- Documentação Redoc: https://crud-fruit.fly.dev/redoc

---

## ✨ **Exemplo de Uso**
### **Criar uma Fruta (POST /fruit/)**
Request Body:
```json
{
  "name": "Maçã",
  "color": "Vermelha",
  "price": 1.5
}
```
Response:
```json
{
  "id": 1,
  "name": "Maçã",
  "color": "Vermelha",
  "price": 1.5
}
```

---

## ✨ **Contribuição**
Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar problemas no repositório.
