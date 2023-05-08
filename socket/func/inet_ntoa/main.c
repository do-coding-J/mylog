#include <stdio.h>
#include <string.h>
#include <arpa/inet.h>

int main(int argc, char *argv[])
{
   struct sockaddr_in addr1, addr2;
   char *str_ptr;
   char str_arr[20];

   addr1.sin_addr.s_addr = htonl(0x1020304);  // htonl : 호스트 주소를 네트워크 타입으로 가져옴
   addr2.sin_addr.s_addr = htonl(0x1010101);

   str_ptr = inet_ntoa(addr1.sin_addr);   // ntoa 함수 호출
   strcpy(str_arr, str_ptr);              // 함수를 또 호출할꺼라서 다른 메모리에 기존의 문자열 복사
   printf("Dotted-Decimal notation1 :%s \n", str_ptr);

   inet_ntoa(addr2.sin_addr);             // ntoa 함수 호출
   printf("Dotted-Decimal notation2 :%s \n", str_ptr);
   printf("Dotted-Decimal notation3 :%s \n", str_ptr);
   return 0;
}