class Persona:
    def __init__(self, id, nombre, password=None):
        self.id = id
        self.nombre = nombre
        self.password = password
        self.acceso_permitido = False

    def ingresar(self):
        codigo = input("Por favor ingrese su código: ")
        password = input("Por favor ingrese su contraseña: ")
        if self.id == codigo and self.password == password:
            print("Bienvenido", self.nombre)
            self.acceso_permitido = True
        else:
            print("Credenciales inválidas")



#------------------------------------------------------------------------------------------------------

class Paciente(Persona):
    def __init__(self, id, nombre, password):
        super().__init__(id, nombre, password)

    def acceder_perfil(self):
        self.ingresar()
        if self.acceso_permitido:
            print("Accediendo al perfil de Paciente:", self.nombre)
            pass
            




#------------------------------------------------------------------------------------------------------

class Medico(Persona):
    def __init__(self, id, nombre, password):
        super().__init__(id, nombre, password)

    def acceder_perfil(self):
        self.ingresar()
        if self.acceso_permitido:
            print("Accediendo al perfil de Médico:", self.nombre)
            pass

          

#------------------------------------------------------------------------------------------------------

class Enfermera(Persona):
    def __init__(self, id, nombre, password):
        super().__init__(id, nombre, password)

    def acceder_perfil(self):
        self.ingresar()
        if self.acceso_permitido:
            print("Accediendo al perfil de Enfermera:", self.nombre)
            pass

#------------------------------------------------------------------------------------------------------         



# Ejemplo de uso

paciente = Paciente("P01", "Juan", "123")
paciente.acceder_perfil()

medico = Medico("M01", "Dr. Ana", "123")
medico.acceder_perfil()

enfermera = Enfermera("E01", "María", "123")
enfermera.acceder_perfil()
