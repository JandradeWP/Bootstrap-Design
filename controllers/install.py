# coding: utf8
# try something like
def index(): 

    ### Creamos los niveles de usaurios
    auth.add_group('admin', 'Administrador del sistema')
    auth.add_group('gerente', 'Gerente del sistema')
    auth.add_group('mayorista', 'Agencia mayoristas')
    auth.add_group('minorista', 'Agencia minorista')
    auth.add_group('agente', 'Agente de ventas')

    ### Creamos un usuario administrador
    ### admin@localhost : hello
    import users

    id = users.create(db, 
            first_name='Admin',
            last_name='',
            password='hello',
            email='admin@localhost',
            role=1
            )


    return dict(message="hello from install.py")
