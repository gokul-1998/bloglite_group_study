import secrets
class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"
    SECRET_KEY = '4FJwO_fyFymIe26DjpIQ0IWwVl_BoKtGIyGexUPFo0s'
    # secret key is used for generating tokens, 
    SECURITY_PASSWORD_SALT = '52c1cd1dbfa6f21207ec7cc328931af721ca0855'
    # password salt is used for hashing passwords
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    # track modifications is used to suppress warning, 
    # if we don't set it to false, it will give us warning that it is true and it will slow down the application
    SECURITY_REGISTERABLE = True
    # registerable is used to enable registration of new users 
    # if we set it to false, then we can't register new users 
    # but we can still create new users from the backend 
    # and we can also create new users from the flask shell 

    SECURITY_CONFIRMABLE = False
    # confirmable is used to enable email confirmation , 
    # if we set it to false, then we can't confirm email
    # but we can still create new users from the backend 
    # and we can also create new users from the flask shell
    SECURITY_SEND_REGISTER_EMAIL = False
    # send register email is used to send email to the user after registration, 
    # if we set it to false, then we can't send email to the user after registration
    # but we can still create new users from the backend
    SECURITY_UNAUTHORIZED_VIEW = None
    # unauthorized view is used to redirect user to a specific page if the user is not authorized to access a specific page
    # if we set it to none, then it will redirect user to the login page

    WTF_CSRF_ENABLED = False
    # wtf csrf enabled is used to enable csrf protection, 
    # if we set it to false, then we can't protect our forms from csrf attacks
    
    SECURITY_API_ENABLED_METHODS=['token']
    SECURITY_USERNAME_ENABLE=True
    SECURITY_USERNAME_REQUIRED=True
    CELERY_BROKER_URL="redis://default:vmy16jAbvbHXlBph9PqGn9pwsXK6P7NE@redis-17198.c301.ap-south-1-1.ec2.cloud.redislabs.com:17198/0"
    CELERY_RESULT_BACKEND = "redis://default:vmy16jAbvbHXlBph9PqGn9pwsXK6P7NE@redis-17198.c301.ap-south-1-1.ec2.cloud.redislabs.com:17198/1"
    CELERY_IMPORTS = ('backend.applicaiton.task')
    CACHE_TYPE = 'RedisCache'
    CACHE_DEFAULT_TIMEOUT=300
    CACHE_REDIS_HOST='redis-17198.c301.ap-south-1-1.ec2.cloud.redislabs.com'
    CACHE_REDIS_PORT=17198