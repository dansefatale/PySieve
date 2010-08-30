#include <Python.h>
#include <stdio.h>
#include <msieve.h>


void get_random_seeds(uint32 *seed1, uint32 *seed2){
	FILE *rand_device = fopen("/dev/urandom", "r");

	uint32 tmp1, tmp2;
	if (rand_device != NULL){
		fread(&tmp1, sizeof(uint32), (size_t)1, rand_device);
		fread(&tmp2, sizeof(uint32), (size_t)1, rand_device);
	}

	(*seed1) = tmp1 * ((uint32)40499 * 65543);
	(*seed2) = tmp2 * ((uint32)40499 * 65543);
}

void calculate_factors(char *buf,
											 PyObject *result,
											 uint32 flags,
											 char *savefile_name,
											 char *logfile_name,
											 char *nfs_fbfile_name,
											 uint32 *seed1, uint32 *seed2,
											 uint32 max_relations,
											 uint64 nfs_lower,
											 uint64 nfs_upper,
											 enum cpu_type cpu,
											 uint32 cache_size1,
											 uint32 cache_size2,
											 uint32 num_threads,
											 uint32 mem_mb,
											 uint32 which_gpu){
	char *int_start, *last;
	msieve_obj *obj;
	msieve_factor *factor;
	msieve_obj *g_curr_factorization;

	last = strchr(buf, '\n');
	if (last)
		*last = 0;

	int_start = buf;
	while (*int_start && !isdigit(*int_start) && *int_start != '('){
		int_start++;
	}
	
	if (*int_start == 0)
		return;
	
	g_curr_factorization = msieve_obj_new(int_start, flags,
																				savefile_name, logfile_name,
																				nfs_fbfile_name,
																				*seed1, *seed2, max_relations,
																				nfs_lower, nfs_upper, cpu,
																				cache_size1, cache_size2,
																				num_threads, mem_mb, which_gpu);

	if (g_curr_factorization == NULL){
		printf("factoring failed\n");
		return;
	}
	
	msieve_run(g_curr_factorization);

	factor = g_curr_factorization->factors;

	while(factor != NULL){
		PyList_Append(result, PyString_FromString(factor->number));
		factor = factor->next;
	}
	
	/*printf("Number: %s\nFactors:\n", buf);

	while(factor != NULL){
		printf("%s\n", factor->number);
		factor = factor->next;
	}
	printf("\n");*/

	obj = g_curr_factorization;
	g_curr_factorization = NULL;
	if (obj)
		msieve_obj_free(obj);
}


static PyObject *pysieve_pysieve(PyObject *self, PyObject *args){

	uint32 seed1, seed2;
	uint32 cache_size1, cache_size2;
	char buf[400];
	enum cpu_type cpu;
	uint32 flags;
	char *savefile_name = NULL;
	char *logfile_name = NULL;
	/*	char *infile_name = "worktodo.ini";*/
	char *nfs_fbfile_name = NULL;
	/*int32 deadline = 0;*/
	uint32 max_relations = 0;
	uint64 nfs_lower = 0;
	uint64 nfs_upper = 0;
	uint32 num_threads = 0;
	uint32 mem_mb = 0;
	uint32 which_gpu = 0;

	get_cache_sizes(&cache_size1, &cache_size2);
	cpu = get_cpu_type();

	flags = MSIEVE_DEFAULT_FLAGS;
	

	get_random_seeds(&seed1, &seed2);

	const char *number;
	PyObject *result = PyList_New(0);

	if (!PyArg_ParseTuple(args, "s", &number))
		return NULL;

	strcpy(buf, number);
			
		 
	calculate_factors(buf, result,flags, 
										savefile_name,
										logfile_name, nfs_fbfile_name,
										&seed1, &seed2,
										max_relations, nfs_lower , nfs_upper,
										cpu,
										cache_size1,
										cache_size2,
										num_threads, mem_mb, which_gpu);

	return result;
			
}

PyMethodDef PySieveMethods[] = {
	{"pysieve", pysieve_pysieve, METH_VARARGS, "factor a number"},
	{NULL, NULL, 0 ,NULL}
};

PyMODINIT_FUNC initpysieve(void){
	(void) Py_InitModule("pysieve", PySieveMethods);
	
}


