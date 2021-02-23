#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

void BMMultiply(int n, double **a, double **b, double **c)
{
	int bi=0;
	int bj=0;
	int bk=0;
	int i=0;
	int j=0;
	int k=0;

	int blockSize=100; 

	for(bi=0; bi<n; bi+=blockSize)
        for(bj=0; bj<n; bj+=blockSize)
            for(bk=0; bk<n; bk+=blockSize)
                for(i=0; i<blockSize; i++)
                    for(j=0; j<blockSize; j++)
                        for(k=0; k<blockSize; k++)
                            c[bi+i][bj+j] += a[bi+i][bk+k]*b[bk+k][bj+j];
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

	printf("Multiply Matrix for Task 3 Bonus with %d reps linear matrices...\n", numreps);
	for (r = 0; r < numreps; ++r) {
		gettimeofday(&tv1, &tz);
		BMMultiply(n,A,B,C);
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
