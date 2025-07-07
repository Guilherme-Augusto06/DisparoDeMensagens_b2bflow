# Disparo de mensagens B2BFLOW

## ✅ Requisitos

- Python **3.x**
- `flask`
- `supabase`
- `requests`

---

## 🧰 Instalação das dependências

> As instruções abaixo funcionam tanto para **Windows** quanto para **Linux**.

### 1. Crie um ambiente virtual (opcional, mas recomendado)

#### Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

#### Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 2. Instale as dependências

Com o ambiente virtual ativado, execute:

```bash
pip install requests supabase flask
```

---

## ▶️ Como executar o script

Após instalar as dependências, execute:

### No Windows:

```powershell
python app.py
```

### No Linux:

```bash
python3 app.py
```

---

## 🧪 Funcionamento do script

Quando você executa o script com python app.py, o Flask inicia um servidor local de desenvolvimento.
Exemplo de saída no terminal:

```text
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 606-226-436
```

### ✅ Como usar:
Após ver essa mensagem, abra seu navegador e acesse:
```
http://127.0.0.1:5000
```
Você verá a interface da aplicação com um botão para disparar mensagens.
---
