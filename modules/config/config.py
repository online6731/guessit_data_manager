import logging
import yaml
import attrdict
from log4mongo.handlers import MongoHandler


with open("./modules/config/config.yml" , 'r') as yamlfileobj:
    config = attrdict.AttrDict(yaml.safe_load(yamlfileobj))


logging.basicConfig(
    # datefmt='%y-%b-%d %H:%M:%S',
    datefmt='%H:%M:%S',
    format='%(levelname)8s:[%(asctime)s][%(funcName)20s()][%(lineno)4s]: %(message)s',

    level=logging.DEBUG,
    handlers=[
        logging.FileHandler(f'{config.project_dir}/log.log', mode='w+', encoding='utf8', delay=0),
        logging.StreamHandler(),
        MongoHandler(host='198.143.179.211' , username='admin' , password='parishadbg18',port=27017,authentication_db='admin',database_name='DataManager',collection='log')

    ]
)

logger = logging.getLogger('DataGeters')
