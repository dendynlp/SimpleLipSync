#include "SimpleLipSync.h"
#include "SimpleLipSyncInterface.h"
 
SIMPLE_LIP_SYNC_EXPORTS_API void voice2bs(float* input_value, int input_len, float* ret_bs)
{
	SimpleLipSyncImplInst->voice2bs(input_value,input_len, ret_bs);
}
SIMPLE_LIP_SYNC_EXPORTS_API void init_model(const char* base_path)
{
	SimpleLipSync::init_model(base_path);
}