# this is cross-compile toolchain 
SET (CMAKE_SYSTEM_NAME Generic)
SET (CMAKE_SYSTEM_PROCESSOR arm) # target processor while cross-compiling

# cross compiler setting
FILE (GLOB TOOLCHAIN_DIR 
    /usr/share/gcc-arm-none-eabi*)
SET (TOOLCHAIN_PATH ${TOOLCHAIN_DIR}/bin)

SET (TOOLCHAIN_PREFIX arm-none-eabi-) # gcc, g++, size, objcopy

SET (C_FLAGS
    "-fdata-sections -ffunction-sections \
    --specs=nano.specs -Wl,--gc-sections")
SET (CPP_FLAGS
    "-fno-rtti -fno-exceptions \
    -fno-threadsafe-statics")

# compiler setting
SET (CMAKE_C_COMPILER ${TOOLCHAIN_PATH}/${TOOLCHAIN_PREFIX}gcc)
SET (CMAKE_C_FLAGS ${C_FLAGS})

SET (CMAKE_ASM_COMPILER ${CMAKE_C_COMPILER}) # compile asm as c compiler

SET (CMAKE_CXX_COMPILER ${TOOLCHAIN_PATH}/${TOOLCHAIN_PREFIX}g++)
SET (CMAKE_CXX_FLAGS  ${FLGAS} ${CPP_FLAGS})

SET (CMAKE_OBJCOPY ${TOOLCHAIN_PREFIX}objcopy)

SET (CMAKE_SIZE ${TOOLCHAIN_PREFIX}size)

# output setting
SET (CMAKE_EXECUTABLE_SUFFIX_ASM ".elf")
SET (CMAKE_EXECUTABLE_SUFFIX_C ".elf")
SET (CMAKE_EXECUTABLE_SUFFIX_CXX ".elf")

# compile type
SET (CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)