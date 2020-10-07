
#--- Exercício 3  - Variáveis
#--- Imprima dois parágrafos do último livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- As informações do Livro serão: 
#---    Título
#---    Edição
#---    Autor
#---    Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro

dictLivro = {'Titulo': 'Dom Casmurro', 'Edição': 'Não informado', 'Autor':'Machado de Assis', 'Data-Publicação':'1899'}

print(" ***** INFORMAÇÕES LIVRO *****")

for chave in dictLivro:
    print(chave, " - ", dictLivro[chave])

print("******************************")

print("""
PARÁGRAFOS: 
Outra vez D. Fortunata apareceu à porta da casa; não sei para que, se nem me
deixou tempo de puxar o braço; desapareceu logo. Podia ser um simples descargo
de consciência, uma cerimônia, como as rezas de obrigação, sem devoção, que se
dizem de tropel; a não ser que fosse para certificar aos próprios olhos a realidade
que o coração lhe dizia...

Fosse o que fosse, o meu braço continuou a apertar a cintura da filha, e foi assim
que nos pacificamos. O bonito é que cada um de nós queria agora as culpas para
si, e pedíamos reciprocamente perdão. Capitu alegava a insônia, a dor de cabeça,
o abatimento do espírito, e finalmente "os seus calundus”.Eu, que era muito
chorão por esse tempo, sentia os olhos molhados... Era amor puro, era efeito dos
padecimentos da amiguinha, era a ternura da reconciliação.""")