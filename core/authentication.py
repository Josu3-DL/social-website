from django.contrib.auth.models import User

#costum the authentication method
class EmailAuthBackend:
    '''
    Authenticate using an e-mail address
    '''

    def authenticate(self,request, username = None, password = None):
        try:
            user = User.objects.get(email = username)
            if user.check_password(password):
                return user 
            return None
        
        # The MultipleObjectsReturned exception is raised if multiple users are found with the same # email address. 
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None
        

    def get_user(self, id_user):
        try:
            return User.objects.get(pk=id_user)
        except User.DoesNotExist:
            return None