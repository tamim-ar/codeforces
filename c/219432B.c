#include <stdio.h>

int main()
{
    int N, i, count = 0;
    scanf("%d", &N);

    for (i = 1; i <= N; i++)
    {
        if (1 <= N <= 1000)
        {
            if (i % 2 == 0)
            {
                count = count + 1;
                printf("%d\n", i);
            }
        }
    }
    if (count <= 1)
    {
        printf("-1\n");
    }

    return 0;
}
