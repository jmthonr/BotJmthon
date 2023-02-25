import glob
from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec

def load_plugins(plugin_name):
    path = Path(f"{working_dir}/{plugin_name}.py")
    name = "jmthon.plugins.{}".format(plugin_name)
    spec = spec_from_file_location(name, path)
    load = module_from_spec(spec)
    spec.loader.exec_module(load)
    modules["jmthon.plugins." + plugin_name] = load
    LOGGER.info("🔷 Successfully Imported " + plugin_name)
    return


path = 'jmthon/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_plugins(shortname.replace(".py", ""))
