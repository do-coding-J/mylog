BUILD_DIR := build
EXECUTABLE := lread

all : clean build

build : cmake
	${MAKE} -C ${BUILD_DIR}

cmake :
	cmake -B ${BUILD_DIR}

clean :
	rm -rf ${BUILD_DIR}

run :
	sudo ./build/${EXECUTABLE}