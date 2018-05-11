# -*- coding: utf-8 -*-
# @Author: CSB307
# @Date:   2018-02-15 14:44:42
# @Last Modified by:   CSB307
# @Last Modified time: 2018-02-15 16:19:02

# @Title: Nested SelectionProgramming
# @Student name: Anurak Boonyaritpanit
# @ID: 560510680
# @ Lab04_2 (à¹€à¸›à¸£à¸µà¸¢à¸šà¹€à¸—à¸µà¸¢à¸šà¸ªà¸´à¸™à¸„à¹‰à¸³)

price_product_a = int(input("Enter A's price: "))
quality_product_a = int(input("Enter A's quality (0-4): "))

price_product_b = int(input("Enter B's price: "))
quality_product_b = int(input("Enter B's quality (0-4): "))

# compare price
if( price_product_a  < price_product_b and quality_product_a > quality_product_b ):
    print("Pick A")

elif( price_product_a  > price_product_b and quality_product_a < quality_product_b ):
    print("Pick B")

elif( price_product_a  == price_product_b or quality_product_a == quality_product_b):
    if( price_product_a  == price_product_b and quality_product_a == quality_product_b):
        print("Both are equally good")
    elif( price_product_a  == price_product_b):
        if( quality_product_a > quality_product_b ):
            print("Pick A")
        else:
            print("Pick B")
    elif( quality_product_a == quality_product_b ):
        if( price_product_a < price_product_b ):
            print("Pick A")
        else:
            print("Pick B")
else:
    print("Not sure...")



