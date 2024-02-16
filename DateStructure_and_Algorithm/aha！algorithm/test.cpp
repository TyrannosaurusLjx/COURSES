#include <stdio.h>
#include <stdlib.h>
int main()
{
    int *p; //定义一个指针p
    p=(int *)malloc(sizeof(int)); //指针p获取动态分配的内存空间地址
    *p=10; //向指针p所指向的内存空间中存入10
    printf("%d",*p); //输出指针p所指向的内存中的值
    getchar();getchar();
    return 0;
}
