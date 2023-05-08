#include <stdio.h>
#include <arpa/inet.h>

int main(int argc, char *argv[])
{
    unsigned short host_port = 0x1234;
    unsigned short net_port;
    unsigned long host_addr = 0x12345678;
    unsigned long net_addr;

    net_port = htons(host_port);
    net_addr = htonl(host_addr);

    printf("Host ordered port : %#x \n", host_port);
    printf("Network ordered port : %#x \n", net_port);
    printf("Host ordered address : %#lx \n", host_addr);
    printf("Network ordered address : %#lx \n", net_addr);
    return 0;

}
/*
출력 값이 다를 경우 리틀 엔디안
출력 값이 같을 경우 빅 엔디안

CPU의 저장 체계에 따라 다름, 네트워크는 빅 엔디안으로 통일
*/