import configparser
import logging
import re

logger=logging.getLogger('root')

class configLoader:

    def __init__(self,file:str = 'config.ini' ,section:str = 'DEFAULT'):
        self.file = file
        self.section = section
        self.configuration_parser = configparser.ConfigParser()
        self.configuration_parser.read(file)
        logger.info(f'__init__ -> file {self.file} read')
        
        if not (section in self.configuration_parser.sections() or 
                section == 'DEFAULT' ) :
            logger.error(f"__init__ -> section '[{section}]' not found in {file}")
            exit(-1)
        
        logger.info(f'__init__ -> section {self.section} loaded ')
        self.check_init_variables()

    def check_init_variables(self):
        logger.debug('check_init_variables -> checking the variable initialization from ini file')
        for i in ['webhook_url', 'rss_feed_url', 'author_name', 
                  'author_image_url', 'author_url', 'embeded_image_url', 
                  'footer_message', 'footer_image_url']:
        
            value = self.get_field(i)
            if value:
                logging.debug(f'check_init_variables -> {i} initialized : {value}')
                continue
            else:
                logging.error(f'check_init_variables -> {i} not initialized or empty in the file : {self.file} section : [{self.section}]')
                exit(-1)


    def set_field(self,key:str, value:str):
        if isinstance(value,str):
            value = f"'{value}'"
        self.configuration_parser.set(self.section, key, str(value))

        # once updated we save the config to the file to be updated
        self.save_config()

    def get_field(self, key:str):
        val = self.configuration_parser[self.section].get(key,None)
        regex=r'^([\'"])(.*)\1$'
        if val:
            val = re.sub(regex,r'\2',val)
            logging.debug(f'get_field -> got {key}\'s value : {val}')
            return val
        
        logger.error(f'get_field -> key : {key} not found in the config file \'{self.file}\' section [{self.section}]')
        exit(-1)
        
    def save_config(self): 
        with open(self.file, 'w') as configfile:
            self.configuration_parser.write(configfile)


    def pretty_print(self):
        msg=f'file : {self.file} , section : {self.section}\n' 
        for i in self.configuration_parser[self.section]:
            msg += f'\t{i} = {self.configuration_parser[self.section][i]} \n'
        print(msg, end='')