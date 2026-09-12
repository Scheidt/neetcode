get, set, popback and getSize are O(1). pushback is O(1) amortized, being O(1) in the common case, but triggers an O(n) resize when the buffer is full.

I deliberately avoided list.append and other dynamic-list features, treating the underlying list as a fixed-size buffer, the equivalent of a malloc'd block in C.