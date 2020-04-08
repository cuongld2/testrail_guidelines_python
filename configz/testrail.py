import os

from utilz.cfgparse import CfgParse

cfg_parse = CfgParse(file_name=os.getcwd() + '/testrail.cfg')
testrail_config = cfg_parse.read_testrail_config()

TESTRAIL_DOMAIN_URL = testrail_config['API']['url']
TESTRAIL_USERNAME = testrail_config['API']['email']
TESTRAIL_PASSWORD = testrail_config['API']['password']







