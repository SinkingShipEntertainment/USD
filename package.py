name = "usd"

authors = [
    "Pixar"
]

# NOTE: version = <usd_version>.sse.<sse_version>
version = "22.11.sse.2.0.0"

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
    "tbb-2019.6",
    "boost-1.76.0",
    "OpenSubdiv-3.5.0",
    "oiio-2.3.15.0.sse.2",
    "ocio-2.1.1",
    "osl-1.12.10",
    "PyOpenGL-3.1.6",
    "alembic-1.8.5",
    "openexr-3.1.5",
    "materialx-1.38.6",
    "openvdb-9.1.0",
    "numpy",  # usdview is using it (I guess)
]

private_build_requires = [
    "Jinja2",
    "pyside2_setup-5.14.1",
]

# NOTE: Unfortunately, Ptex conflicts with Maya-Usd plugin and Arnold plugin for Maya.
# So, while building the maya-usd plugin against USD, we need to build it against a
# USD that was not build with Ptex. That means, OpenSubdiv and oiio will need to be
# build with/without Ptex as REZ variants as well.
variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-3.7", "!ptex"],
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-3.7", "ptex-2.3.2"],
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-3.9", "!ptex"],
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-3.9", "ptex-2.3.2"],
]

# If want to use Ninja, run:
# rez-build -i --cmake-build-system "ninja"
# rez-release --cmake-build-system "ninja"
#
# Pass cmake arguments (with debug symbols):
# rez-build -i --bt Debug -- -DBoost_NO_BOOST_CMAKE=On -DBoost_NO_SYSTEM_PATHS=True
# rez-release --bt Debug -- -DBoost_NO_BOOST_CMAKE=On -DBoost_NO_SYSTEM_PATHS=True

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

    env.LD_LIBRARY_PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    env.PYTHONPATH.append("{root}/lib/python")
