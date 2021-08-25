name = "usd"

authors = [
    "Pixar"
]

# NOTE: version = <usd_major>.<usd_minor>.sse.<sse_version>
version = "20.08.sse.1.0.0"

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
    "glew-2.0.0",
    "tbb-2017.6",
    "openexr-2.2.0",
    "ocio-1.0.9",
    "alembic-1.7.10",
    "OpenSubdiv-3.4.3",
    "PyOpenGL",
    "PySide2",
    "materialx-1.37.1",
    "openvdb-6.1.0",
    "oiio-2.1.16.0",
    "osl-1.9.13",
]

private_build_requires = [
    "Jinja2",
]

# NOTE: Unfortunately, Ptex conflicts with Maya-Usd plugin and Arnold plugin for Maya.
# So, while building the maya-usd plugin against USD, we need to build it against a
# USD that was not build with Ptex. That means, OpenSubdiv and oiio will need to be
# build with/without Ptex as REZ variants as well.
variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7", "boost-1.61.0", "!ptex"],
    ["platform-linux", "arch-x86_64", "os-centos-7", "boost-1.61.0", "ptex-2.1.28"],
    ["platform-linux", "arch-x86_64", "os-centos-7", "boost-1.70.0", "!ptex"],
    ["platform-linux", "arch-x86_64", "os-centos-7", "boost-1.70.0", "ptex-2.1.28"],
]

# If want to use Ninja, run:
# rez-build -i --cmake-build-system "ninja"
# rez-release --cmake-build-system "ninja"
#
# Pass cmake arguments:
# rez-build -i -- -DBoost_NO_BOOST_CMAKE=On -DBoost_NO_SYSTEM_PATHS=True
# rez-release -- -DBoost_NO_BOOST_CMAKE=On -DBoost_NO_SYSTEM_PATHS=True

uuid = "repository.USD"

def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")

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

    env.LD_LIBRARY_PATH.append("{root}/lib")
