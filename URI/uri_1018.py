dinheiro  = int(input())

troco     = dinheiro

cem       = int(troco / 100)
troco     = troco - (cem * 100)
cinquenta = int(troco / 50)
troco     = troco - (cinquenta * 50)
vinte     = int(troco / 20)
troco     = troco - (vinte * 20)
dez       = int(troco / 10)
troco     = troco - (dez * 10)
cinco     = int(troco / 5)
troco     = troco - (cinco * 5)
dois      = int(troco / 2)
troco     = troco - (dois * 2)

print(f"""{dinheiro}
{cem} nota(s) de R$ 100,00
{cinquenta} nota(s) de R$ 50,00
{vinte} nota(s) de R$ 20,00
{dez} nota(s) de R$ 10,00
{cinco} nota(s) de R$ 5,00
{dois} nota(s) de R$ 2,00
{troco} nota(s) de R$ 1,00""")