from setuptools import setup

setup(

    name="paquetecalculos",
    version="1.0",
    description="Paquete de redondeo y potencia",
    author="Gabriel",
    author_email="gabo0423@hotmail.com",
    url="www........",
    packages=["calculos","calculos.redondeo_potencia"]

)

# Para hacer un paquete para instalar se debe escribir 
# el path, la dirección de donde esta el setup
# Mypath\ python setup.py sdist y así se crea el paquete distribuible
# Para instalarlo debemos estar en el directorio del dist y colocar en la consola
# pip3 install & nombre del paquete junto a su extensión &

# para desintalar se usa pip3 uninstall & nombre del paquete sin extensión &