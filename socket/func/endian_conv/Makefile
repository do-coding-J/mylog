BUILD_DIR := build
EXECUTABLE := endian_conv

all : build

build : cmake
	${MAKE} -C ${BUILD_DIR}

cmake :
	cmake -B ${BUILD_DIR}

clean :
	rm -rf ${BUILD_DIR}

run :
	./build/${EXECUTABLE}