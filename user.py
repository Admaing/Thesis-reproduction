#! usr/bin/env python3
# -*- coding: utf-8 -*-

from glob import glob1
from telnetlib import EL
from xml.dom.minidom import Element
from pypbc import *
import hashlib
# from BloomFilter import *
# from TimeCount import *

#   system params generation
#   q_1 * q_2 = n, n is the order of the group

q_1 = get_random_prime(160)
q_2 = get_random_prime(160)


params = Parameters( n = q_1 * q_2 )    #   使用的是pbc中的a1_param参数，详见pbc_manul手册中的说明
pairing = Pairing( params )

print(params)
print(pairing)
# #   print(params)

# #   生成g,u,和h，参考e-Finga的论文。
g = Element.random( pairing, G1 )
u = Element.random( pairing, G1 ) #全局常量
# h = Element( pairing, G2, value = u **q_2 )a

# SB = Element( pairing, G2, value = g ** q_1 )

# PB = Element( pairing, GT )
# PB = pairing.apply( g, g )
# PB = Element( pairing, GT, value = PB ** q_1 )

# #   哈希就在这凑合一下吧，是那么个意思，对效率的影响不大，等以后有时间了再加进来吧。
hash1 = hashlib.sha256
hash2 =  hashlib.sha256
h =  hashlib.sha256

x = Element.random( pairing, G1 )  #用户uj选择随机数Xj
#使用随机数计算私钥
  
# Tj是啥玩意     每个用户的管理属性Tj定义为32bit



def KeyGen(j):

    for i in j:

        Tj = "12333333333333333333333333333123123123123123113123"
        Xj = x * h(int(Tj)) #私钥
        Yj = Element( paring, G1, value = g**Xj)    #公钥

        tj = Element(paring, G1, value = Tj+Tj**Xj)



def SigGen(name, F,X,Y):
    mi = F
    mi = Element.random( pairing, Zr)
    TagF = hash(mi) #出问题
    id = name+1+hash2(mi+1)
    u_m = Element(paring, G1, value=u**mi)
    tao = Element(paring, G1, value=(hash1(id)*u_m)**X)

    return F,TagF, tao

def ReKeygen(X,Y):
    return Elment(paring, G1, value = Y**(1/X))

# def ReSiggen(k)
if __name__ == "__main__":
    


# #   构造布隆过滤器，这个可是费老劲了！
# Delta_d = 20
# BF = BloomFilter( 8, 65536 )
# Delta_d_2 = Delta_d * Delta_d
# for i in range( Delta_d_2 + 1 ) :
#     i_value = Element( pairing, Zr, value = i )
#     BF.insert( Element( pairing, GT, value = PB ** i_value ) )

# #   Template Generation，细节看论文。
# def Template_Gen( BioCode ) :
#     n = len( BioCode )
#     x = []
#     r = []
#     for i in range( n ) :
#         x.append( Element( pairing, Zr, value = Element( pairing, Zr, value = BioCode[i] ) + hash_value ) )
#         r.append( Element.random( pairing, Zr ) )
#     f_x = []
#     for i in range( n ) :
#         f_x.append( Element( pairing, G2, value = (g**x[i])*(h**r[i]) ) )
#     temp1 = Element.zero( pairing, Zr )
#     for i in range( n ) :
#         temp1 = Element( pairing, Zr, value = temp1 + x[i]**2 )
#     f_x_PB = Element( pairing, GT, value = PB ** (-temp1) )     #   这里说明一下，才疏学浅，就用负的幂来代替后面的除了，不知道GT群上咋求逆，反正结果是一样的。
#     T_u = ( f_x, f_x_PB )
#     return T_u

# #   Query Generation
# def Query_Gen( BioCode ) :
#     n = len( BioCode )
#     y = []
#     for i in range( n ) :
#         y.append( Element( pairing, Zr, value = Element( pairing, Zr, value = BioCode[i] ) + hash_value ) )
#     q_y = []
#     for i in range( n ) :
#         temp = Element( pairing, Zr, value = y[i] + y[i] )
#         q_y.append( SB ** temp )
#     temp1 = Element.zero( pairing, Zr )
#     for i in range( n ) :
#         temp1 = Element( pairing, Zr, value = temp1 + y[i]**2 )
#     temp1 = Element( pairing, Zr, value = Element( pairing, Zr, value = Delta_d_2 ) - temp1 )   #   同上，结果一样，暂时不深入研究了。
#     q_y_PB = Element( pairing, GT, value = PB ** temp1 )
#     Q_u = ( q_y, q_y_PB )
#     return Q_u

# #   Match data
# def Match_Data( T_u, Q_u ) :
#     f_x = T_u[0]
#     f_x_PB = T_u[1]
#     q_y = Q_u[0]
#     q_y_PB = Q_u[1]
#     n = len( f_x )

#     #   感觉这个e_list的说法怪怪的，感觉应该是这么用。
#     e_list = []
#     for i in range( n ) :
#         e_list.append( Element( pairing, GT ) )
#     for i in range( n ) :
#         e_list[i] = pairing.apply( f_x[i], q_y[i] )
#     up_value= Element.one( pairing, GT )
#     for i in range( n ) :
#         up_value = Element( pairing, GT, value = up_value * e_list[i] )
#     down_value = Element( pairing, GT, value = f_x_PB * q_y_PB )
#     M_d = Element( pairing, GT, value = up_value * down_value)
#     return M_d

# #   Test Fuction，小小的设计一下测试。
# def test( dims, times ) :

#     t_TG = timing( Template_Gen, 1 )
#     t_QG = timing( Query_Gen, 1 )
#     t_MD = timing( Match_Data, 1 )

#     clocktime_TG_sum = 0
#     clocktime_QG_sum = 0
#     clocktime_MD_sum = 0

#     Result_list = []

#     for i in range( times ) :
#         #   尽可能的减少人为的因素，BioCode码是随机的。
#         BC_1 = []
#         for i in range( dims ) :
#             BC_1.append( get_random(255) )
#         #   加一些扰乱因子，算是每次采集信息会有一点点不同的样子，但好像又有一点点小问题，也没有想像中的那么美好。
#         BC_2 = []
#         for i in range( dims ) :
#             BC_2.append( BC_1[i] + get_random( 3 ) )
#         T_u, clocktime_TG = t_TG( BC_1 )
#         clocktime_TG_sum += clocktime_TG
#         Q_u, clocktime_QG = t_QG( BC_2 )
#         clocktime_QG_sum += clocktime_QG
#         M_d, clocktime_MD = t_MD( T_u, Q_u )
#         clocktime_MD_sum += clocktime_MD
#         Result_list.append( BF.is_exist( M_d ) )
#     return ( clocktime_TG_sum, clocktime_QG_sum, clocktime_MD_sum, Result_list )


# if __name__ == "__main__":

#     test_1 = test( 2, 5 )
#     print( test_1[0] )
#     print( test_1[1] )
#     print( test_1[2] )
# #    print( test_1[3] )
