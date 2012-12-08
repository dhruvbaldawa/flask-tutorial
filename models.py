from werkzeug.security import check_password_hash, generate_password_hash
from db import db


class User(db.Model):
    """
    User class to take care of user authentication, creation and deletion
    """
    __tablename__ = 'users' # This will be the name of the table in the database
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(255), unique=True, nullable=False)
    _password = db.Column('password', db.String(255), nullable=False)
    name = db.Column('name', db.String(255), nullable=False)

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = generate_password_hash(password)

    # Hide password encryption by exposing password field only.
    password = db.synonym('_password',
                          descriptor=property(_get_password, _set_password))

    @classmethod
    def authenticate(cls, username, password):
        ''' Authenticates a user, given his username and password
        Parameters
        ----------
        username : str
            The username of the user
        password : str
            The password of the user

        Returns
        -------
        status : bool
            The status of the operation
        return : dict
            The error/success message of the operation. It should contain a 
            'message' key which gives a human-readable description.
        '''
        # Check if user is in present in the database
        user = User.query.filter_by(username=username).first()
        if user is not None:
            # Check if the user has correct password
            if check_password_hash(user.password, password):
                return True, {"name": user.name, 
                    "message": "Login successful"}
            else:
                return False, {"message": 'Wrong password'}
        else:
            return False, {"message": 'User not found'}
