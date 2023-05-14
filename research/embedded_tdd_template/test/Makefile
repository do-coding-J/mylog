BUILD_DIR := build
BUILD_TYPE ?= Debug


all : build

build : cmake
	${MAKE} -C ${BUILD_DIR} --no-print-directory

cmake :
	cmake \
		-B ${BUILD_DIR}

clean :
	rm -rf ${BUILD_DIR}