import gensim
model = gensim.models.fasttext.load_facebook_vectors('cc.en.300.bin')
kelimeler = ["kid", "woman", "disabled", "immigrant", "refugee", "gay", "orphan", "homeless", "sick", "poor", "muslim", "black", "african american", "fat", "middle east", "syria", "terror"]
for i in range(len(kelimeler)):
    print(model.most_similar(kelimeler[i]))
    print("----")