BUILD_DIR := build
EXECUTABLE := clnt
IP = 127.0.0.1
PORT = 9090

all : clean build

build : cmake
	${MAKE} -C ${BUILD_DIR}

cmake :
	cmake -B ${BUILD_DIR}

clean :
	rm -rf ${BUILD_DIR}

run:
	./${BUILD_DIR}/${EXECUTABLE} ${IP} ${PORT}