from datetime import date

STAGES = ["novo"]# por enquanto só marcamos como "novo"

def model_leads(name, company, email):
    """ Modelar/ estruturar um lead como um dicionario simples"""
    return{
        "name" : name,
        "company" : company,
        "email" : email,
        "stage" : "novo",
        "created" : date.today().isoformat()
    }