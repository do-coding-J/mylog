#include <stdio.h>
#include <unistd.h>

int main(int argc, char const *argv[])
{
    __pid_t pid = fork();

    if(pid == 0) // child
        puts("Hi, this is Child process");
    else 
    {
        // puts("Hi, this is Parent process");
        printf("Child process ID : %d \n", pid);
        sleep(10);
    }

    if(pid == 0)
        puts("End Child Process");
    else
        puts("End Parent Process");

    return 0;
}
