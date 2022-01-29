#! usr/bin/env python3
# -*- coding: utf-8 -*-

from ast import Gt
from xml.dom.minidom import Element
from pypbc import *
# from BloomFilter import *
# from TimeCount import *

#   system params generation
#   q_1 * q_2 = n, n is the order of the group

q_1 = get_random_prime(60)
q_2 = get_random_prime(60)


params = Parameters( n = q_1 * q_2 )    #   使用的是pbc中的a1_param参数，详见pbc_manul手册中的说明
pairing = Pairing( params )

# print(params)
# print(pairing)
# #   print(params)

# #   生成g,u,和h，参考e-Finga的论文。
g = Element.random( pairing, G1 )
g1 = Element(pairing,G2)
u = Element.random( pairing, G2 )
# gt = Element.random( pairing, GT)
print("G1",g)
print("g2",g1)
print("G2",u)
# print("Gt",gt)