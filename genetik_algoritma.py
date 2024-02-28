import numpy as np

# Fitness fonksiyonu: Bireyin çözüm kalitesini değerlendirir.
def fitness(birey):
    # Örnek olarak, maksimum toplamı aradığımız bir problem varsayalım.
    return sum(birey)

# Seçim fonksiyonu: En iyi bireyleri seçer.
def secim(populasyon, skorlar, n_birey=2):
    # En iyi n_birey'i seçmek için fitness skorlarına göre sıralama
    secilenler = np.argsort(skorlar)[-n_birey:]
    return populasyon[secilenler]

# Çaprazlama fonksiyonu: Yeni bireyler üretir.
def caprazlama(a, b):
    # Rastgele bir noktada ikiye böl ve genleri birleştir
    kesim_noktasi = np.random.randint(1, len(a))
    yeni_birey = np.concatenate((a[:kesim_noktasi], b[kesim_noktasi:]))
    return yeni_birey

# Mutasyon fonksiyonu: Bireylerde rastgele değişiklikler yapar.
def mutasyon(birey, mutasyon_orani=0.01):
    for i in range(len(birey)):
        if np.random.rand() < mutasyon_orani:
            birey[i] = np.random.randint(1, 100) # Rastgele bir değer ile değiştir
    return birey

# Genetik algoritma ana fonksiyonu
def genetik_algoritma(populasyon_sayisi=100, gen_sayisi=10, nesil_sayisi=100):
    # Başlangıç popülasyonunu rastgele oluştur
    populasyon = np.random.randint(0, 100, (populasyon_sayisi, gen_sayisi))
    for nesil in range(nesil_sayisi):
        skorlar = np.array([fitness(birey) for birey in populasyon])
        secilenler = secim(populasyon, skorlar)
        yeni_populasyon = []
        for i in range(0, populasyon_sayisi, 2):
            a, b = secilenler[np.random.choice(len(secilenler), 2, replace=False)]
            cocuk = caprazlama(a, b)
            cocuk = mutasyon(cocuk)
            yeni_populasyon.append(cocuk)
        populasyon = np.array(yeni_populasyon)
        # En iyi çözümü yazdır
        print(f"Nesil {nesil}: En iyi skor {max(skorlar)}")
    return populasyon

# Algoritmayı çalıştır
genetik_algoritma()


'''
1) Popülasyon Oluşturma: Rastgele oluşturulan bir dizi çözüm (birey) ile başlar. Her birey, problemi çözmek için bir aday çözüm olarak görülür.
2 )Fitness Değerlendirme: Her bireyin problemi ne kadar iyi çözdüğünü belirleyen bir fitness değerine sahiptir. Bu değer, çözümün kalitesini ölçer.
3) Seçim: Fitness değerlerine göre bireyler seçilir. Yüksek fitness değerine sahip bireylerin bir sonraki nesile geçme olasılığı daha yüksektir.
4) Çaprazlama (Crossover): Seçilen bireyler, yeni bireyler (çocuklar) oluşturmak için bir araya getirilir. Bu işlem, bireylerin genlerinin bir kombinasyonunu sağlar.
5) Mutasyon: Çocuk bireylerde rastgele değişiklikler yapılır. Bu, çeşitliliği artırır ve yerel optimumlardan kaçınmaya yardımcı olur.
6) Yeni Popülasyon: Çaprazlama ve mutasyon sonucu oluşan yeni bireyler, bir sonraki nesil olarak kabul edilir ve işlem tekrarlanır.


'''