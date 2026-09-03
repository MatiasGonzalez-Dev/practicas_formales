#paso 1: verificacion de ubicacion actual

$pwd
/media/matiasdev/8E5D-D17B/practicas_formales/linux/practica_linux


#paso 2: creamos la estructura de carpetas 

$mkdir
mkdir -p practica_linux/{imagenes,documentos,scripts}

#paso 3: creacion de archivos vacios y reubicacion

$touch
$mv

touch foto.png documento.txt deploy.sh
mv foto.png practica_linux/imagenes
mv documento.txt practica_linux/documentos
mv deploy.sh practica_linux/scripts


#paso 4: busqueda de archivos .txt

$find

find -name "*.txt"

