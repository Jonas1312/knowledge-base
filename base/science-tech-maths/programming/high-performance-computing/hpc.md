# High Performance Computing

## Better use cache

Normally cache memory is split into instruction cache memory and data cache memory. The purpose of the first is to speed up access to instructions and the purpose of the second is to speed up access to data used by instructions.

There are two principles that govern the behavior of the real world programs:

1. The first is called temporal locality and it essentially means that if the processor is currently accessing a certain memory address, there is a high probability it will access the same memory address in the near future (think a counter in a loop).
2. The second is called spatial locality and what it means is that if the processor is currently accessing a certain memory address, there is a high probability it will access neighboring memory addresses in the near future (think running through arrays).

Cache memory is divided into cache lines and in modern processors each cache line can typically hold 64 bytes of data. One cache line corresponds to one 64 bytes block in the main memory. Access to one byte within a 64 bytes memory block means that the whole 64 bytes memory block will be loaded into the cache line. When the block is fetched into the cache line, a mapping is created between the cache line and the original memory block.

To improve performance, store your data in a contiguous block of memory. This will improve spatial locality and will result in fewer cache misses.

All writes to memory go through the data cache3. When a write is made, the cache marks that cache line as “dirty”. If a cache line is dirty, that means that it is different from the content of the memory and sooner or later its content will have to me written back to memory.

## More

- <https://queue.acm.org/detail.cfm?id=3372264>
- <https://stackoverflow.blog/2020/07/08/improving-performance-with-simd-intrinsics-in-three-use-cases/>
- <https://blog.cr.yp.to/20190430-vectorize.html>
- <https://gist.github.com/nadavrot/5b35d44e8ba3dd718e595e40184d03f0> High-Performance Matrix Multiplication
- <https://viralinstruction.com/posts/hardware/>
<https://codeconfessions.substack.com/p/gpu-computing>
<https://towardsdatascience.com/matrix-multiplication-on-the-gpu-e920e50207a8>
