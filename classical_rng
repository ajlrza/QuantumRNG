import time

def mt19937_classical_rng(range):
    seed = int(time.clock_gettime(time.CLOCK_MONOTONIC_RAW))
    bit_gen = np.random.MT19937(seed=seed)
    rng = np.random.Generator(bit_gen)
    random = rng.random(range)

    return random

def pcg64_classical_rng(range):
    seed = int(time.clock_gettime(time.CLOCK_MONOTONIC_RAW))
    bit_gen = np.random.default_rng(seed=seed)
    random = bit_gen.random(range)

    return random

def philox_classical_rng(range):
    seed = int(time.clock_gettime(time.CLOCK_MONOTONIC_RAW))
    bit_gen = np.random.Philox(seed=seed)
    rng = np.random.Generator(bit_gen)
    random = rng.random(range)

    return random

def sfc64_classical_rng(range):
    seed = int(time.clock_gettime(time.CLOCK_MONOTONIC_RAW))
    bit_gen = np.random.SFC64(seed=seed)
    rng = np.random.Generator(bit_gen)
    random = rng.random(range)

    return random
    
mt19937 = mt19937_classical_rng(1)
print('====MT19937====')
print(mt19937)

pcg64 = pcg64_classical_rng(1)
print('====PCG64====')
print(pcg64)

philox = philox_classical_rng(1)
print('====Philox====')
print(philox)

sfc64 = sfc64_classical_rng(1)
print('====SFC64====')
print(sfc64)
