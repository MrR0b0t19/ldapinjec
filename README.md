
# LDAP Injection 

## Descripción
Este script permite la identificación y explotación de vulnerabilidades de inyección LDAP en aplicaciones web que interactúan con directorios LDAP de manera insegura. Se desarrolló basándose en técnicas documentadas en **HackTricks** y fue probado en entornos controlados, incluyendo máquinas vulnerables y un proyecto de auditoría de seguridad.

## Características
- Identificación de atributos expuestos en consultas LDAP.
- Detección de atributos vulnerables a ataques de fuerza bruta.
- Extracción de datos sensibles mediante técnicas de bypass con comodines (`*`).

## Instalación y Uso
### Requisitos
- Python 3.x
- Librerías necesarias:

  pip install requests termcolor


### Ejecución
1. Clonar el repositorio:

   git clone https://github.com/tuusuario/ldap-injection-tool.git
   cd ldap-injection-tool

2. Ejecutar el script:

   python3 ldap.py

3. Ingresar la URL objetivo cuando el script lo solicite.

## Ejemplo de Uso

Ingresa la URL objetivo (ejemplo: http://target.com/users/list.php?name=*) : http://vulnerable.site/list.php?name=*)

El script intentará enumerar atributos y detectar aquellos vulnerables a inyección LDAP.

## Referencias
- [HackTricks - LDAP Injection](https://book.hacktricks.xyz/pentesting/pentesting-ldap)

## Advertencia
Este script debe usarse exclusivamente para **fines educativos y pruebas en entornos autorizados**. El uso indebido de esta herramienta en sistemas sin permiso explícito puede ser ilegal y tener consecuencias legales.



