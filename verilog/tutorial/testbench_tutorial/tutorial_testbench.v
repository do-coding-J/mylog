`timescale 1ns/1ns
module testbench;
    reg a,b,c;
    reg [2:0] v;

    initial begin
        $dumpfile("tutorial_testbench.vcd");
		// $dumpvars(-1, _tutorial_testbench);
        $dumpvars;

        a = 0; v = 3'b000; #50;
		b = 1; v = 3'b010; #50;
		a = 0; b = 1; c = 0; #50;
		v = 3'b110; #50;
    end

endmodule