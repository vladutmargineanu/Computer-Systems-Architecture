#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

void multiplyTask2(int n, double **a, double **b, double **c)
{
	int i = 0;
	int j = 0;
	int k = 0;
	int sum;

	for (i = 0; i < n; i++){
   		for (j = 0; j < n; j++){
      		sum = 0;
      		for (k = 0;k < n; k++)
         		sum += a[i][k] * b[k][j];
      		c[i][j] = sum; 
   		}
	}
}

int main(void)
{
	int n;
	double** A;
	double** B;
	double** C;
	int i;
	int j;
	int k;
	int r;
	int numreps = 10;
	struct timeval tv1, tv2;
	struct timezone tz;
	double elapsed;

	n = 500;

	A = (double **)malloc(n * sizeof(double *));
	for (int i = 0; i < n; i++) {
		A[i] = (double *)malloc(n * sizeof(double));
	}
	
	B = (double **)malloc(n * sizeof(double *));
	for (int i = 0; i < n; i++) {
		B[i] = (double *)malloc(n * sizeof(double));
	}
	
	C = (double **)malloc(n * sizeof(double *));
	for (int i = 0; i < n; i++) {
		C[i] = (double *)malloc(n * sizeof(double));
	}
	
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			A[i][j] = 1;
			B[i][j] = 2;
		}
	}

	printf("Multiply Matrix for Task 2 Bonus with %d reps linear matrices...\n", numreps);
	for (r = 0; r < numreps; ++r) {
		gettimeofday(&tv1, &tz);
		multiplyTask2(n,A,B,C);
		gettimeofday(&tv2, &tz);
		elapsed += (double) (tv2.tv_sec-tv1.tv_sec) + (double) (tv2.tv_usec-tv1.tv_usec) * 1.e-6;
	}
	printf("Time = %lf \n",elapsed);

	for (int i = 0; i < n; i++) {
		free(A[i]);
	}
	free(A);

	for (int i = 0; i < n; i++) {
		free(B[i]);
	}
	free(B);

	for (int i = 0; i < n; i++) {
		free(C[i]);
	}
	free(C);
	
	return 0;
}
