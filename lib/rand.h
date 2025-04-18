#ifndef _ALGORITHM
#define _ALGORITHM
#include <algorithm>
#endif

template<typename Type>
inline Type int_rand_in_range(Type _Begin, Type _End) {
    srand(time(0));
    return rand() % (_End - _Begin + 1) + _Begin;
}