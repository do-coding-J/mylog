BUILD_DIR := build
EXECUTABLE := iterative_echo_clnt2
IP = 127.0.0.1
PORT = 9090

all : build

build : cmake
	${MAKE} -C ${BUILD_DIR}

cmake :
	cmake -B ${BUILD_DIR}

clean :
	rm -rf ${BUILD_DIR} 

run :
	./build/${EXECUTABLE} ${PORT}