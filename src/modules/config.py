import configparser
import logging

logger=logging.getLogger('root')

class configLoader:
    def __init__(self,file:str = 'config.ini' ,section:str = 'DEFAULT'):
        self.conf = configparser.ConfigParser()
        self.conf.read(file)

    def check_init_variables(self):
        #TODO check that every variable needed is well initialized
        pass
        
    def save_conf_status(self):
        #TODO write the init file with the current configuration that we (keep track of wich item in the feed we processed) 
        self.conf.write(self)
        pass

    def pretty_print(self):
        msg=f'file : {self.file} , section : {self.section}\n' 
        for i in self.conf.items():
            msg += f'\t{i[0]} = {i[1]} \n'
        print(msg, end='')