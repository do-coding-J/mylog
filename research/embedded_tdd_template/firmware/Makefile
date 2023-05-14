BUILD_DIR := build
BUILD_TYPE ?= Debug


all : build

build : cmake
	${MAKE} -C ${BUILD_DIR} --no-print-directory

cmake :
	cmake \
		-B ${BUILD_DIR} \
		-D CMAKE_TOOLCHAIN_FILE=arm-none-eabi.cmake \
		-D CMAKE_BUILD_TYPE=${BUILD_TYPE}

clean :
	rm -rf ${BUILD_DIR}