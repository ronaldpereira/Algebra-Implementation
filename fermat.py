# Para interpretar e executar o programa, basta digitar no Terminal do Linux : python tp1.py
# -*- coding: utf-8 -*-

import math

print '\nAlgebra A - 2015/2\n\nTrabalho Pratico - Parte 1\n\nAutor: Ronald Davi Rodrigues Pereira - 2015004437\n\nMétodo de Fermat para achar fatores de um número de Mersenne\n\n'

i = 0

for p in xrange(2, 258):
	aux = 0
	for j in xrange(2, p):
		if p % j == 0:
			aux += 1
	if aux == 0:
		print '-----------------------------------------\np = %d\n'%p
		limite_r = (math.sqrt(2**p)-1)/(2*p)
		parada = int(limite_r)
		aux_2 = 0
		r = 0
		while 1:
			if r > parada and aux_2 == 0:
				print 'p = %d faz com que M(%d)=%d seja primo.\n'%(p,p,(2**p)-1)
			if r > parada:
				break
			if aux_2 == 1:
				print 'p = %d faz com que M(%d)=%d NAO seja primo.\n'%(p,p,(2**p)-1)
				break

			E = p
			A = 2
			P = 1
			q = r * 2 * p + 1

			while 1:
				if E == 0:
					if P == 1:
						print '2^%d é equivalente a %d (mod %d)\n'%(p,P,q)
						aux_2 = 1
					break
				else:
					if E % 2 == 1:
						P = (A * P)%q
						E = (E - 1)/2
					else:
						E = E / 2
					A = (A**2)%q
			r+=1
