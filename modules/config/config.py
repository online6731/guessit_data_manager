import logging
import yaml
from attrdict import AttrDict

# --------------------------------------------------------------------
# project data config
# --------------------------------------------------------------------

with open("config.yaml" , 'r') as yamlfileobj:
    config = AttrDict(yaml.safe_load(yamlfileobj))


# --------------------------------------------------------------------
# logger config
# --------------------------------------------------------------------

logging.basicConfig(
    # datefmt='%y-%b-%d %H:%M:%S',
    datefmt='%H:%M:%S',
    format='%(levelname)8s:[%(asctime)s][%(funcName)20s()][%(lineno)4s]: %(message)s',

    level=logging.DEBUG,
    handlers=[
        logging.FileHandler(f'{project_dir}/log.log', mode='w+', encoding='utf8', delay=0),
        logging.StreamHandler(),
    ]
)

logger = logging.getLogger('DataGeters')
