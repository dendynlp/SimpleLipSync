#pragma once
#ifndef SIMPLE_LIP_SYNC_INTERFACE_H
#define SIMPLE_LIP_SYNC_INTERFACE_H
#include "SimpleLipSyncDef.h"
#include <vector>
#include<string>
SIMPLE_LIP_SYNC_EXPORTS_API void voice2bs(float* input_value, int input_len, float* ret_bs);
SIMPLE_LIP_SYNC_EXPORTS_API void init_model(const char* base_path);
#endif //SIMPLE_LIP_SYNC_INTERFACE_H