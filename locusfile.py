from locust import HttpUser, task, between
import csv
import os

# Caminho dos arquivos CSV
INPUT_CSV = "users.csv"
SUCCESS_CSV = "successful_logins.csv"
FAILED_CSV = "failed_logins.csv"

# Função para ler usuários do CSV
def read_users_from_csv():
    users = []
    with open(INPUT_CSV, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    return users

# Função para escrever resultados em CSV
def write_to_csv(filename, data):
    file_exists = os.path.isfile(filename)
    with open(filename, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        # Lê os usuários do CSV
        self.users = read_users_from_csv()
        self.current_user = None

    @task
    def login(self):
        if not self.users:
            self.stop(True)  # Para o usuário virtual se não houver mais usuários para testar
            return

        # Seleciona o próximo usuário da lista
        self.current_user = self.users.pop(0)
        email = self.current_user["email"]
        password = self.current_user["password"]

        # Simula o login
        response = self.client.post(
            "", #Adicione seu endpoint de login aqui
            json={
                "email": email,
                "password": password,
                "returnSecureToken": True
            }
        )

        # Verifica se o login foi bem-sucedido
        if response.status_code == 200:
            print(f"Login bem-sucedido para {email}!")
            write_to_csv(SUCCESS_CSV, {"email": email, "password": password})
        else:
            # Captura o erro retornado pelo Firebase ou qualquer outro DB que você esteja usando
            error_message = response.json().get("error", {}).get("message", "Erro desconhecido")
            print(f"Falha no login para {email}: {error_message}")
            write_to_csv(FAILED_CSV, {"email": email, "password": password, "error": error_message})

    @task
    def visit_homepage(self):
        if self.current_user:
            self.client.get("/")