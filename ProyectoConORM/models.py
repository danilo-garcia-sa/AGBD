import enum
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, Enum, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from conexion import Base, engine

# Definición de Estados de Asistencia (P: Presente, A: Ausente, T: Tardanza)
class EstadoAsistenciaEnum(str, enum.Enum):
    P = "P"  # Presente (Verde)
    A = "A"  # Ausente (Rojo)
    T = "T"  # Tardanza (Amarillo)

# 1. TABLA: Docentes
class Docente(Base):
    __tablename__ = 'docentes'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    
    # Relaciones
    cursos = relationship("Curso", back_populates="docente")


# 2. TABLA: Cursos / Materias
class Curso(Base):
    __tablename__ = 'cursos'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)  # Ej: "3º Año A"
    materia = Column(String(100), nullable=False) # Ej: "Matemática"
    ciclo_lectivo = Column(Integer, default=2026, nullable=False) # Ej: 2026
    docente_id = Column(Integer, ForeignKey('docentes.id'), nullable=False)

    # Relaciones
    docente = relationship("Docente", back_populates="cursos")
    estudiantes = relationship("Estudiante", back_populates="curso")
    asistencias = relationship("Asistencia", back_populates="curso")
    evaluaciones = relationship("Evaluacion", back_populates="curso")


# 3. TABLA: Estudiantes
class Estudiante(Base):
    __tablename__ = 'estudiantes'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    avatar_url = Column(String(255), nullable=True) # Para la foto de perfil/avatar
    curso_id = Column(Integer, ForeignKey('cursos.id'), nullable=False)

    # Relaciones
    curso = relationship("Curso", back_populates="estudiantes")
    asistencias = relationship("Asistencia", back_populates="estudiante")
    notas = relationship("Nota", back_populates="estudiante")


# 4. TABLA: Asistencias (Módulo 1)
class Asistencia(Base):
    __tablename__ = 'asistencias'

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, nullable=False) # Fecha de la toma de asistencia
    estado = Column(Enum(EstadoAsistenciaEnum), default=EstadoAsistenciaEnum.P, nullable=False)
    justificacion = Column(Text, nullable=True) # Campo para justificación de inasistencia/tardanza
    
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id'), nullable=False)
    curso_id = Column(Integer, ForeignKey('cursos.id'), nullable=False)

    # Relaciones
    estudiante = relationship("Estudiante", back_populates="asistencias")
    curso = relationship("Curso", back_populates="asistencias")


# 5. TABLA: Evaluaciones (Estructura para el Módulo 2)
class Evaluacion(Base):
    __tablename__ = 'evaluaciones'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False) # Ej: "Parcial 1", "Parcial 2", "Trabajo Práctico"
    fecha = Column(Date, nullable=True)
    curso_id = Column(Integer, ForeignKey('cursos.id'), nullable=False)

    # Relaciones
    curso = relationship("Curso", back_populates="evaluaciones")
    notas = relationship("Nota", back_populates="evaluacion")


# 6. TABLA: Notas / Calificaciones por Alumno
class Nota(Base):
    __tablename__ = 'notas'

    id = Column(Integer, primary_key=True, index=True)
    valor = Column(Float, nullable=False) # Ej: 8.5
    estudiante_id = Column(Integer, ForeignKey('estudiantes.id'), nullable=False)
    evaluacion_id = Column(Integer, ForeignKey('evaluaciones.id'), nullable=False)

    # Relaciones
    estudiante = relationship("Estudiante", back_populates="notas")
    evaluacion = relationship("Evaluacion", back_populates="notas")


# Script para crear todas las tablas automáticamente en MySQL
if __name__ == "__main__":
    print("Creando tablas en la base de datos 'Anotame-UBA'...")
    Base.metadata.create_all(bind=engine)
    print("¡Tablas creadas exitosamente!")