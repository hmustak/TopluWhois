# !/usr/bin/python3
# -*-coding:utf-8-*-

# ------------------------------------------------------------------------------------------------------------
# myDomain - Version2
# Domain kalan gün Sorgulama & Hesaplama Scripti
# Python3 - Training
#
# Version#1: 21.05.2017 - 23:37
# Version#2: 06.06.2017 - 21:51
# ------------------------------------------------------------------------------------------------------------
# Yazan: Hakan Mustak
# Mail: hmustak@gmail.com
# ------------------------------------------------------------------------------------------------------------
# Versiyon 2'de eklenenler;
# - Domain kalan gün sıralama algoritması eklendi
# - Yatay çizgi statik halden dinamik hale getirildi
# - Açıklamalarda anlaşılmayan yerler giderildi
# - Mail Fonksiyonu eklendi
# ------------------------------------------------------------------------------------------------------------


# Kullanılan Modüller
import whois, datetime, smtplib

# Liste ve değişkenler
domainler = ['hassasvalf.com', 'mustak.org', 'senemmustak.com', 'didemblog.com']
tarihler = []
domainBilgiler = []
bugün = datetime.datetime.today()
mesaj = """From: Hakan Mustak <hmustak@gmail.com>
To: Hakan Mustak <hakan@mustak.org>, Hasan Mustak <hassasvalf@hotmail.com>,
Subject: Domain Kalan Günler

Merhaba,
Domainlerinizle ilgili günlük hatırlatmadır. Hangi domainin kaç gün sonra register edilmesi gerektiğini hatırlatmak amacıyla gönderilmiştir.
""".encode('utf-8')

# Mail Değişkenleri
gonderici_mail = 'hmustak@gmail.com'
gonderici_sifre = ''
alicilar = ['hakan@mustak.org']


# Fonksiyonumuz - Tek tek listedeki Domainler geliyor
def sorgula(domain):
    # Domainlerimizin bilgilerini yüklediğimiz modülle çekiyoruz
    tarih = whois.whois(domain)
    # Domain süresi dolma tarihini geri döndürüyoruz
    return tarih.expiration_date


# Yatay Çizgi Fonksiyonumuz
def yatayCizgi(say):
    print('-' * say)


# Domain listemizi tek tek çekiyoruz
for domainID in range(len(domainler)):
    # Tarihi tutan listemize domain tarihlerimizi yazıyoruz (Evet, daha kısa bir fonksiyonla burası atlanarakta yapılabilirdi ama fazladan bir dizi ile
    #                                                        birden fazla bağlantı ihtiyacı olmaksızın script çalışma süresini kısaltıyor)
    tarihler.append(sorgula(domainler[domainID]))

    # Domain sayfasından dönen veri tipi liste yada stringse, işlemimizi ona göre ayırıp yapıyoruz
    if (isinstance(tarihler[domainID], list)):  # Veri tipi karşılaştırması için isinstance() kullanıyoruz
        domainBilgiler.append([domainler[domainID], tarihler[domainID][0].strftime('%d.%m.%Y'),
                               (tarihler[domainID][0] - datetime.datetime.today()).days])
    else:
        domainBilgiler.append([domainler[domainID], tarihler[domainID].strftime('%d.%m.%Y'),
                               (tarihler[domainID] - datetime.datetime.today()).days])

# Tüm veriyi aldığımıza göre diziyi kendi içine sıralayarak tekrar gömelim
domainBilgiler = sorted(domainBilgiler, key=lambda item: item[2])

# Başlık
# Ekrana Bas
print('\n {0:23} {1:14} {2:4}'.format('Domain', 'Tarih', ' Gün'))
# Mail Gövdesine Ekle
yatayCizgi(45)

# Gelen verimizi ekrana basalım
for domain in range(len(domainBilgiler)):
    print(
        ' {0:23} {1:14} {2:4}'.format(domainBilgiler[domain][0], domainBilgiler[domain][1], domainBilgiler[domain][2]))
    mesaj = mesaj + '\n{0} : {1} gün kaldı'.format(domainBilgiler[domain][0], domainBilgiler[domain][2]).encode('utf-8')

yatayCizgi(45)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(gonderici_mail, gonderici_sifre)
server.sendmail(gonderici_mail, alicilar, mesaj)

server.quit()

print("Mail Gönderildi")

# Hakan Müştak ©