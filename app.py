from flask import Flask, render_template
from supabase import create_client, Client
import requests

app = Flask(__name__)

# Dados Supabase
url = "https://bfqeidvekcwpwpasdhht.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcWVpZHZla2N3cHdwYXNkaGh0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTE5MTI1NzQsImV4cCI6MjA2NzQ4ODU3NH0.OLPzyvJ-t0AC-Qsv-Dzm_ls_qPdvlUZmMg8AqnuNkfI"
supabase: Client = create_client(url, key)


# Dados da Z-API
ZAPI_INSTANCE_ID = "3E3D8E3704C3102130118AA94DBE6FD7"
ZAPI_TOKEN = "A2BD83992F9FA6034A2F7344"

ZAPI_URL = "https://api.z-api.io/instances/3E3D8E3704C3102130118AA94DBE6FD7/token/A2BD83992F9FA6034A2F7344/send-text"

headers = {
    "Content-Type": "application/json",
    "Client-Token": "Fa4835697a5b540bcaa9c94a0413b5117S"
}


# Link do repositório
linkRepo = "https://github.com/Guilherme-Augusto06/DisparoDeMensagens_b2bflow.git"

@app.route('/disparar', methods=['GET'])
def dispararMensagens():
    global linkRepo
    response = supabase.table('TelNumbers').select('*').limit(5).execute() # Obtem os 5 contatos salvos
    contacts = [(item['name'], item['numbers']) for item in response.data] # Extrai os nomes e os numeros

    for name, number in contacts: # Percorre os contatos que no caso são seus nomes e numeros
        payload = {
            "phone": number, 
            "message": f"Olá {name}, tudo bem? \nMeu nome é Guilherme, e quero fazer parte da b2bfow. \nEsse é meu disparo de mensagem para o teste. \nDeixarei o código utilizado no seguinte repositório do GitHub \nLink repositório: {linkRepo} \nEstou a disposição",
        } 
        responseAPI = requests.post(ZAPI_URL, json=payload, headers=headers) # Envia a mensagem via Z-API
        print(f"Envio para {number} - Status: {responseAPI.status_code}, Resposta: {responseAPI.text}") # Imprime no console
    return "Mensagens enviadas com sucesso!"
    
@app.route('/') # Rota para a página inicial
def home():
    return render_template('homepage.html') # Renderiza o template HTML da página inicial



if __name__ == '__main__':
    app.run(debug=True)
