from app.utilis.generator import new_name
from app.negocio import name_exist
from app.negocio.backend import add_name

def main():
    i=0
    while i<4:
        name=new_name()
        i+=1
        if not name_exist(name):
            add_name(name)
            print(f'name is {name}')
            continue
        
main()