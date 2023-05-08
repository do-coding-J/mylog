#include <stdio.h>
#include <arpa/inet.h>

int main(int argc, char *argv[])
{
   char *addr1 = "1.2.3.4";
   char *addr2 = "1.2.3.256"; // 255까지인데 256으로 바이트 범위를 넘어서 에러뜰것임

   unsigned long conv_addr = inet_addr(addr1);
   if(conv_addr == INADDR_NONE)
      printf("Error ouccured! \n");
   else
      printf("Network ordered integer addr : %#lx \n", conv_addr);


   conv_addr = inet_addr(addr2);
   if(conv_addr == INADDR_NONE)
      printf("Error ouccured! \n");
   else
      printf("Network ordered integer addr : %#lx \n", conv_addr);

   return 0;
}