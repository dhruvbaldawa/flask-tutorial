# The users in the system.
USERS = {
    "dhruv": {"name": "Dhruv Baldawa", "password": "pass"},
    "jack": {"name": "Jack Sparrow", "password": "pass"},
}


class User(object):
    """
    User class to take care of user authentication, creation and deletion
    """
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
        if username in USERS.keys():
            # Check if the user has correct password
            if USERS[username]['password'] == password:
                return True, {"name": USERS[username]["name"], 
                    "message": "Login successful"}
            else:
                return False, {"message": 'Wrong password'}
        else:
            return False, {"message": 'User not found'}
