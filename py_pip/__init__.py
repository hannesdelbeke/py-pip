import sys
import subprocess
import pkgutil
import os
import pkg_resources  # todo replace deprecated module


default_target_path = ""

_cached_installed_packages = []


def run_command(command):
    # pass custom python paths, in case they were dynamically added
    my_env = os.environ.copy()
    joined_paths = os.pathsep.join(sys.path)
    env_var = my_env.get("PYTHONPATH")
    if env_var:
        joined_paths = f"{env_var}{os.pathsep}{joined_paths}"
    my_env["PYTHONPATH"] = joined_paths

    # Run the command and capture the output
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=my_env)
    output, error = process.communicate()
    return output, error


def list():
    """return tuple of (name, version) for each installed package"""
    output, error = run_command([sys.executable, "-m", "pip", "list"])

    # Parse the output of the pip list command
    packages = []
    raw = output.decode()

    for line in raw.split("\n")[2:-1]:  # 2-1 skips the first lines
        name, version = line.split()[:2]  # TODO edit packages contain a 3rd value: path 
        packages.append((name, version))

    global __cached_installed_packages
    __cached_installed_packages = packages
    return packages


def get_version(package_name, cached=False) -> str:
    """
    Return installed package version or empty string
    use_cached: requires running list before use. speed up get_version since pip list is slow
    """
    if cached:
        global __cached_installed_packages
        packages = __cached_installed_packages
    else:
        packages = list()
    for name, version in packages:
        if name == package_name:
            return version
    return ""


# def get_location(package_name) -> str:
#     output, error = run_command([sys.executable, "-m", "pip", "show", package_name])
#     raw = output.decode()
#     for line in raw.split("\n"):
#         if line.startswith("Location:"):
#             return line.split(" ")[1]
#     return ""


def get_location(package_name) -> str:
    # TODO cleanup
    def find_package_location(package_name):
        try:
            distribution = pkg_resources.get_distribution(package_name)
            return distribution.location
        except pkg_resources.DistributionNotFound:
            return f"Package '{package_name}' not found."
        
    try:
        loader = pkgutil.get_loader(package_name)
        if loader is not None:
            package_location = os.path.dirname(loader.get_filename())
            return package_location
        else:
            loc = find_package_location(package_name)
            if loc:
                return loc
            else:
                return f"Package '{package_name}' not found."
    except ImportError:
        return f"Error while trying to locate package '{package_name}'."


def install(package_name, invalidate_caches=True, target_path=None):
    """
    target_path: path where to install module too, if default_target_path is set, use that
    """
    command = [sys.executable, "-m", "pip", "install", package_name]
    target_path = target_path or default_target_path
    
    if target_path:
        command.extend(["--target", str(target_path)])
    output, error = run_command(command)

    # TODO if editable install, we add a pth file to target path.
    # but target path might not be in site_packages, and pth might not be processed.
    # if target_path:
    #     import site
    #     site.addsitedir(pth_path)
    #     site.removeduppaths()

    if invalidate_caches:
        import importlib
        importlib.invalidate_caches()
    return output, error    


def get_package_modules(package_name):
    # Get a list of modules that belong to the specified package
    package_modules = []
    package_loader = pkgutil.get_loader(package_name)

    if package_loader is not None:
        for _, module_name, _ in pkgutil.walk_packages(package_loader.get_filename()):
            full_module_name = f"{package_name}.{module_name}"
            package_modules.append(full_module_name)

    return package_modules


def uninstall(package_name, delete_module=True):
    command = [sys.executable, "-m", "pip", "uninstall", package_name]
    output, error = run_command(command)
    if delete_module:
        for module_name in get_package_modules(package_name):
            if module_name in sys.modules:
                del sys.modules[module_name]