from krunner.conf import get_config_value
from conf.schemes import Scheme

sn = get_config_value('serialno')[0]
pkg = get_config_value('pkg_name')

scheme = Scheme(pkg)