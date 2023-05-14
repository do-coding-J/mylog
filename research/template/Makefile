BUILD_DIR := build
BUILD_TYPE ?= Debug

all : build # do build

${BUILD_DIR}/Makefile: # cmake cofigure
	cmake \
		-B${BUILD_DIR}\
		-DCMAKE_BUILD_TYPE=${BUILD_TYPE} \
		-DCMAKE_TOOLCHAIN_FILE=arm-none-eabi.cmake

cmake: ${BUILD_DIR}/Makefile #do ${BUILD_DIR}/Makefile 
# do cmake and execute make at ${BUILD_DIR}
build : cmake 
	${MAKE} -C ${BUILD_DIR} --no-print-directory

clean : 
	rm -rf ${BUILD_DIR} # empty build

rebuild :
	${MAKE} clean --no-print-directory
	${MAKE} all --no-print-directory