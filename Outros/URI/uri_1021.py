dinheiro  = float(input())

troco     = dinheiro + 0.001

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

um       = int(troco / 1)
troco    = troco - (um * 1)
cent50   = int(troco / 0.5)
troco    = troco - (cent50 * 0.5)
cent25   = int(troco / 0.25)
troco    = troco - (cent25 * 0.25)
cent10   = int(troco / 0.10)
troco    = troco - (cent10 * 0.10)
cent05   = int(troco / 0.05)
troco    = troco - (cent05 * 0.05)
cent01   = int(troco / 0.01)

print(f"""NOTAS:
{cem} nota(s) de R$ 100.00
{cinquenta} nota(s) de R$ 50.00
{vinte} nota(s) de R$ 20.00
{dez} nota(s) de R$ 10.00
{cinco} nota(s) de R$ 5.00
{dois} nota(s) de R$ 2.00
MOEDAS:
{um} moeda(s) de R$ 1.00
{cent50} moeda(s) de R$ 0.50
{cent25} moeda(s) de R$ 0.25
{cent10} moeda(s) de R$ 0.10
{cent05} moeda(s) de R$ 0.05
{cent01} moeda(s) de R$ 0.01""")