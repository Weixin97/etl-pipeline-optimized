"""
Running the Xetra ETL application
"""

import logging
import logging.config
import yaml 

def main():
    """
    entry point to run the xetra etl job
    """

    # parsing YAML file
    config_path = r'C:\Users\User\Documents\Python Scripts\etl-pipeline\etl-pipeline-optimized\configs\xetra_report1_config.yml'
    config = yaml.safe_load(open(config_path))
    # configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info('This is a test.') #print out the info message


    #print(config)


if __name__ == '__main__':
    main()