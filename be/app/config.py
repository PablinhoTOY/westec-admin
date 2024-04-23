class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True


    # PROPLAYER
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://admin:eurocorp@192.168.10.151:3306/nic_2"

    # LOCAL2 
    #SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@127.0.0.1:3306/nic_2"

    # PRODUCCION
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://carnet:dTwM2023@localhost:3306/carnet"
    
    # DEV
    # SQLALCHEMY_DATABASE_URI = "sqlite:///datos.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    LANGUAGES = ['es', 'en']


config = {
    "development": DevelopmentConfig,
}
