# DDNSGoogle
Contenedor Docker para automatizar la actualizacion de DNS Dinámicos alojados de Google Domains


Para construir la imagen de Docker ejecutar:
      
        docker build -t ddnsgoogle .
        
# Uso

Crear un subdominio de DNS Dinamico segun las instruciones de Google Domain.

Ejecutar el contenedor:
      
        docker run -d -t -e usuario=******** -e passwd=******** -e dominio=xxx.xxx.xxx ddnsgoogle

