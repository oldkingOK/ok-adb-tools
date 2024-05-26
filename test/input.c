#include <stdio.h>
#include <windows.h>

/**
 * 用于测试输入输出
 * Popen 会调用这个程序
*/
int main() {
    printf("Hi!\n");
    fflush(stdout);
    int i = 1000;
    while (i--)
    {
        printf("Hi!\n");
        fflush(stdout);
        Sleep(1000);
    }
    return 0;
}