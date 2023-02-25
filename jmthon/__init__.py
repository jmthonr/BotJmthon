import glob
import logging

from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec

def load_plugins(plugin_name):
    path = Path(f"{working_dir}/{plugin_name}.py")
    name = "jmthon.plugins.{}".format(plugin_name)
    spec = spec_from_file_location(name, path)
    load = module_from_spec(spec)
    spec.loader.exec_module(load)
    modules["jmthon.plugins." + plugin_name] = load
    logging.info("🔷 Successfully Imported " + plugin_name)
    return


