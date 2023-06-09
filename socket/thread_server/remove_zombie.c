#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>
#include <sys/wait.h>

void read_childproc(int sig)
{
    int status;
    pid_t id = waitpid(-1, &status, WNOHANG);
    if(WIFEXITED(status))
    {
        printf("Remove proc id : %d \n", id);
        printf("child send : %d \n", WEXITSTATUS(status));
    }
}

int main(int argc, char const *argv[])
{
    pid_t pid;
    struct sigaction act;
    act.sa_handler = read_childproc;
    sigemptyset(&act.sa_mask);
    act.sa_flags = 0;
    sigaction(SIGCHLD, &act, 0);

    pid = fork();
    if(pid == 0)
    {
        puts("Hi i am child proc");
        sleep(10);
        return 12;
    }
    else
    {
        int i;
        printf("child proc id : %d\n", pid);
        for(int i=0; i<5; i++)
        {
            puts("wait....");
            sleep(5);
        }
    }
    return 0;
}
