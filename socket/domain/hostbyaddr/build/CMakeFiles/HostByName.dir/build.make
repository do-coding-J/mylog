# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/jj/ws/log/socket/domain/hostbyaddr

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/jj/ws/log/socket/domain/hostbyaddr/build

# Include any dependencies generated for this target.
include CMakeFiles/HostByName.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/HostByName.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/HostByName.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/HostByName.dir/flags.make

CMakeFiles/HostByName.dir/main.c.o: CMakeFiles/HostByName.dir/flags.make
CMakeFiles/HostByName.dir/main.c.o: ../main.c
CMakeFiles/HostByName.dir/main.c.o: CMakeFiles/HostByName.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jj/ws/log/socket/domain/hostbyaddr/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/HostByName.dir/main.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -MD -MT CMakeFiles/HostByName.dir/main.c.o -MF CMakeFiles/HostByName.dir/main.c.o.d -o CMakeFiles/HostByName.dir/main.c.o -c /home/jj/ws/log/socket/domain/hostbyaddr/main.c

CMakeFiles/HostByName.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/HostByName.dir/main.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/jj/ws/log/socket/domain/hostbyaddr/main.c > CMakeFiles/HostByName.dir/main.c.i

CMakeFiles/HostByName.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/HostByName.dir/main.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/jj/ws/log/socket/domain/hostbyaddr/main.c -o CMakeFiles/HostByName.dir/main.c.s

# Object files for target HostByName
HostByName_OBJECTS = \
"CMakeFiles/HostByName.dir/main.c.o"

# External object files for target HostByName
HostByName_EXTERNAL_OBJECTS =

HostByName: CMakeFiles/HostByName.dir/main.c.o
HostByName: CMakeFiles/HostByName.dir/build.make
HostByName: CMakeFiles/HostByName.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/jj/ws/log/socket/domain/hostbyaddr/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable HostByName"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/HostByName.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/HostByName.dir/build: HostByName
.PHONY : CMakeFiles/HostByName.dir/build

CMakeFiles/HostByName.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/HostByName.dir/cmake_clean.cmake
.PHONY : CMakeFiles/HostByName.dir/clean

CMakeFiles/HostByName.dir/depend:
	cd /home/jj/ws/log/socket/domain/hostbyaddr/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jj/ws/log/socket/domain/hostbyaddr /home/jj/ws/log/socket/domain/hostbyaddr /home/jj/ws/log/socket/domain/hostbyaddr/build /home/jj/ws/log/socket/domain/hostbyaddr/build /home/jj/ws/log/socket/domain/hostbyaddr/build/CMakeFiles/HostByName.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/HostByName.dir/depend

