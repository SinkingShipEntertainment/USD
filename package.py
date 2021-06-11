name = "usd"

authors = [
    "Pixar"
]

# NOTE: version = <usd_major>.<usd_minor>.sse.<python_major>.<sse_major>.<sse_patch>
# NOTE Remember to modify the `pre_build_commands` function and the `private_build_requires`
version = "20.08.sse.2.0.0"  # Python 2

description = \
    """
    Universal Scene Description (USD) is an efficient, scalable system for authoring,
    reading, and streaming time-sampled scene description for interchange between
    graphics applications.
    """

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

    #c.build_thread_count = "physical_cores"

requires = [
]

private_build_requires = [
    "cmake",
    "python-2.7",
    "PyOpenGL",
    "Jinja2",
    "PySide2",
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7"],
]

build_command = "bash {root}/rez_build.sh {root}"

# If want to use Ninja, run the `rez-build -i --cmake-build-system "ninja"`
# or `rez-release --cmake-build-system "ninja"`

uuid = "repository.USD"

def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")
    env.USE_PYTHON = 2

def commands():
    # NOTE: REZ package versions can have ".sse." to separate the external
    # version from the internal modification version.
    split_versions = str(version).split(".sse.")
    external_version = split_versions[0]
    internal_version = None
    if len(split_versions) == 2:
        internal_version = split_versions[1]

    env.USD_VERSION = external_version
    env.USD_PACKAGE_VERSION = external_version
    if internal_version:
        env.USD_PACKAGE_VERSION = internal_version

    env.USD_ROOT.append("{root}")
    env.USD_LOCATION.append("{root}")

    env.USD_INCLUDE_DIR = "{root}/include"
    env.USD_LIBRARY_DIR = "{root}/lib"
    env.USD_PYTHON_DIR = "{root}/lib/python"

    env.PATH.append("{root}/bin")
    env.PATH.append("{root}/lib")

    env.PYTHONPATH.append("{root}/lib/python")
