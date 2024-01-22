from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, user_type):
        if not user_type:
            raise ValueError ("User Type is Required")
        
        user = self.model(user_type = user_type)
        user.save(using =self.db)
        return user
    def create_superuser(self, user_type, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(user_type)
