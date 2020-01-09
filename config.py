import numpy as np

class Config(object):
    '''定义一些计算中的设置, 比如数值的类型等一些不变的量'''
    __dtype = np.float32
    __available_dtypes = (np.float16, np.float32, np.float64)

    @property
    def dtype(self):
        return self.__dtype

    @dtype.setter
    def dtype(self,dtype):
        if dtype in self.__available_dtypes:
            self.__dtype = dtype
        else:
            raise ValueError('This data type is not allowed!')
        
config = Config()
config.dtype = np.float128

print(config.dtype)
