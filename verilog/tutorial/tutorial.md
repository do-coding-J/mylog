# icarus 사용법

## .v 확장자
> 예시 : hello.v

## iverilog 사용하여 컴퍼일
> 예시 : iverilog -o ${output name}.vvp {file name}

## vvp 사용하여 시뮬레이션
> 예시 : vvp ${output name}.vvp

## gtkwave 사용하여 시각화
> 예시 : gktwave ${output name}.vcd


## verilog syntax 
### 1. module
사용 방법 :   
```
module my_module (a, b, c, e);
    input a, b;
    output c, d;
    ...
endmodule
```

호출 방법 :
- 순서 호출
- 이름 호출
```
module top; 
   reg A, B; 
   wire C, D;  
   my_module m1 (A, B, C, D);     // By order    
   my_module m2 (.b(B), .d(D), .c(C), .a(A)); // By name 
   ... 
 
 endmodule 
```

중목되는 변수는 override됨

### 2. data types
1. physical
- net : default(z)
- register : default(x)
- charge storage node (battery, capacitor etc.) : default(x)
2. abstract
- integer : 32bit signed
- timer : 64bit unsinged ($time)
- real : floating point
- parameter : constant
- event : only name reference (no value)
> verilog에는 user-defined type이 없다. (VHDL에는 있음)

### 3. value and literals
1. basic values
- 0 : logic zero or false
- 1 : logic one or true
- x : unknown/undefined logic value (only for physical data)
- z : high-impedence/floating state (only for physical data)
2. constants
> expressed as : width 'radix value
- width : length of array
- radix : 'b(binary), 'o(octal), 'h(hex), 'd(decimal)
- value : value of it

### 4. wire
1. wire : 그냥 wire
2. wor : or 연산을 하는 wire
3. wand : and 연산을 하는 wire

### 5. vector & array
1. vector : bus와 같은 하나의 신호를 표시 할 때 사용
- wire [7:0] data : 8bit의 데이터 뭉치
2. array : 같은 형식의 변수를 보관 할 때 사용
- reg [7:0] data [3:0] : 8 bit의 데이터 4개짜리 배열

### 6. task & function
1. task
- 0 argument
- 0 return
- delay, event, timing control
2. function
- should contain argument
- should have return value
- no time control

```
module m; 
  reg [1:0] r1; 
  reg [3:0] r2; 
  reg r3; 
 
  ... 
  always 
  begin 
    ... 
    r2 = my_func(r1);  // Invoke function     
    ... 
    my_task (r2, r3);  // Invoke task    
    ... 
  end 
 
  task my_task;     
    input [3:0] i; 
    output o;     
    begin 
      ... 
    end 
  endtask   
  ... 
  function [3:0] my_func; 
    input [1:0] i;     
    begin 
      ...       
      my_func = ...;   // Return value 
    end 
  endfunction 
  ... 
endmodule
```

### 7. system task & compiler directives
- system task
```
$display("format", v1, v2, ...);  // Similar format to printf() in C 
$write("format", v1, v2, ...);    // $display appends newline at the end, 
                                  //   but $write does not. 
$strobe("format", v1, v2, ...);   // $strobe always executes last among  
                                  //   assignment statements of the same  
                                  //   time.  Order for $display among  
                                  //   assignment statements of the same        
                                  //   time is unknown. 
$monitor("format", v1, v2, ...); // Invoke only once, and execute (print)        
                                  //   automatically when any of the   
                                  //   variables change value. $monitoron;  
                                  // Enable monitoring from here $monitoroff;  
                                  // Disable monitoring from here 
$stop;                            // Stop the simulation 
$finish;                          // Terminate and exit the simulation 
$time;                            // Return current simulation time in 64-bit integer $stime;                           // Return current simulation time in 32-bit integer
$realtime;                        // Return current simulation time in 64-bit real  
$random(seed);                    // Return random number.  Seed is optional.
```
- directives
```
`define alias text                // Create an alias.  Aliases are replaced/substituted 
                                  //  prior to compilation. 
`include file                     // Insert another file as part of the current file.  
`ifdef cond                       // If cond is defined, compile the following. `else 
`endif
```

### 8. operators
> similar to c operators

### 9. Structed Procedures
1. initial
- 시뮬레이션을 시작하기 위한 구문
- 시작시 timer가 0으로 초기화
2. always @
- @ 뒤에 괄호를 사용해 조건을 단다.
- 조건에 따라 event가 계속 실행된다.

### 10. Sequential & Parallel
1. Sequential
- begin과 end를 통해 실행 된다.
2. Parallel
- fork와 join을 사용하여 실행 된다.

### 11. Assignments
1. Continuous
- 연속 절차 지향
2. Procedural
- 절차지향
- Blocking
  - = 사용하여 대입
  - 절차대로 진행
- non-Blocking
  - <= 사용하여 대입
  - 절차 무시하고 대입 (쓰레기 값, 존재 유무 판단하지 않음)
3. quasi-continuous
- active 상태와 deactive 상태가 있다.
```
begin 
   ... 
   assign register = expression1;   // Activate quasi-continuous 
   ...    register = expression2;   // No effect.  Overridden by active 
                                    //   quasi-continuous      
   ... 
   assign register = expression3;   // Becomes active and overrides  
                                    //  previous quasi-continuous 
   ... 
   deassign register;               // Disable quasi-continuous 
   ... 
   register = expression4;          // Executed.      
   ... 
 end 
```

### 12. timing controls
