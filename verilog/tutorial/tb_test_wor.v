`timescale 1ms/1ms

`include "test_wor.v"

module tb_test_wor();

	reg a, b, c, d, e, f, g, h, i;
	wire y;

	test_wor _test_wor(
		.y(y),

		.a(a), .b(b), .c(c),
		.d(d), .e(e), .f(f),
		.g(g), .h(h), .i(i)
	);

	initial begin
		// for simulation
		$dumpfile("test_wor.vcd");
		$dumpvars(-1, _test_wor);

		// initialize
		a <= 0; b <= 0; c <= 0;
		d <= 0; e <= 0; f <= 0;
		g <= 0; h <= 0; i <= 0;

		// start
		#1 a = 1; #1 b = 1; #1 c = 1;
		#1 d = 1; #1 e = 1; #1 f = 1;
		#1 g = 1; #1 h = 1; #1 i = 1;

		// end
		#1
		$finish;
	end

endmodule