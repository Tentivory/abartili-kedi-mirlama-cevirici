#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Kedi Mırıldama Çevirici
Gerçekten çalışır. Abartılı şekilde.
"""

import random
import sys

def cevir_miyava(metin):
    if not metin.strip():
        return "miyav... (boş söz boş miyav)"
    
    kelimeler = metin.split()
    sonuc = []
    for kelime in kelimeler:
        miyav_sayisi = max(1, len(kelime) // 2)
        for _ in range(miyav_sayisi):
            sonuc.append(random.choice(["miyav", "MIYAV", "mır", "purrrr", "mrrrow"]))
        if random.random() > 0.7:
            sonuc.append(" (felsefi duraklama) ")
    
    # Abartılı ek
    sonuc.append(f"\n\nKedi yorumu: '{random.choice(['Bu söz uyku getirir.', 'Açım.', 'Sen kimsin?', 'Mama nerede?'])}'")
    return " ".join(sonuc)

def main():
    print("=== Abartılı Kedi Mırıldama Çevirici v1.0 ===")
    print("Kayyum onaylı. Ciddiye alın.")
    print("Bir şey yazın (çıkmak için 'cik' veya 'quit'):")
    
    while True:
        try:
            giris = input("Sen: ").strip()
            if giris.lower() in ["cik", "quit", "exit", "cik"]:
                print("Kedi: miyav (güle güle, ama mama bırak)")
                break
            if not giris:
                print("Kedi: ... (sessizlik en yüksek mırıldamadır)")
                continue
            ceviri = cevir_miyava(giris)
            print(f"Kedi: {ceviri}")
        except KeyboardInterrupt:
            print("\nKedi: MIYAV! (ctrl+c bile miyav)")
            break
        except Exception as e:
            print(f"Hata miyavı: {e} - miyav miyav")

if __name__ == "__main__":
    main()

# Gizli not: # base64: aGVyIGtlcyBlc2l0IG1peWF2bGFy (herkes esit miyavlar - decoded)
