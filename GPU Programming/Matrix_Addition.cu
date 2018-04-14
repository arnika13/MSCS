#include <stdio.h>
#include <stdlib.h>
#include "../common/book.h"
#include <cuda.h>

#define M 3
#define N 3

/*----Defining kernel function matrixAdd which takes 3 arguments A,B,C these are matrix of 3*3 A & B are input matrix and matrix C is the sum of A & B--------*/

__global__ void matrixAdd(float *A, float *B, float *C) 
{
	int index = threadIdx.x + blockDim.x * blockIdx.x;

	/*The sum of matrix A & B is stored in C*/

	C[index] = A[index] + B[index];

	//printf("ThreadIdx.x : %d\tblockDim.x : %d\tblockIdx.x : %d ThreadIdx.y : %d\tblockDim.y : %d\tblockIdx.y : %d index: %d\n", threadIdx.x, blockDim.x, blockIdx.x, threadIdx.y, blockDim.y, blockIdx.y, index);

}


int main() {

	float A[M][N], B[M][N], C[M][N]; /*Declaring matrix A & B of size M*N */
	int i, j;
	float *dev_a, *dev_b, *dev_c;

	/*--------Taking user input for matrix A elements----------*/

	printf("\n Enter elements of first matrix A of size %d * %d\n", M, N);
	for(i = 0; i<M; i++) // i is representing row of matrix 
	{
		for(j = 0; j<N; j++) // j is representing column of matrix 
		{
			printf("Enter the element A[%d][%d] : ", i, j);
			scanf("%f", &A[i][j]);
		}
	}


	/*--------Taking user input for matrix B elements----------*/

	printf("\n Enter elements of second matrix B of size %d * %d\n", M, N);
	for(i = 0; i<M; i++)
	{
		for(j = 0; j<N; j++)
		{
			printf("Enter the element B[%d][%d] : ", i, j);
			scanf("%f", &B[i][j]);
		}
	}
	/*--------Allocating memory in GPU by using cudaMalloc----------*/

	cudaMalloc((void**)&dev_a, (M*N) * sizeof(float));
	cudaMalloc((void**)&dev_b, (M*N) * sizeof(float));
	cudaMalloc((void**)&dev_c, (M*N) * sizeof(float));

	/*--------Copying elements of 2D matrix A, B from host(CPU) to device(GPU) by using cudaMemcpy----------*/

	cudaMemcpy(dev_a, A, (M*N) * sizeof(float), cudaMemcpyHostToDevice);
	cudaMemcpy(dev_b, B, (M*N) * sizeof(float), cudaMemcpyHostToDevice);
	cudaMemcpy(dev_c, C, (M*N) * sizeof(float), cudaMemcpyHostToDevice);

	/*---------Calling kernel function-------------*/

	matrixAdd << < M, N >> >(dev_a, dev_b, dev_c); //  Calling kernel function with 3 block and 3 threads per block

	cudaThreadSynchronize(); // Synchronizing CPU with GPU

							 /*-------- After the GPU kernel function executes it copies the result stored in device to host i.e CPU */

	cudaMemcpy(C, dev_c, (M*N) * sizeof(float), cudaMemcpyDeviceToHost);

	/*-----------Printing the addition of two matrix A & B---------------*/
	printf("\n");
	printf("Sum of two matrix A & B :\n\n");

	for(i = 0; i<M; i++)
	{
		for(j = 0; j<N; j++)
		{
			printf("%.2f\t\t", C[i][j]);
		}
		printf("\n\n");
	}

	// Free the memory allocated in GPU

	cudaFree(dev_a);
	cudaFree(dev_b);
	cudaFree(dev_c);

	return 0;
}