import configparser


class configLoader:
    def __init__(self,file:str = 'config.ini' ,section:str = 'DEFAULT'):
        conf = configparser.ConfigParser()
        conf.read(file)

    def check_init_variables():
        #TODO check that every variable needed is well initialized
        pass
        
    def save_conf_status():
        #TODO write the init file with the current configuration that we (keep track of wich item in the feed we processed) 
        pass

    def pretty_print():
        pass