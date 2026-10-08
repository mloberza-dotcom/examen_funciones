import subprocess
subprocess.run("cls",shell=True)
def validador(lista):
    for i in range (len(lista)):
        if lista[1]>=2010:
            edad=True
        else:
            edad=False
        if lista[2]>=180:
            altu=True
        else:
            altu=False
    final=[edad,altu]
    return(final)