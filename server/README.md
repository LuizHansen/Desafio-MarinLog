# Desafio MarinLog - Processador de Arquivo CNAB

## 📌 Sobre o Projeto
Este projeto processa arquivos **CNAB** e exibe as transações de forma organizada. Ele permite:
- **Upload de arquivos CNAB** via frontend.
- **Processamento e armazenamento das transações** em um banco de dados.
- **Consulta das transações** através de uma API.
- **Exibição das operações** no frontend, incluindo o saldo total.

## 🛠️ Tecnologias Utilizadas
- **Backend**: Python, FastAPI, SQLAlchemy, PyMSSQL
- **Banco de Dados**: SQL Server
- **Frontend**: HTML, CSS, JavaScript

---

## 🚀 Setup do Projeto

### 🔹 1. Clonar o Repositório
```sh
git clone https://github.com/LuizHansen/Desafio-MarinLog.git
cd Desafio-MarinLog
```

### 🔹 2. Configurar o Ambiente Virtual
```sh
python -m venv venv
venv\Scripts\activate
```

### 🔹 3. Instalar Dependências
```sh
pip install -r requirements.txt
```

### 🔹 4. Configurar o Banco de Dados
Crie um banco no **SQL Server** e defina as variáveis no arquivo `.env`:
```ini
DB_USER=seu_usuario
DB_PASS=sua_senha
DB_HOST=127.0.0.1
DB_NAME=MarinLog
```

### 🔹 5. Rodar as Migrações (se aplicável)
```sh
alembic upgrade head
```

### 🔹 6. Iniciar a API
```sh
uvicorn server.main:app --reload
```

---

## 🌍 Como Consumir a API
### 🔹 **Enviar um Arquivo CNAB** (`POST /cnab/enviar_cnab`)
```sh
curl -X POST "http://127.0.0.1:8000/cnab/enviar_cnab" -F "file=@caminho/do/arquivo.txt"
```
📌 **Retorno esperado:**
```json
{"message": "Arquivo processado com sucesso!"}
```

### 🔹 **Consultar Transações** (`GET /cnab/consultar_cnab`)
```sh
curl -X GET "http://127.0.0.1:8000/cnab/consultar_cnab"
```
📌 **Retorno esperado:**
```json
[
  {"tipo_transacao": "Débito", "valor": 100.0, "cpf": "12345678901", "nome_da_loja": "Supermercado"},
  ...
]
```

---

## 🎨 Executar o Frontend
1️⃣ Navegue até a pasta do frontend:
```sh
cd client
```
2️⃣ Rode um servidor local para abrir `index.html`:
```sh
python -m http.server 8000
```
3️⃣ Acesse: [http://127.0.0.1:8000](http://127.0.0.1:8000)
## 🔗 Links do Projeto
- **Frontend Online**: [https://desafio-marin-log.vercel.app](https://desafio-marin-log.vercel.app)
- **Repositório GitHub**: [https://github.com/LuizHansen/Desafio-MarinLog](https://github.com/LuizHansen/Desafio-MarinLog)

---

🚀 **Feito por [Luiz Henrique Hansen]**
