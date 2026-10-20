from datetime import date
from conexion import SessionLocal
from models import Docente, Curso, Estudiante, Asistencia, EstadoAsistenciaEnum, Evaluacion, Nota

def cargar_datos_ejemplo():
    db = SessionLocal()

    try:
        # 1. Crear Docente de prueba (Joaquín Blanco)
        docente_joaquin = Docente(
            nombre="Joaquín",
            apellido="Blanco",
            email="joaquin.blanco@anotame.edu.ar"
        )
        db.add(docente_joaquin)
        db.commit()
        db.refresh(docente_joaquin)

        # 2. Crear Cursos de prueba
        curso_1 = Curso(
            nombre="3º Año A",
            materia="Matemática",
            ciclo_lectivo=2026,
            docente_id=docente_joaquin.id
        )
        curso_2 = Curso(
            nombre="2º Año B",
            materia="Física",
            ciclo_lectivo=2026,
            docente_id=docente_joaquin.id
        )
        db.add_all([curso_1, curso_2])
        db.commit()
        db.refresh(curso_1)
        db.refresh(curso_2)

        # 3. Crear Estudiantes de prueba para 3º Año A - Matemática
        estudiante_1 = Estudiante(
            nombre="Sofía",
            apellido="Gómez",
            avatar_url="https://ui-avatars.com/api/?name=Sofia+Gomez",
            curso_id=curso_1.id
        )
        estudiante_2 = Estudiante(
            nombre="Lucas",
            apellido="Rodríguez",
            avatar_url="https://ui-avatars.com/api/?name=Lucas+Rodriguez",
            curso_id=curso_1.id
        )
        estudiante_3 = Estudiante(
            nombre="Mateo",
            apellido="Fernández",
            avatar_url="https://ui-avatars.com/api/?name=Mateo+Fernandez",
            curso_id=curso_1.id
        )
        db.add_all([estudiante_1, estudiante_2, estudiante_3])
        db.commit()
        db.refresh(estudiante_1)
        db.refresh(estudiante_2)
        db.refresh(estudiante_3)

        # 4. Registrar Asistencias de prueba (Módulo 1) para la fecha de hoy
        hoy = date.today()
        asistencia_1 = Asistencia(
            fecha=hoy,
            estado=EstadoAsistenciaEnum.P, # Presente (Verde)
            justificacion=None,
            estudiante_id=estudiante_1.id,
            curso_id=curso_1.id
        )
        asistencia_2 = Asistencia(
            fecha=hoy,
            estado=EstadoAsistenciaEnum.A, # Ausente (Rojo)
            justificacion="Fiebre - Presentó certificado médico",
            estudiante_id=estudiante_2.id,
            curso_id=curso_1.id
        )
        asistencia_3 = Asistencia(
            fecha=hoy,
            estado=EstadoAsistenciaEnum.T, # Tardanza (Amarillo)
            justificacion="Llegó 15 min tarde por problemas de transporte",
            estudiante_id=estudiante_3.id,
            curso_id=curso_1.id
        )
        db.add_all([asistencia_1, asistencia_2, asistencia_3])

        # 5. Crear Evaluaciones (Módulo 2)
        parcial_1 = Evaluacion(
            nombre="Parcial 1",
            fecha=date(2026, 5, 10),
            curso_id=curso_1.id
        )
        parcial_2 = Evaluacion(
            nombre="Parcial 2",
            fecha=date(2026, 9, 15),
            curso_id=curso_1.id
        )
        tp_1 = Evaluacion(
            nombre="Trabajo Práctico",
            fecha=date(2026, 6, 20),
            curso_id=curso_1.id
        )
        db.add_all([parcial_1, parcial_2, tp_1])
        db.commit()
        db.refresh(parcial_1)
        db.refresh(parcial_2)
        db.refresh(tp_1)

        # 6. Cargar Calificaciones / Notas para cada estudiante
        notas = [
            # Notas de Sofía Gómez (Promedio alto)
            Nota(valor=9.0, estudiante_id=estudiante_1.id, evaluacion_id=parcial_1.id),
            Nota(valor=8.5, estudiante_id=estudiante_1.id, evaluacion_id=parcial_2.id),
            Nota(valor=10.0, estudiante_id=estudiante_1.id, evaluacion_id=tp_1.id),

            # Notas de Lucas Rodríguez
            Nota(valor=4.0, estudiante_id=estudiante_2.id, evaluacion_id=parcial_1.id),
            Nota(valor=5.5, estudiante_id=estudiante_2.id, evaluacion_id=parcial_2.id),
            Nota(valor=6.0, estudiante_id=estudiante_2.id, evaluacion_id=tp_1.id),

            # Notas de Mateo Fernández
            Nota(valor=7.0, estudiante_id=estudiante_3.id, evaluacion_id=parcial_1.id),
            Nota(valor=6.5, estudiante_id=estudiante_3.id, evaluacion_id=parcial_2.id),
            Nota(valor=8.0, estudiante_id=estudiante_3.id, evaluacion_id=tp_1.id),
        ]
        db.add_all(notas)
        db.commit()

        print("¡Datos de prueba insertados con éxito en todas las tablas!")

    except Exception as e:
        db.rollback()
        print(f"Error al insertar datos: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    cargar_datos_ejemplo()