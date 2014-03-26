"""def mod_num(n):
	mstart = (n-7) % 32
	if mstart == 0:
		return n
	if mstart <= 8:
		return (n + (8 - mstart))
	if mstart <= 16:
		return (n + (16 - mstart))
	if mstart <= 20:
		return (n + (20 - mstart))
	if mstart <= 24:
		return (n + (24 - mstart))
#	if mstart < 32: 				#can just assume it's less than 32, so skip the if statement.
	return (n + (32 - mstart))
#No longer needed now that we don't deal with any integers below Level 2 outside of collatz."""
