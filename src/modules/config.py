import configparser
import logging

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
        logger.debug('checking the vraible initialization from ini file')
        for i in ['webhook_url', 'rss_feed_url', 'author_name', 
                  'author_image_url', 'author_url', 'embeded_image_url', 
                  'footer_message', 'footer_image_url']:
            try:
                if self.conf[i] :
                    logging.debug(f'{i} initialized : {self.conf[i]}')
                    continue
                else:
                    raise(KeyError)
            except KeyError: 
                logging.error(f'{i} not initialized or empty in the file : {self.file} section : [{self.section}]')
                exit(-1)
        pass

    def pretty_print(self):
        msg=f'file : {self.file} , section : {self.section}\n' 
        for i in self.conf.items():
            msg += f'\t{i[0]} = {i[1]} \n'
        print(msg, end='')