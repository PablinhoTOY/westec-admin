from app import db, app

from sqlalchemy import insert

from app.Models.Users import User, Permisos, Role, role_permission, roles_users
from app.Models.Grupo import Grupo

def seed_db():

    grupos_to_insert = [Grupo(nombre='Campus Central Victor Levi Sasso', codigo='01'),
                       Grupo(nombre='Centro Regional de Chiriqui', codigo='02'),
                       Grupo(nombre='Centro Regional de Veraguas', codigo='04'),
                       Grupo(nombre='Centro Regional de Colon', codigo='05'),
                       Grupo(nombre='Centro Regional de Cocle', codigo='06'),
                       Grupo(nombre='Centro Regional de Azuero', codigo='07'),
                       Grupo(nombre='Centro Regional de Bocas del Toro', codigo='08'),
                       Grupo(nombre='Centro Regional de Panama Oeste', codigo='09'),
                       Grupo(nombre='Facultad de Ingenieria Civil', codigo='11'),
                       Grupo(nombre='Facultad de Ingenieria Electrica', codigo='12'),
                       Grupo(nombre='Facultad de Ingenieria Industrial', codigo='13'),
                       Grupo(nombre='Facultad de Ingenieria Mecanica', codigo='14'),
                       Grupo(nombre='Facultad de Ingenieria Sistemas Computacionales', codigo='15'),
                       Grupo(nombre='Facultad de Ciencias y Tecnologia', codigo='16'),
                       ]
    
    permisos_to_insert = [Permisos(nombre="Administrar Usuarios", categoria='Administración', key='OIRAM23'),
                        Permisos(nombre="Administrar Permisos", categoria='Administración', key='HCAEP32'),
                        Permisos(nombre="Administrar Roles", categoria='Administración', key='DAOT54'),
                        Permisos(nombre="Administrar Grupos", categoria='Administración', key='RESWOB66'),
                        Permisos(nombre="Roles y Permisos", categoria='Administración', key='KWAS935'),
                        Permisos(nombre="Dashboard", categoria='Administración', key='KABRA292'),
    ]

    roles_to_insert = [Role(name="Administrador")]
    
    #Reemplazar correo por uno que tenga acceso. De lo contrario, no podrá iniciar sesión.                    
    user_to_insert = [User(email="franklin.quintero1@utp.ac.pa",
                    
                    nombre="franklin", apellido="quintero", active=1, grupo_id=1,fs_uniquifier="8@uQHvRniq5TDQ67ung&bXL38d3M5NerLfxoH@X!", roles=[roles_to_insert[0]])
                    
                    ]

   
        
    db.session.bulk_save_objects(grupos_to_insert)
    db.session.bulk_save_objects(permisos_to_insert)
    db.session.bulk_save_objects(roles_to_insert)
    db.session.bulk_save_objects(user_to_insert)



    # db.session.commit()
        
        
    #stmt1 = (insert(role_permission).values(role_id='1', permission_id=['1']))
    stmt2 = (insert(roles_users).values(usuario_id='1', role_id='1'))
   #db.session.execute(stmt1)
    db.session.execute(stmt2)
    db.session.commit()
    permisos = ['0', '1', '2', '3', '4', '5', '6']
    role = Role.query.filter_by(id=1).first()
    for i in permisos:
        permiso = Permisos.query.filter_by(id=i).first()
        if permiso != None:
            role.permisos.append(permiso)
    db.session.commit()
    
