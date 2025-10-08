from backend import model_leads
import repo

def add_lead():
    name=input("Nome: ")
    company= input("Empresa: ")
    email = input("Email: ")

    repo.create_lead(model_leads(name, company, email))
    print("Lead adicionado")

def list_leads():
    print("Listar leads")


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
        elif op == "0":
            print("Até mais")
            break
        else:
            print("Opção invalida")

def print_menu():
    print("\n Mini CRM de Leads - (Adicionar/Listar)")
    print("[1] Adicionar Lead")
    print("[2] Listar Leads")
    print("[0] Sair do programa")


if __name__ == '__main__':
    main()