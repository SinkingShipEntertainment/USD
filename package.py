name = "usd"

authors = [
    "Pixar"
]

version = "21.05"

description = \
    """
    Universal Scene Description (USD) is an efficient, scalable system for authoring,
    reading, and streaming time-sampled scene description for interchange between
    graphics applications.
    """

build_dir_name = None
with scope("config") as c:
    # Determine location to release: internal (int) vs external (ext)

    # NOTE: Modify this variable to reflect the current package situation
    release_as = "ext"

    # The `c` variable here is actually rezconfig.py
    # `release_packages_path` is a variable defined inside rezconfig.py

    import os
    if release_as == "int":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_INT"]
    elif release_as == "ext":
        c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

    build_dir_name = c.build_directory

requires = [
    "PySide2",
]

private_build_requires = [
    "cmake",
    "gcc",
    "pip",
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-2.7"]
]

build_command_str = "python {root}/build_scripts/build_usd.py"
build_command_str += " {root}/" + build_dir_name
build_command_str += " --verbose"
build_command_str += " --debug"
build_command_str += " --force-all"
build_command_str += " --no-tests"
build_command_str += " --examples"
build_command_str += " --tutorials"
build_command_str += " --tools"
build_command_str += " --python"
build_command_str += " --usd-imaging"
build_command_str += " --ptex"
build_command_str += " --openvdb"
build_command_str += " --usdview"
build_command_str += " --openimageio"
build_command_str += " --opencolorio"
build_command_str += " --alembic"
build_command_str += " --hdf5"
build_command_str += " --materialx"

build_command = build_command_str

uuid = "repository.USD"

def commands():
    # NOTE: REZ package versions can have "-" to separate the external
    # version from the internal modification version.
    # Example: 21.05-sse.1
    # 21.05 is the USD version and sse.1 is the internal version
    split_versions = str(version).split('-')
    env.USD_VERSION.set(split_versions[0])
    env.USD_PACKAGE_VERSION.set(split_versions[1])

    env.USD_ROOT.append("{root}")

    env.USD_INCLUDE_DIR.set("{root}/include")
    env.USD_LIBRARY_DIR.set("{root}/lib")
    env.USD_PYTHON_DIR.set("{root}/lib/python")

    env.PATH.append("{root}/bin")
    env.PATH.append("{root}/lib")

    env.PYTHONPATH.append("{0}".format(env.USD_PYTHON_DIR))
