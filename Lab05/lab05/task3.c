#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

void BMMultiply(int n, double *a, double *b, double *c)
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
							c[(bi + i) * n + bj + j] += a[(bi + i) * n + bk + k]
								* b[(bk + k) * n +  bj + j];
}

int main(void)
{
	int n;
	double* A;
	double* B;
	double* C;
	int i;
	int j;
	int k;
	int r;
	int numreps = 10;
	struct timeval tv1, tv2;
	struct timezone tz;
	double elapsed;

	n = 500;

	A = malloc(n * n * sizeof(double));

	B = malloc(n * n * sizeof(double));

	C = malloc(n * n * sizeof(double));
	
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			A[i * n + j] = 1;
			B[i * n + j] = 2;
		}
	}

	printf("Blocked Multiply Matrix %d reps linear matrices...\n", numreps);
	for (r = 0; r < numreps; ++r) {
		gettimeofday(&tv1, &tz);
		BMMultiply(n,A,B,C);
		gettimeofday(&tv2, &tz);
		elapsed += (double) (tv2.tv_sec-tv1.tv_sec) + (double) (tv2.tv_usec-tv1.tv_usec) * 1.e-6;
	}
	printf("Time = %lf \n",elapsed);

	free(A);
	free(B);
	free(C);
	return 0;
}
