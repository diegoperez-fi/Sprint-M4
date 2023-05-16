import random
#CLASE PADRE PERSONA
class Persona():
    def __init__(self, id, nombre, password):
        self.id = id
        self.nombre = nombre
        self.password = password

#-------------------------------------------------------------
#CLASE CLINICA
class Clinica:
    def __init__(self):
        self.pacientes = []
        self.enfermeras = []
        self.medicos = []

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def agregar_enfermera(self, enfermera):
        self.enfermeras.append(enfermera)

    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def asignar_enfermera_medico(self):
       
       for paciente in self.pacientes:
            if not paciente.enfermera_asignada:
                paciente.enfermera_asignada = random.choice(self.enfermeras)
            if not paciente.medico_asignado:
                paciente.medico_asignado = random.choice(self.medicos)

       for paciente in self.pacientes:
            print(f"Paciente: {paciente.nombre}")
            print(f"Enfermera asignada: {paciente.enfermera_asignada.nombre}")
            print(f"Médico asignado: {paciente.medico_asignado.nombre}")
    

    def llamar_enfermera(self):
        enfermera = random.choice(self.enfermeras)
        return enfermera.nombre
       
        
#-------------------------------------------------------------
#CLASE PACIENTE HEREDA DE PERSONA
class Paciente(Persona):
    def __init__(self, id, nombre, password, edad, enfermera_asignada=None, medico_asignado=None):
        super().__init__(id, nombre, password)
        self.edad = edad
        self.enfermera_asignada = enfermera_asignada
        self.medico_asignado = medico_asignado
       


#Funcion para ingresar a la cuenta, si las credenciales son correctas, entonces nos muestra un menu deopciones que podemos realizar
    def ingresar_paciente(self, clinica):
        codigo = input("Por favor ingrese su codigo: ")
        password = input("Por favor ingrese su contraseña: ")
        if self.id == codigo and self.password == password:
            print("Bienvenido, Paciente", self.nombre)
        else:
            print("Credenciales inválidas")
        opcion = ""
        while opcion != "0":
            print("Seleccione una opción:")
            print("1. Calificar servicio")
            print("2. Llamar enfermera")
            print("0. Salir")
            opcion = input("Ingrese su opcion: ")

            if opcion == "1":
                self.calificar_servicio()
            elif opcion == "2":
               # self.llamar_enfermera(clinica)
               #print(clinica.llamar_enfermera())
               print("Llamando a enfermera")
               enfermera_nombre = clinica.llamar_enfermera()
               print("Enfermera asignada: ", enfermera_nombre)
                     
            elif opcion == "0":
                print("Hasta luego")
                exit()
            else:
                print("Opción inválida")
                exit()

#Funcion para calificar servicio, si la calificacion es menor a 3, entonces nos pide comentarios para mejorar el servicio
    def calificar_servicio(self):
        calificacion = input("Por favor ingrese su calificacion del 1 al 5, siendo 1 muy malo y 5 muy bueno: ")
        if calificacion == "1":
            print("Lamentamos esta nota, por favor ingrese sus comentarios para mejorar nuestro servicio")
            comentarios = input("Ingrese sus comentarios: ")
            print("Gracias por sus comentarios, nos ayudara a mejorar")
        elif calificacion == "2":
            print("Lamentamos esta nota, por favor ingrese sus comentarios para mejorar nuestro servicio")          
            comentarios = input("Ingrese sus comentarios: ")
            print("Gracias por sus comentarios, nos ayudara a mejorar")
        elif calificacion == "3":
            print("Gracias por su calificacion, nos ayudara a mejorar")
        elif calificacion == "4":
            print("Gracias por su calificacion, nos ayudara a mejorar")
        elif calificacion == "5":
            print("Gracias por su calificacion, siempre es un placer atenderlo")
        else:
            print("Calificacion invalida, por favor ingresar numeros del 1 al 5")
        
#Funcion para llamar a enfermera        
    def llamar_enfermera(self, enfermera):
        if isinstance(enfermera, Enfermera):
            self.enfermera_asignada = enfermera
            print(f"ATENCION Enfermera {enfermera.nombre}: Esta siendo solicitada por el paciente: {self.nombre}")
        else:
            print("Error: El objeto no es de la clase Enfermera")



#-------------------------------------------------------------
#CLASE ENFERMERA HEREDA DE PERSONA
class Enfermera(Persona):
    def __init__(self, id, nombre, password):
        super().__init__(id, nombre, password)


#Funcion para ingresar a la cuenta, si las credenciales son correctas, entonces nos muestra un menu deopciones que podemos realizar
    def ingresar_enfermera(self, clinica):
        codigo = input("Por favor ingrese su codigo: ")
        password = input("Por favor ingrese su contraseña: ")
        if self.id == codigo and self.password == password:
            print("Bienvenido, Enfermera", self.nombre)
        else:
            print("Credenciales inválidas")

        opcion = ""
        while opcion != "0":
            print("Seleccione una opción:")
            print("1. Tomar signos vitales")
            print("2. Dar Medicamentos")
            print("0. Salir")
            opcion = input("Ingrese su opcion: ")

            if opcion == "1":
                self.tomar_signos_vitales(clinica.pacientes)
            elif opcion == "2":
                self.dar_medicamentos(clinica.pacientes)
            elif opcion == "0":
                print("Hasta luego")
                exit()
            else:
                print("Opción inválida")
                exit()
    

    def tomar_signos_vitales(self, pacientes):
        try:
            pac = input("Ingrese el id del paciente: ")
            presion = input("Ingrese la presion: ") 
            temperatura = input("Ingrese la temperatura: ")
            for paciente in pacientes:
                if pac == paciente.id:
                    print(f"La enfermera {self.nombre} ha registrado los signos vitales para el paciente {paciente.nombre}: {presion}, {temperatura}.")
                    return
        except IndexError: 
            print("Error al registrar signos vitales")


    def dar_medicamentos(self, pacientes):
        try:
            pac = input("Ingrese el id del paciente: ")
            medicamento = input("Ingrese el medicamento: ")
            word = input("Ingrese su contraseña: ")
            for paciente in pacientes:
                if word == self.password and pac == paciente.id:
                  print(f"La enfermera {self.nombre} ha dado el medicamento {medicamento} al paciente {paciente.nombre}.")
                  return
        except IndexError: 
            print("Error al dar medicamento")   
   

#-------------------------------------------------------------
#CLASE MEDICO HEREDA DE PERSONA
class Medico(Persona):
    def __init__(self, id, nombre, password):
        super().__init__(id, nombre, password)


#Funcion para ingresar a la cuenta, si las credenciales son correctas, entonces nos muestra un menu deopciones que podemos realizar
    def ingresar_medico(self, clinica):
        codigo = input("Por favor ingrese su codigo: ")
        password = input("Por favor ingrese su contraseña: ")
        if self.id == codigo and self.password == password:
            print("Bienvenido, Doctor", self.id)
        else:
            print("Credenciales inválidas")

        opcion = ""
        while opcion != "0":
            print("Seleccione una opción:")
            print("1. Dar Descanso")
            print("2. Dar de alta")
            print("0. Salir")
            opcion = input("Ingrese su opcion: ")

            if opcion == "1":
                self.dar_descanso(clinica.pacientes)
            elif opcion == "2":
                self.dar_alta(clinica.pacientes)
            elif opcion == "0":
                print("Hasta luego")
                exit()
            else:
                print("Opción inválida")


#Funcion para dar dias de descanso
    def dar_descanso(self, pacientes):
        try:
            pac = input("Ingrese el id del paciente: ")
            dias = input("Ingrese los dias de descanso: ")
            word = input("Ingrese su contraseña: ")
            for paciente in pacientes:
                if word == self.password and pac == paciente.id:
                    print(f"El doctor {self.nombre} ha dado {dias} dias de descanso al paciente {paciente.nombre}.")
                    return
                
        except IndexError: 
            print("Error al dar dias de descanso")


#Funcion para dar de alta a paciente
    def dar_alta(self, pacientes):
        try:
            pac = input("Ingrese el id del paciente: ")
            word = input("Ingrese su contraseña: ")
            for paciente in pacientes:
                if word == self.password and pac == paciente.id:
                     print(f"El doctor {self.nombre} ha dado de alta al paciente {paciente.nombre}.")
                     return
                
        except IndexError: 
            print("Error al dar de alta")













