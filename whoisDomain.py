#!/usr/bin/python3
# -*-coding:utf-8-*-

# Hakan Mustak
# hmustak@gmail.com
# 21.05.2017 - 23:37
# TopluWhois Denemesi
# Python3 - Training

import whois, datetime

domainler   = ['hassasvalf.com',
               'mustak.org',
               'didemblog.com']
tarihler = []
bugün = datetime.datetime.today()


def sorgula(domain):
    tarih = whois.whois(domain)
    return tarih.expiration_date


print(' {0:20} {1:12} {2:4}'.format('Domain', 'Tarih', ' Gün'))
print('-'*40)

for domainID in range(len(domainler)):
    tarihler.append(sorgula(domainler[domainID]))

    if (isinstance(tarihler[domainID], list)): # Veri tipi karşılaştırması için isinstance() kullanıyoruz
        print(' {0:20} {1:12} {2:4}'.format(domainler[domainID], tarihler[domainID][0].strftime('%d.%m.%Y'), (tarihler[domainID][0] - datetime.datetime.today()).days))
    else:
        print(' {0:20} {1:12} {2:4}'.format(domainler[domainID], tarihler[domainID].strftime('%d.%m.%Y'), (tarihler[domainID] - datetime.datetime.today()).days))

print('-'*40)
