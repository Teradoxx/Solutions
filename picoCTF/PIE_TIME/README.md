# PIE TIME

(PIE) or Position Independent Execution is a property of executable programs.
In particular, it means that the program will function in the same way
regardless of where the operating system loads it into memory. See the
[wikipedia](https://en.wikipedia.org/wiki/Position-independent_code) page for
more details.

This executable gives us the address of the `main()` function, lets us provide
a memory address, and the program will attempt to call a function found at that
address. Because of PIE, and the random nature of where in memory the OS will
load the program, the address of the `win()` function is not constant, but
rather is at a constant offset from the `main()` function.

To find this offset, take an objdump of the binary and find the difference in
memory locations between `main()` and `win()`, and then use that offset from
the provided `main()` function address to call the `win()` function.

```shell
objdump -d vuln >> objdump.txt
```
