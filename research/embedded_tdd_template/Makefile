FW := firmware
TEST := test
BUILD_DIR := build
FW_FILE_EXISTS = 0
TEST_FILE_EXISTS = 0
## all
all: build

build : fw test

clean : fw_clean test_clean

## firmware
fw : fw_check fw_build

fw_build:
ifeq (${FW_FILE_EXISTS},0)
	${MAKE} -C ${FW} clean
	${MAKE} -C ${FW} build
else
	${MAKE} -C ${FW} build
endif

fw_clean:
	${MAKE} -C ${FW} clean --no-print-directory --quiet

fw_check:
ifneq ("$(wildcard ${FW}/${BUILD_DIR})","")
FW_FILE_EXISTS = 1
else
FW_FILE_EXISTS = 0
endif

## test
test : test_check test_build test_execute

test_build:
ifeq (${TEST_FILE_EXISTS},0)
	${MAKE} -C ${TEST} clean
	${MAKE} -C ${TEST} build
else
	${MAKE} -C ${TEST} build
endif

test_clean:
	${MAKE} -C ${TEST} clean --no-print-directory --quiet

test_check:
ifneq ("$(wildcard ${TEST}/${BUILD_DIR})","")
TEST_FILE_EXISTS = 1
else
TEST_FILE_EXISTS = 0
endif

test_execute: 
	$(foreach file, $(wildcard ${TEST}/$(BUILD_DIR)/*_TEST), ./$(file);)