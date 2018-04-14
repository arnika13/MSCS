#include <stdio.h>
#include <stdlib.h>
#include"../common/book.h"
#include <cuda.h>
#include <cuda_runtime.h>
#include<math.h>

#define N 3

/*Defining kernel function matrix multiplication which takes 3 arguments A,B,C these are matrix of 3*3 A & B are input matrix and matrix C is the product of A & B */

__global__ void matrixMult(float *A, float *B, float *C) 
{
	float Sum_Matrix = 0;
	int row = threadIdx.y + blockDim.y * blockIdx.y; // row represents the indices of matrix A
	int col = threadIdx.x + blockDim.x * blockIdx.x; // col represents the indices of matrix B 
	//printf("ThreadIdx.x : %d\tblockDim.x : %d\tblockIdx.x : %d\tThreadIdx.y : %d\tblockDim.y : %d\tblockIdx.y :%d\t\n", threadIdx.x, blockDim.x, blockIdx.x, threadIdx.y, blockDim.y, blockIdx.y);
	
	int index = row * N + col;
	//printf("Index = %d\n",index);
	if (row < N && col < N)
	{
		// each thread computes one element of the block sub- matrix
		for (int i = 0; i < N; ++i) 
		{
			Sum_Matrix += A[i + row * N] * B[col + i * N];
		}
	}
	C[index] = Sum_Matrix;
}


int main() 
{
	/*Declaring matrix A & B of size N*N */
	float A[N][N], B[N][N], C[N][N]; 
	int i, j; // Declaring i for row and j for column of matrix

	/* creating three 2D arrays  */
	float *dev_a, *dev_b, *dev_c; 

	/*--------Taking user input for matrix A elements----------*/
	printf("\n Enter elements of first matrix A of size %d * %d\n", N, N);
	for(i = 0; i<N; i++) // i is representing row of matrix A
	{
		for(j = 0; j<N; j++) // j is representing column of matrix A
		{
			printf("Enter the element A[%d][%d] : ", i, j);
			scanf("%f", &A[i][j]);
		}
	}

	/*--------Taking user input for matrix B elements----------*/
	printf("\n Enter elements of second matrix B of size %d * %d\n", N, N);
	for(i = 0; i<N; i++) // i is representing row of matrix B
	{
		for(j = 0; j<N; j++) // j is representing column of matrix B
		{
			printf("Enter the element B[%d][%d] : ", i, j);
			scanf("%f", &B[i][j]);
		}
	
	}
	/*--------Allocating memory in GPU by using cudaMalloc----------*/

	cudaMalloc((void**)&dev_a, (N*N) * sizeof(float));
	cudaMalloc((void**)&dev_b, (N*N) * sizeof(float));
	cudaMalloc((void**)&dev_c, (N*N) * sizeof(float));

	/*--------Copying elements of 2D array A, B from host(CPU) to device(GPU) by using cudaMemcpy----------*/

	cudaMemcpy(dev_a, A, (N*N) * sizeof(float), cudaMemcpyHostToDevice);
	cudaMemcpy(dev_b, B, (N*N) * sizeof(float), cudaMemcpyHostToDevice);
	cudaMemcpy(dev_c, C, (N*N) * sizeof(float), cudaMemcpyHostToDevice);

	/*---------Calling kernel function-------------*/
	dim3 blocksPerGrid(1, 1); // Number of blocks is 1
	dim3 threadsPerBlock(N, N); // Number of threadsPerBlock is 9 (3*3)
	matrixMult<<< blocksPerGrid,threadsPerBlock >>>(dev_a, dev_b, dev_c); // Calling kernel function with 1 block and 9 threads per block
	cudaThreadSynchronize(); // synchronizing CPU with GPU

	/*-------- After the GPU kernel function executes it copies the 2D array back from GPU to CPU ----------------*/

	cudaMemcpy(C, dev_c, (N*N) * sizeof(float), cudaMemcpyDeviceToHost);

	/*-----------------printing the product of two matrix A & B --------------------*/

	printf("\n");
	printf("Product of two matrix A and B is :\n\n ");

	for(i = 0; i<N; i++)
	{
		for(j = 0; j<N; j++)
		{
			printf("%.2f\t\t", C[i][j]);
		}
		printf("\n");
	}

	// Free the memory allocated in GPU
	cudaFree(dev_a); 
	cudaFree(dev_b);
	cudaFree(dev_c);

	return 0;
}
