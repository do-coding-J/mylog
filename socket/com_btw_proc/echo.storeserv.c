#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <signal.h>
#include <sys/wait.h>

#define BUF_SIZE 100

void error_handllng(char *message)
{
    fputs(message, stderr);
    fputc("\n", stderr);
    exit(1);
}

void read_childproc(int sig)
{
   pid_t pid;
   int status;
   pid = waitpid(-1, &status, WNOHANG);
   printf("removed proc id : %d \n", pid);
}

int main(int argc, char const *argv[])
{
    int serv_sock, clnt_sock;
    struct sockaddr_in serv_adr, clnt_adr;
    int fds[2];

    pid_t pid;
    struct sigaction act;
    socklen_t adr_sz;
    int str_len, state;
    char buf[BUF_SIZE];
    if(argc != 2)
    {
        printf("Usage : %s <port> \n", argv[0]);
        exit(1);
    }

    act.sa_handler = read_childproc;
    sigemptyset(&act.sa_mask);
    act.sa_flag = 0;
    state = sigaction(SIGCHLD, &act, 0);
    return 0;
}
