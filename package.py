name = "usd"

authors = [
    "Pixar"
]

# NOTE: version = <usd_version>.sse.<sse_version>
version = "23.11.sse.2.0.0"

description = \
    """
    Universal Scene Description (USD) is an efficient, scalable system for authoring,
    reading, and streaming time-sampled scene description for interchange between
    graphics applications.
    """

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]
    # c.build_thread_count = 1  # we need to use just 1 core of the CPU

requires = [
    "tbb-2020.3",
    "boost-1.82",
    "numpy",
    "PyOpenGL-3.1.7",
    "openexr-3.1.12",
    "imath-3.1.5",
    "alembic-1.8.5",
    "OpenSubdiv-3.6.0",
    "materialx-1.38.9",
    "openvdb-9.1.0",
    "ocio-2.1.3",
    "oiio-2.5.9.0",
    "osl-1.13.7",
]

private_build_requires = [
    "Jinja2",
    "PySide6",
]

variants = [
    ["python-3.7"],
    ["python-3.9"],
    ["python-3.11"],
]

# NOTE: Do not build in debug mode since TBB and other dependencies are not built in debug
# If want to use Ninja, run:
# rez-build -i --cmake-build-system "ninja"
# rez-release --cmake-build-system "ninja"

uuid = "repository.USD"

def pre_build_commands():

    info = {}
    with open("/etc/os-release", 'r') as f:
        for line in f.readlines():
            if line.startswith('#'):
                continue
            line_info = line.replace('\n', '').split('=')
            if len(line_info) != 2:
                continue
            info[line_info[0]] = line_info[1].replace('"', '')
    linux_distro = info.get("NAME", "centos")
    print("Using Linux distro: " + linux_distro)

    if linux_distro.lower().startswith("centos"):
        command("source /opt/rh/devtoolset-6/enable")
    elif linux_distro.lower().startswith("rocky"):
        pass

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
