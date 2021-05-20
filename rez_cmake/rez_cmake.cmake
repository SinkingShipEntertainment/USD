
# FindBoost and FindPython
set(BOOST_ROOT $ENV{REZ_BOOST_ROOT})

#set(Boost_VERSION 1.70)
#set(Boost_INCLUDE_DIRS $ENV{BOOST_INCLUDEDIR})
#set(Boost_LIBRARY_DIRS $ENV{BOOST_LIBRARYDIR})
#set(Boost_PYTHON_LIBRARIES $ENV{REZ_BOOST_ROOT}/lib)
#set(Boost_LIBRARIES
#    $ENV{REZ_BOOST_ROOT}/lib/libboost_atomic.so
#    $ENV{REZ_BOOST_ROOT}/lib/libboost_program_options.so
#    $ENV{REZ_BOOST_ROOT}/lib/libboost_date_time.so
#    $ENV{REZ_BOOST_ROOT}/lib/libboost_system.so
#    $ENV{REZ_BOOST_ROOT}/lib/libboost_thread.so
#    $ENV{REZ_BOOST_ROOT}/lib/libboost_regex.so
#)
#set(Boost_PYTHON27_LIBRARIES
#    $ENV{REZ_BOOST_ROOT}/lib/libboost_python27.so
#)

# In cmake/defaults/packages.cmake, there is the logic of finding Boost.
set(Boost_NO_SYSTEM_PATHS True)
set(Boost_NO_BOOST_CMAKE On)  # Since we are using Boost-1.70
