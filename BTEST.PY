KAMPANYA_A=[100,120,150,130,140,190,200,200]
KAMPANYA_B=[150,300,100,150,200,100,450,300]
print(KAMPANYA_A)
print(KAMPANYA_B)
from scipy import stats

# T-Testi İki örneklem grubu arasında ortalamalar açısından fark olup olmadığını araştırmak için kullanılır.
t_stat, p_value = stats.ttest_ind(KAMPANYA_A, KAMPANYA_B)

# BURDA İF MANTIĞI İLE HANGİ KAMPANYAYI SEÇMEMİZ GEREKTİĞİNİ ÖĞRENECEĞİZ

if p_value <0.05:
    #Eğer p değeri 0,05'ten küçük ise anlamlıdır.
    if sum(KAMPANYA_A)> sum(KAMPANYA_B):
        sonuc='A kampanyası seçilmelidir. A kampanyası istatistiksel olarak anlamlı ve en çok satışı yapan kampanyadır'
    else:
        sonuc='B kampanyası seçilmelidir. B kampanyası istatistiksel olarak anlamlı ve en çok satışı yapan kampanyadır'
else:
    # Eğer p-değeri 0.05'ten büyükse, fark anlamlı değildir
    sonuc = "İki kampanya arasında anlamlı bir fark yoktur, her iki kampanya da seçilebilir."

print(f"Sonuç: {sonuc}")
    