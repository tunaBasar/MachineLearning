# BLG-407 Makine Öğrenmesi - Dönem Projeleri

**Ad Soyad:** [Adını Soyadını Buraya Yaz]
**Öğrenci No:** [Numaranı Yaz]
**Dönem:** 2025-2026 Güz

Bu depo, BLG-407 Makine Öğrenmesi dersi kapsamında geliştirdiğim üç farklı projeyi içeriyor. Dönem boyunca görüntü işleme, nesne tespiti ve regresyon analizi üzerine çalışmalar yaptım.

---

## 📂 Proje 1: CNN ile Görüntü Sınıflandırma

Bu projede hazır veri seti kullanmak yerine, kendi çektiğim fotoğraflardan oluşan özgün bir veri seti oluşturdum ve bir CNN (Konvolüsyonel Sinir Ağı) modeli eğittim.

* **Veri Seti:** Telefon kamerasıyla farklı açılardan ve ışık koşullarından çektiğim görselleri kullandım.
* **Yöntem:**
    * Verileri `train`, `validation` ve `test` klasörlerine ayırdım.
    * İşlem yükünü azaltmak için görselleri yeniden boyutlandırdım.
    * Hem kendi tasarladığım CNN mimarisini hem de Transfer Learning yöntemlerini denedim.
    * Modelin başarısını artırmak için Data Augmentation (veri çoğaltma) teknikleri uyguladım.

---

## 📂 Proje 2: YOLOv8 ile Nesne Tespiti ve Masaüstü Arayüzü

İkinci projede, güncel YOLOv8 algoritmasını kullanarak nesne tespiti yapan bir model eğittim. Ardından bu modelin kolayca kullanılabilmesi için bir masaüstü uygulaması geliştirdim.

* **Model:** YOLOv8n (Nano) modelini, etiketlediğim verilerle eğittim (`best.pt`).
* **Arayüz (GUI):** Arayüzü tasarlamak için Python'un PyQt5 kütüphanesini kullandım.
* **Neler Yapılabiliyor?**
    * Bilgisayardan fotoğraf seçip yüklenebiliyor.
    * "Test Image" butonuyla model çalıştırılıp nesneler kutu içine alınıyor.
    * Sonuçlar kaydedilebiliyor ve tespit edilen nesne sayıları listeleniyor.

**Kurulum ve Çalıştırma:**

    cd Proje2_NesneTespiti
    pip install -r requirements.txt
    python gui_app.py

---

## 📂 Proje 3: Flask ile Köpekbalığı Ağırlık Tahmini (Regresyon)

Son projede, Çoklu Doğrusal Regresyon (Multiple Linear Regression) yöntemini kullanarak bir tahmin modeli geliştirdim. Senaryo olarak köpekbalıklarının fiziksel özelliklerinden ağırlıklarını tahmin etmeyi seçtim.

* **Veri Analizi Adımlarım:**
    * Veri setindeki eksik yaş bilgilerini ortalama değer atayarak doldurdum.
    * "Tür" ve "Cinsiyet" gibi sözel verileri, makine anlayabilsin diye sayısal verilere (Encoding) çevirdim.
    * **Backward Elimination** tekniğiyle, sonuca etkisi olmayan (P-değeri yüksek) gereksiz sütunları eledim.
* **Web Arayüzü:** Flask kullanarak basit bir web sitesi yaptım. Bu sayede verileri forma girince model arka planda çalışıp tahmini ekrana yazdırıyor.

**Kurulum ve Çalıştırma:**

    cd Proje3_KopekbaligiAgirlikTahmin
    pip install -r requirements.txt
    python app.py

---

### 🛠 Genel Kurulum Notları

Projeleri çalıştırmadan önce ilgili klasörün içindeki kütüphaneleri yüklemeniz gerekebilir:

    pip install -r requirements.txt
