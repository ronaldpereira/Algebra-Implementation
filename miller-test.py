# Para interpretar e executar o programa, basta digitar no Terminal do Linux : python miller-test.py
# -*- coding: utf-8 -*-

from random import randint
print '\nAlgebra A - 2015/2\n\nTrabalho Pratico - Parte 2 Exercicio 3\n\nAutor: Ronald Davi Rodrigues Pereira - 2015004437\n\nAplicacao do Teste de Miller\n\n'

r = randint(524288, 1048575) # 524288 = 10000000000000000000 (min 20 bits) e 1048575 = 11111111111111111111 (max 20 bits)
s = randint(524288, 1048575)

print '\nNumeros primos gerados : r = %d s = %d'%(r,s)

print '\nVerificação dos numeros "r" e "s" da divisibilidade por um primo menor que 5000:\n'

for i in xrange (2, 5000):
	aux = 0
	for j in xrange(2, i):
		if i % j == 0 :
			aux += 1
	if aux == 0 :
		if r % i == 0 :
			print 'O numero %d é divisivel por %d\n'%(r, i)

for i in xrange (2, 5000):
	aux = 0
	for j in xrange(2, i):
		if i % j == 0 :
			aux += 1
	if aux == 0 :
		if s % i == 0 :
			print 'O numero %d é divisivel por %d\n'%(s, i)

print '\nAplicacao do teste de Miller em "r" e "s" usando como base os 10 primeiros primos\n'

# Para evitar gasto desnecessário de tempo do programa, já gerei os 10 primeiros primos : 2, 3, 5, 7, 11, 13, 17, 19, 23 e 29.
i = 0
while 1:
	# Modificação da base em relação ao contador, para evitar repetições no código
	if i == 0:
		base = 2
	elif i == 1:
		base = 3
	elif i == 2:
		base = 5
	elif i == 3:
		base = 7
	elif i == 4:
		base = 11
	elif i == 5:
		base = 13
	elif i == 6:
		base = 17
	elif i == 7:
		base = 19
	elif i == 8:
		base = 23
	elif i == 9:
		base = 29
	elif i >= 10:
		break
	# Início do Teste de Miller para o número r
	print '--> Base = %d\nAplicacao para "r" = %d\n'%(base, r)
	q = r-1
	k = 0

	while q % 2 != 1:
		q /= 2
		k+=1

	print 'k = %d e q = %d\n'%(k,q)

	j = 0
	resto = (base**q)%r
	while 1:
		if j == 0 and resto == 1 or j >= 0 and resto == r-1:
			print 'Teste não conclusivo\n'
			break

		j += 1
		resto = (resto**2)%r
		if(j > k):
			print 'r = %d é composto\n'%r
			break

	# Início do Teste de Miller para o número s
	print '--> Base = %d\nAplicacao para "s" = %d\n'%(base, s)
	q = s-1
	k = 0

	while q % 2 != 1:
		q /= 2
		k+=1

	print 'k = %d e q = %d\n'%(k,q)

	j = 0
	resto = (base**q)%s
	while 1:
		if j == 0 and resto == 1 or j >= 0 and resto == s-1:
			print 'Teste não conclusivo\n'
			break

		j += 1
		resto = (resto**2)%s
		if(j > k):
			print 's = %d é composto\n'%s
			break
	# Mudança de i para que a mude a próxima base e execute o Teste com ela
	i+=1
