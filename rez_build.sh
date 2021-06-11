!/usr/bin/bash

root_dir=$1

# build
echo "----------------------------------------------------------------------"
echo "Running build.py..."
echo "----------------------------------------------------------------------"

echo "REZ_BUILD_PATH: ${REZ_BUILD_PATH}"
echo "REZ_BUILD_INSTALL_PATH: ${REZ_BUILD_INSTALL_PATH}"
echo "PATH: ${PATH}"

# NOTE: -vvv is verbose = 3
# NOTE: I am using --jobs 1 because Centos 7 has an issue with building with -j > 1
# NOTE: Not building with OSL: --build-args USD,"-DPXR_USE_PYTHON_3=OFF -DPXR_ENABLE_OSL_SUPPORT=TRUE" \

if [ ${USE_PYTHON} = 2 ]
then
    # Building variant 0 (python-2.7)
    echo "Building for Python 2"

    python ${root_dir}/build_scripts/build_usd.py \
        ${REZ_BUILD_INSTALL_PATH} \
        -vvv \
        --build ${REZ_BUILD_PATH} \
        --build-args USD,"-DPXR_USE_PYTHON_3=OFF" \
        --no-tests \
        --no-examples \
        --no-tutorials \
        --no-docs \
        --no-embree \
        --no-prman \
        --no-draco \
        --tools \
        --python \
        --usd-imaging \
        --ptex \
        --openvdb \
        --usdview \
        --openimageio \
        --opencolorio \
        --alembic \
        --hdf5 \
        --materialx \
        --jobs "1"

elif [ ${USE_PYTHON} = 3 ]
then
    # Building variant 1 (python-3.7)
    echo "Building for Python 3"

    python ${root_dir}/build_scripts/build_usd.py \
        ${REZ_BUILD_INSTALL_PATH} \
        -vvv \
        --build ${REZ_BUILD_PATH} \
        --build-args USD,"-DPXR_USE_PYTHON_3=ON" \
        --no-tests \
        --no-examples \
        --no-tutorials \
        --no-docs \
        --no-embree \
        --no-prman \
        --no-draco \
        --tools \
        --python \
        --usd-imaging \
        --ptex \
        --openvdb \
        --usdview \
        --openimageio \
        --opencolorio \
        --alembic \
        --hdf5 \
        --materialx \
        --jobs "1"

fi
