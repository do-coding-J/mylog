// display test
module display_test (input data);
    initial begin
        $display("Input data : %b", data);
    end
endmodule