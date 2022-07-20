find_program(PYSIDEUICBINARY
    NAMES
        uic
    NO_DEFAULT_PATH
    NO_SYSTEM_ENVIRONMENT_PATH
    HINTS
        $ENV{REZ_PYSIDE2_SETUP_ROOT}/bin
)


if (EXISTS ${PYSIDEUICBINARY})
    message(STATUS "Found uic: will use ${PYSIDEUICBINARY} for uic binary")
    set(PYSIDE_AVAILABLE True)
else()
    message(STATUS "uic not found")
    set(PYSIDE_AVAILABLE False)
endif()

include(FindPackageHandleStandardArgs)

find_package_handle_standard_args(PySide2REZ
    REQUIRED_VARS
        PYSIDE_AVAILABLE
        PYSIDEUICBINARY
)