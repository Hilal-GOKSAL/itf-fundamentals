# Translation with Python;
pip install textblob

from textblob import TextBlob

text = "data science is one of the best paid professions "
blob = TextBlob(text)
blob_eng = blob.translate(to='tr')
blob_Hirvat = blob.translate(to='hr')
blob_Hind = blob.translate(to='hi')
blob_Ru = blob.translate(to='ru')
blob_Tr = blob.translate(to='tr')

print(blob_eng)
print(blob_Hirvat)
print(blob_Hind)
print(blob_Ru)
print(blob_Tr)

# veri bilimi en iyi ücretli mesleklerden biridir
# znanost o podacima jedno je od najbolje plaćenih zanimanja
# डेटा साइंस सबसे अच्छे भुगतान वाले व्यवसायों में से एक है
# наука о данных - одна из самых высокооплачиваемых профессий
# veri bilimi en iyi ücretli mesleklerden biridir
