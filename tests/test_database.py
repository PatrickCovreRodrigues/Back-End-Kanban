import psycopg2

try:
    conn = psycopg2.connect("postgresql+psycopg2://app_user:app_password@172.26.13.184:5432/app_db")
    print("Conexão bem-sucedida!")
    conn.close()
except Exception as e:
    print(f"Erro ao conectar: {e}")
