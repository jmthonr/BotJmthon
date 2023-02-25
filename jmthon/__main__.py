import contextlib
import logging
import glob
import sys
from sys import modules
from importlib.util import spec_from_file_location, module_from_spec

from pathlib import Path



def load_plugins(plugin_name):
    path = Path(f"jmthon/plugins/{plugin_name}.py")
    name = "jmthon.plugins.{}".format(plugin_name)
    spec = spec_from_file_location(name, path)
    load = module_from_spec(spec)
    spec.loader.exec_module(load)
    modules["jmthon.plugins." + plugin_name] = load
    logging.info("🔷 Successfully Imported " + plugin_name)
    return


path = 'jmthon/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_plugins(shortname.replace(".py", ""))

print("workkkkkkkkk")

if len(sys.argv) in {1, 3, 4}:
    with contextlib.suppress(ConnectionError):
        jmthon.run_until_disconnected()
else:
    jmthon.disconnect()
