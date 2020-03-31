from app import db, bcrypt, login_manager

class User():
    def __init__(self,  username, password, name, email, id=None):
        self.id = id
        self.username = username
        self.password = bcrypt.generate_password_hash(password)
        self.name = name
        self.email = email

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def check_password(password_hash, password):
        return check_password_hash(password_hash, password)


    @login_manager.user_loader
    def load_user(username):
        u = db.users.find_one({"username": username})
        if not u:
            return None
        return User(username= u['username'], password = u['password'], name= u['name'], email = u['email'], id = u['_id'])


    def verify_password(self, pwd):
        return bcrypt.check_password_hash(self.password, pwd)

    def inserirDados(self):
        usuario = db.users

        user_exist = usuario.find_one({'username': self.username})
        if user_exist is None:
            usuario.insert_one(
                {
                    '_id': int(usuario.find().count()) + 1,
                    'username': self.username,
                    'password': self.password,
                    'name': self.name,
                    'email': self.email,

                }
            )
