BUILD_DIR := build
EXECUTABLE := type
IP = 127.0.0.1
PORT = 9090
DOMAIN = www.naver.com

all : build

build : cmake
	${MAKE} -C ${BUILD_DIR}

cmake :
	cmake -B ${BUILD_DIR}

clean :
	rm -rf ${BUILD_DIR}

run :
	./build/${EXECUTABLE}