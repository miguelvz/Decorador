import requests as req

def consulta_frontera(function): # consulta fronteras de países en Suramérica
    def wrapper(pais):
        response = req.get(f"https://restcountries.eu/rest/v2/alpha/{pais}")
        
        if response.status_code == 200:
            diccionario = eval(response.content) # De str a dict
            
            if diccionario["subregion"] == "South America":
                return f"{diccionario['name']} tiene frontera con: {diccionario['borders']}"
            else:
                return function()

        elif response.status_code == 404:
            return "Esas siglas de país no existen!"
        else:
            return "Ocurrió un error :("
    return wrapper

        