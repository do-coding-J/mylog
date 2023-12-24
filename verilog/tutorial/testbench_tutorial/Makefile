file_name = tutorial_testbench

all: compile make sim

compile:
	iverilog -o ${file_name}.vvp ${file_name}.v

make:
	vvp ${file_name}.vvp

sim:
	gtkwave ${file_name}.vcd