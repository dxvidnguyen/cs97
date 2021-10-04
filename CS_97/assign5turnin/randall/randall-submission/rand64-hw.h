
/*header file rand64-hw.h */

_Bool rdrand_supported (void);
void hardware_rand64_init (void);
unsigned long long hardware_rand64 ();
unsigned long long hardware_mrand48 ();
void hardware_rand64_fini (void);
