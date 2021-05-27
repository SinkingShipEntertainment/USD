name = "usd"

authors = [
    "Pixar"
]

version = "21.08"

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
    "gcc-6.3",
    "tbb-2017.6",
    "glfw-3.4.0",
    "glew-2.0.0",
    "ptex-2.1.28",
    "OpenSubdiv-3.4.3",
    "openexr-2.2.0",
    "ocio-1.0.9",
    "oiio-2.1.16.0",
    "osl-1.9.13",
    "openvdb-6.1.0",
    "PySide2",
    "PyOpenGL",
    "Jinja2",
]

private_build_requires = [
    "cmake",
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-2.7", "boost-1.70.0"],
    ["platform-linux", "arch-x86_64", "os-centos-7", "python-3.7", "boost-1.70.0"],
]

# If want to use Ninja, run the `rez-build -i --cmake-build-system "ninja"`
# or `rez-release --cmake-build-system "ninja"`

uuid = "repository.USD"

def commands():
    # NOTE: REZ package versions can have "-" to separate the external
    # version from the internal modification version.
    # Example: 21.05-sse.1
    # 21.05 is the USD version and sse.1 is the internal version
    split_versions = str(version).split('-')
    env.USD_VERSION.set(split_versions[0])
    if len(split_versions) == 2:
        env.USD_PACKAGE_VERSION.set(split_versions[1])

    env.USD_ROOT.append("{root}")
    env.USD_LOCATION.append("{root}")

    env.USD_INCLUDE_DIR.set("{root}/include")
    env.USD_LIBRARY_DIR.set("{root}/lib")
    env.USD_PYTHON_DIR.set("{root}/lib/python")

    env.PATH.append("{root}/bin")
    env.PATH.append("{root}/lib")

    env.PYTHONPATH.append("{0}".format(env.USD_PYTHON_DIR))
