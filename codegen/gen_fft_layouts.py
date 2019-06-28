
# This file contains layout definitions. Edit this file to add custom layouts.
# Do not add other logic or call functions in gen_fft_generators.py from this file.

from gen_fft_modules import *

#fft2_scale_none = FFTBase(2, 'fft2_serial2', 'SCALE_NONE', 3)
#fft2_scale_div_n = FFTBase(2, 'fft2_serial2', 'SCALE_DIV_N', 3)

fft2_scale_none = FFTBase(2, 'fft2_serial', 'SCALE_NONE', 6)
fft2_scale_div_n = FFTBase(2, 'fft2_serial', 'SCALE_DIV_N', 6)


#fft4_scale_none = FFT3Step(4, fft2_scale_none, fft2_scale_none);
#fft4_scale_div_sqrt_n = FFT3Step(4, fft2_scale_none, fft2_scale_div_n);
#fft4_scale_div_n = FFT3Step(4, fft2_scale_div_n, fft2_scale_div_n);


fft4_delay = 10
#fft4_large_scale_none = FFTBase(4, 'fft4_serial3', 'SCALE_NONE', fft4_delay)
fft4_large_scale_div_sqrt_n = FFTBase(4, 'fft4_serial3', 'SCALE_DIV_SQRT_N', fft4_delay)
#fft4_large_scale_div_n = FFTBase(4, 'fft4_serial3', 'SCALE_DIV_N', fft4_delay)


#fft4_delay = 12
#fft4_scale_none = FFTBase(4, 'fft4_serial4', 'SCALE_NONE', fft4_delay)
#fft4_scale_div_n = FFTBase(4, 'fft4_serial4', 'SCALE_DIV_N', fft4_delay)



fft4_delay = 11
fft4_entity = 'fft4_serial7'
fft4_scale_none = FFTBase(4, fft4_entity, 'SCALE_NONE', fft4_delay)
fft4_scale_div_sqrt_n = FFTBase(4, fft4_entity, 'SCALE_DIV_SQRT_N', fft4_delay)
fft4_scale_div_n = FFTBase(4, fft4_entity, 'SCALE_DIV_N', fft4_delay)
fft4_scale_none.setOutputBitOrder([1,0])
fft4_scale_div_sqrt_n.setOutputBitOrder([1,0])
fft4_scale_div_n.setOutputBitOrder([1,0])


fft16 = \
	FFT3Step(16, 
		fft4_scale_none,
		fft4_scale_div_n);

fft16_scale_none = FFT3Step(16,  fft4_scale_none, fft4_scale_none);
fft16_scale_div_n = FFT3Step(16,  fft4_scale_div_n, fft4_scale_div_n);

# scales by 1/4. 32 is not a perfect square so 1/sqrt(n) is not possible
fft32 = \
	FFT3Step(32,
		FFT3Step(8, 
			fft4_scale_none,
			fft2_scale_none),
		fft4_scale_div_n);

fft64 = \
	FFT3Step(64,
		FFT3Step(16, 
			fft4_scale_none,
			fft4_large_scale_div_sqrt_n),
		fft4_scale_div_n);


fft64_scale_none = FFT3Step(64, fft16_scale_none, fft4_scale_none);
fft64_scale_div_n = FFT3Step(64, fft16_scale_div_n, fft4_scale_div_n);




fft256 = \
	FFT3Step(256,
		FFT3Step(16, 
			fft4_scale_none,
			fft4_scale_none),
		FFT3Step(16, 
			fft4_scale_div_n,
			fft4_scale_div_n));
fft256.setOptionsRecursive(True, True)


fft1024 = \
	FFT3Step(1024,
		FFT3Step(64,
			FFT3Step(16, 
				fft4_scale_none,
				fft4_scale_none),
			fft4_large_scale_div_sqrt_n),
		FFT3Step(16, 
			fft4_scale_div_n,
			fft4_scale_div_n));

fft1024_wide = \
	FFT3Step(1024,
		FFT3Step(64,
			FFT3Step(16, 
				fft4_scale_none,
				fft4_scale_none),
			fft4_scale_div_sqrt_n),
		FFT3Step(16, 
			fft4_scale_div_n,
			fft4_scale_div_n));

fft1024_wide.setOptionsRecursive(rnd=True, largeMultiplier=True)

fft1024_2 = \
	FFT3Step(1024,
		FFT3Step(256,
			FFT3Step(16, 
				fft4_scale_none,
				fft4_scale_none),
			FFT3Step(16, 
				fft4_large_scale_div_sqrt_n,
				fft4_scale_div_n)),
		fft4_scale_div_n);




fft4096 = \
	FFT3Step(4096,
		FFT3Step(64,
			FFT3Step(16,  fft4_scale_none, fft4_scale_none),
			fft4_scale_none),
		FFT3Step(64, 
			FFT3Step(16,  fft4_scale_div_n, fft4_scale_div_n),
			fft4_scale_div_n));

fft8192 = \
	FFT3Step(8192,
		FFT3Step(128,
			FFT3Step(16,  fft4_scale_none, fft4_scale_none),
			FFT3Step(8,  fft4_scale_none, fft2_scale_div_n)),
		FFT3Step(64, 
			FFT3Step(16,  fft4_scale_div_n, fft4_scale_div_n),
			fft4_scale_div_n));

fft8192_wide = \
	FFT3Step(8192,
		FFT3Step(128,
			FFT3Step(16,  fft4_scale_none, fft4_scale_none),
			FFT3Step(8,  fft4_scale_none, fft2_scale_div_n)),
		FFT3Step(64, 
			FFT3Step(16,  fft4_scale_div_n, fft4_scale_div_n),
			fft4_scale_div_n));
fft8192_wide.setOptionsRecursive(rnd=True, largeMultiplier=True)


fft16k = \
	FFT3Step(16*1024,
		FFT3Step(4096,
			FFT3Step(64,
				FFT3Step(16,
					fft4_scale_none,
					fft4_scale_none),
				fft4_scale_none),
			FFT3Step(64, 
				FFT3Step(16,
					fft4_large_scale_div_sqrt_n,
					fft4_scale_div_n),
				fft4_scale_div_n)),
		fft4_scale_div_n);

fft16k_2 = \
	FFT3Step(16*1024,
		FFT3Step(128,
			FFT3Step(16,  fft4_scale_none, fft4_scale_none),
			FFT3Step(8,  fft4_scale_none, fft2_scale_none)),
		FFT3Step(128,
			FFT3Step(16,  fft4_scale_div_n, fft4_scale_div_n),
			FFT3Step(8,  fft4_scale_div_n, fft2_scale_div_n)));

fft32k = \
	FFT3Step(32*1024,
		FFT3Step(256,
			FFT3Step(16,  fft4_scale_none, fft4_scale_none),
			FFT3Step(16,  fft4_scale_none, fft4_scale_div_sqrt_n)),
		FFT3Step(128,
			FFT3Step(16,  fft4_scale_div_n, fft4_scale_div_n),
			FFT3Step(8,  fft4_scale_div_n, fft2_scale_div_n)));

fft32k_wide = \
	FFT3Step(32*1024,
		FFT3Step(256,
			FFT3Step(16,  fft4_scale_none, fft4_scale_none),
			FFT3Step(16,  fft4_scale_none, fft4_scale_div_sqrt_n)),
		FFT3Step(128,
			FFT3Step(16,  fft4_scale_div_n, fft4_scale_div_n),
			FFT3Step(8,  fft4_scale_div_n, fft2_scale_div_n)));

fft32k_wide.setOptionsRecursive(rnd=True, largeMultiplier=True)


