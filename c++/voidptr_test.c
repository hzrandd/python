#include<stdio.h>

int main(){
    int a=1;
    int *ptr = &a;
    *ptr = 10;
    printf("a=%d\n",a);
    void *q = &a;
//    *q=100;
    printf("a=%d\n",a);

    printf("sizeof(*q)=%ld, sizeof(char)=%ld\n", sizeof(*q),sizeof(char));
    return 0;
}
