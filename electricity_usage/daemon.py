import json

def read_params(filename):
    with open(filename, 'r') as file:
        params = json.load(file)
    return params

if __name__ == "__main__":
    params = read_params('datatransfer.json')
    print("Gelesene Parameter:", params)
    
    #zugriff auf einzelne Parameter
    area = params['area']
    print("area:", area)