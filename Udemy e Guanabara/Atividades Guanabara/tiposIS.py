algo = input("Digite algo: ")

print("INFORMAÇÕES")
print("- {} é {}". format(algo, type(algo)))
print("- {} é numérico: {}".format(algo, algo.isnumeric()))
print("- {} é alfabético: {}".format(algo, algo.isalpha()))
print("- {} é alfanumérico: {}".format(algo, algo.isalnum()))
print("- {} é maiúsculo: {}".format(algo, algo.isupper()))
print("- {} é minúsculo: {}".format(algo, algo.islower()))
print("- {} é espaço: {}".format(algo, algo.isspace()))
print("- {} é ascii: {}".format(algo, algo.isascii()))
print("- {} é capitalizada: {}".format(algo, algo.istitle()))