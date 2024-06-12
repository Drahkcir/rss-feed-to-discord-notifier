import configparser
import logging

logger=logging.getLogger('root')

class configLoader:
    
    def __init__(self,file:str = 'config.ini' ,section:str = 'DEFAULT'):
        self.file = file
        self.section = section
        self.conf = configparser.ConfigParser()
        self.conf.read(file)
        try:
            self.conf=self.conf[section]
        except KeyError as e: 
            err=f"section '[{section}]' not found in {file}"
            logger.error(err)
            raise(e)
        logger.info(f'section')

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