import clipboard
import sys
import json

SAVED_DATA = "clipboard.json"

def save_data(filepath,data):
    with open(filepath, "w") as f:
        json.dump(data,f)

def load_data(filepath):
    try:
    #Eu uso try quando não tenho certeza se certa parte do meu código vai funcionar
        with open(filepath,"r") as f:
            data = json.load(f)
            return data
    except:
        return {}
        #Se meu try der erro, aí o código vem para o except
        #Aqui o código está dizendo que se try não funcionar é para retornar um dicionário vazio

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA,data)
        print("data saved!")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("Key does not exist!")
    elif command == "list":
        print(data)
    else:
        print("Unknown command")

else:
    print("Please pass exactly one command.")




