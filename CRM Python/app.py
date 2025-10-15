from backend import model_leads
import repo

def add_lead():
    name=input("Nome: ")
    company= input("Empresa: ")
    email = input("Email: ")

    repo.create_lead(model_leads(name, company, email))
    print("Lead adicionado")

def list_leads():
    leads= repo.read_leads()
    print(leads)
    if not leads:
        print("nenhum lead ainda.")
        return
    print(f"\n## | {"Nome":<20} | {"Empresa":<20} | {"email":<20}")
    for i,lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<20} | {lead["company"]} | {lead["email"]:<20}")

def search_leads():
    print("Buscando por leads...")
    user_search= input("Buscar por: ").strip().lower()
    if not user_search:
        print("Consulta vazia")
        return

    leads=repo.read_leads()
    results=[]

    for i, lead in enumerate(leads):
        lead_str=f"{lead["name"]} {lead["company"]} {lead["email"]}".lower()
        if user_search in lead_str:
            results.append(lead)

    if not results:
        print("Não foi encontrado!")
        return

    print(f"\n## | {"Nome":<20} | {"Empresa":<20} | {"email":<20}")
    for i,lead in enumerate(results):
        print(f"{i:02d} | {lead["name"]:<20} | {lead["company"]} | {lead["email"]:<20}")

def export_leads():

    path_csv =repo.export_csv()
    if path_csv is None:
        print("Não foi possível exportar os leads.")
    else: print(f"Leads exportados como CSV para: {path_csv}")

def main():
    while True:
        print_menu()
        op= input("Escolha: ")
        if op == "1":
            print("Lead adicionado")
            add_lead()
        elif op == "2":
            print("Listar Leads")
            list_leads()
        elif op == "3":
            search_leads()
        elif op == "4":
            export_leads()
        elif op == "0":
            print("Até mais")
            break
        else:
            print("Opção invalida")

def print_menu():
    print("\n Mini CRM de Leads - (Adicionar/Listar)")
    print("[1] Adicionar Lead")
    print("[2] Listar Leads")
    print("[3] Buscar leads por:")
    print("[4] Exportar leads como CSV")
    print("[0] Sair do programa")


if __name__ == '__main__':
    main()