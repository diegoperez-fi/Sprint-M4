from Clinica import *
import json

clinica = Clinica()

# Agregar pacientes, enfermeras y médicos
paciente1 = Paciente("1", "John Doe", "password", 30)
paciente2 = Paciente("2", "Jane Smith", "password", 25)
enfermera1 = Enfermera("10", "Emily Johnson", "password")
enfermera2 = Enfermera("11", "Michael Brown", "password")
medico1 = Medico("20", "Dr. Sarah Davis", "password")
medico2 = Medico("21", "Dr. Christopher Wilson", "password")



# Agregar a la clase clinica
clinica.agregar_paciente(paciente1)
clinica.agregar_paciente(paciente2)
clinica.agregar_enfermera(enfermera1)
clinica.agregar_enfermera(enfermera2)
clinica.agregar_medico(medico1)
clinica.agregar_medico(medico2)




# Asignar enfermeras y médicos aleatoriamente a los pacientes
clinica.asignar_enfermera_medico()

#-------------------------------------------------------------



# INICIO DEL PROGRAMA, ELEGIR UN PERFIL.
print("Seleccione un perfil:")
print("1. Paciente")
print("2. Medico")
print("3. Enfermera")

opcion = input("Ingrese su opción: ")

if opcion == "1":
    print("Ha escogido perfil: Pacientes")
    paciente_id = input("Ingrese el ID del paciente: ")
    paciente_valido = False

    for paciente in clinica.pacientes:
        if paciente.id == paciente_id:
            print(f"Paciente: {paciente.nombre}")
            paciente.ingresar_paciente(clinica)
            break

    if not paciente_valido:
        print("ID o contraseña incorrectos")




elif opcion == "2":
    print("Ha escogido perfil: Médicos")
    medico_id = input("Ingrese el ID del médico: ")
    medico_valido = False

    for medico in clinica.medicos:
        if medico.id == medico_id:
            print(f"Médico: {medico.nombre}")
            medico.ingresar_medico(clinica)
            medico_valido = True
            break

    if not medico_valido:
        print("ID o contraseña incorrectos")





elif opcion == "3":
    print("Ha escogido perfil: Enfermeras")
    enfermera_id = input("Ingrese el ID de la enfermera: ")
    enfermera_valido = False

    for enfermera in clinica.enfermeras:
        if enfermera.id == enfermera_id:
            print(f"Enfermera: {enfermera.nombre}")
            enfermera.ingresar_enfermera(clinica)
            enfermera_valido = True
            break

    if not enfermera_valido:
        print("ID o contraseña incorrectos")


else:
    print("Opción inválida")

#-------------------------------------------------------------

perfiles_pacientes = []
for paciente in clinica.pacientes:
    perfil = {
        "id": paciente.id,
        "nombre": paciente.nombre,
        "password": paciente.password,
        "edad": paciente.edad,
        "enfermera": paciente.enfermera.nombre,
        "medico": paciente.medico.nombre,
    }

    perfiles_pacientes.append(perfil)

with open("Perfiles_pacientes.json", "w") as archivo:
    json.dump(perfiles_pacientes, archivo)


with open("perfiles_pacientes.json", "r") as archivo:
    perfiles_guardados = json.load(archivo)

# Imprime los perfiles guardados para verificar
print("Perfiles de pacientes guardados:")
for perfil in perfiles_guardados:
    print(perfil)
    