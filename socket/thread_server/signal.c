#include <stdio.h>
#include <unistd.h>
#include <signal.h>

void timeout(int sig)
{
    if(sig == SIGALRM)
        puts("Time Out!");
    alarm(2);
}

void keycontrol(int sig)
{
    if(sig == SIGINT)
        puts("CTRL+C Pressed");
}

int main(int argc, char const *argv[])
{
    int i;
    signal(SIGALRM, timeout);
    signal(SIGINT, keycontrol);

    alarm(2);

    for(int i=0; i< 3; i++)
    {
        puts("wait...");
        sleep(10);
    }
    return 0;
}
