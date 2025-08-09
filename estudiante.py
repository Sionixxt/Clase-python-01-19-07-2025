class Estudiante:
    def __init__(self, nombre, apellido, cedula, fechaNacimiento, grupo, calificaciones):
        self._nombre = nombre 
        self._apellido=apellido
        self._fechaNacimiento=fechaNacimiento
        self._cedula=cedula
        self._grupo=grupo
        self._calificaciones = calificaciones

    def calcular_promedio(self):
        if not self._calificaciones:
            return 0
        return sum(self._calificaciones) / len(self._calificaciones)
    
    def mostrar_info(self):
        print(f"Nombre: {self._nombre} {self._apellido}")
        print(f"Calificaciones: {self._calificaciones}")
        print(f"Promedio: {self.calcular_promedio():.2f}")
    
    
    def AgregarEstudiante(self):
        with open("Estudiantes.txt", "a") as f:
            f.write(f"{self._nombre},{self._apellido},{self._cedula},{self._fechaNacimiento},{self._grupo},{self._calificaciones}, Promedio: {self.calcular_promedio():.2f}\n")
    
    def EliminarEstudiante(cedula):
        estudiantes=[]
        with open("Estudiantes.txt", "r") as f:
            for linea in f:
                if cedula not in linea:
                    estudiantes.append(linea)
                else:
                    print(f"El estudiante ha sido eliminado")
        with open("Estudiantes.txt", "w") as f:
            f.writelines(estudiantes)
    
    def BuscarEstudiante(cedula):
        with open("Estudiantes.txt", "r") as f:
            for linea in f:
                if cedula in linea:
                    return linea
    
    def Listar(self):
        with open("Estudiantes.txt", "r") as f:
            for linea in f:
                print(linea)

if __name__ == "__main__":
    est = Estudiante("Ana", "Pérez", "12345678", "01/01/2000", "A", [18.5, 19.0, 20.0])
    est.AgregarEstudiante()


    