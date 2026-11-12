name = []
lastName = []
age = []
birthday = []
email = []
password = []
confirmPass = []
opcion = []


print("Bienvenido al sistema de registro de usuarios")
print("---------MENU PRINCIPAL---------")
print("1. Registrar usuario")
print("2. Ver informacion del usuario")
print("3. Borrar informacion del usuario")
print ("4. Modificar informacion del usuario")
print("5. Salir")
print("---------------------------------")
opcion = int(input("Selecciona una opcion: "))

match opcion:#Aqui inicia el match, que es una validacion de caso

    case 1:
        name.append(input("Ingresa tu nombre: "))
        lastName.append(input("Ingresa tu apellido: "))
        age.append(int(input("Ingresa tu edad; ")))
        birthday.append(input("Ingresa tu fecha de nacimiento: "))
        email.append(input("Ingresa tu correo electronico: "))
        password.append(input("Ingresa tu contrasena: "))
        confirmPass.append(input("Confirma tu contrasena: "))
    case 2: 
        print("Nombre:", name, "Edad:", age, "Fecha de nacimiento:", birthday, "Correo electronico:", email, "Contrasena:", password)
    case 3:
        name = []
        lastName = []
        age = ¨[]
        birthday = []
        email = []
        password = []
    case 4:
        name.append(input("Ingresa tu nombre: "))
        lastName.append(input("Ingresa tu apellido: "))
        age.append(int(input("Ingresa tu edad: ")))
        birthday.append(input("Ingresa tu fecha de nacimiento: "))
        email.append(input("Ingresa tu correo electronico: "))
        password.append(input("Ingresa tu contrasena: "))
    case 5:
        print("¡Hasta luego!")
    case _:
        print("Opcion no valida")