/*
Date : 10-12-2019
Author : Keerthi
Problem : Floyd Triangle
*/

#include<stdio.h>
int main()
{
	int i,j,n,initial = 0;
	printf("Enter the size of the triangle\n");
	scanf("%d",&n);	
	for(i = 0; i <= n; i++)
	{
		for(j = 0; j <= i; j++)
		{
			printf("%d\t",++initial);//value incremented and then printed
		}
		printf("\n");
	}
 	return 0;
}
