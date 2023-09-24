module hello;
    initial begin
        $display("Hello World");
        $finish;
    end
    
endmodule

// compile with iverilog -o hello hello.v
// simulate with vvp hello