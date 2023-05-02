BUILD_DIR := build
EXECUTABLE := tcp_clnt
IP = 127.0.0.1
PORT_NUM = 9900

all : clean build

build : cmake
	${MAKE} -C ${BUILD_DIR}

cmake :
	cmake -B ${BUILD_DIR}

clean :
	rm -rf ${BUILD_DIR}

run :
	./build/${EXECUTABLE} ${IP} ${PORT_NUM}