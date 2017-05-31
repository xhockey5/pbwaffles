#include<stdio.h>

int func1(char *a, int b, float c)
{
    char string = "This is not the flag";
    int result;
    result = b + 10;
    for(int i=0; i < 100; i++)
    {
        result += i;
    }
    return result;
}


void main()
{
    char *a;
    int b = 555;
    float c;
    int d;

    d = func1(a, b, c);
    printf("FLAG:{g3QzCvmT}");
}
