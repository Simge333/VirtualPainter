# 🎨 Virtual Painter

El hareketleriyle gerçek zamanlı olarak ekranda çizim yapmanızı sağlayan, bilgisayar görüsü tabanlı bir sanal boya uygulaması.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange)

---

## 📌 Proje Hakkında

Virtual Painter, webcam aracılığıyla elinizi takip ederek ekranda çizim yapmanıza olanak tanır. MediaPipe tabanlı el takip modülü sayesinde parmak hareketlerinizi tanıyarak **seçim modu** ve **çizim modu** arasında geçiş yapabilirsiniz. Farklı renkler ve silgi aracıyla tamamen elleri kullanmadan dijital resim çizebilirsiniz.

---

## ✨ Özellikler

- 🖐 **Gerçek Zamanlı El Takibi** — MediaPipe ile yüksek doğrulukta el ve parmak ucu tespiti
- 🖌 **Çizim Modu** — İşaret parmağıyla serbest el çizimi
- 🎨 **Renk Seçimi** — Üst menüden Pembe, Mavi ve Sarı renk seçenekleri
- 🧹 **Silgi** — Siyah rengi seçerek çizilen alanları silebilme
- 📷 **Ayna Görünümü** — Webcam görüntüsü yatay olarak çevrilir, doğal kullanım deneyimi
- 🖼 **Header Katmanı** — Üst bölümde araç çubuğu olarak özel görsel başlıklar

---

## 🕹 Kullanım

### Parmak Kontrolleri

| Mod | Parmak Pozisyonu | Açıklama |
|---|---|---|
| **Seçim Modu** | İşaret + Orta parmak yukarı | Renk / araç seçmek için üst menüye dokunun |
| **Çizim Modu** | Yalnızca işaret parmağı yukarı | Ekranda serbest çizim yapın |

### Renk Seçimi (Üst Menü)

| Alan (X koordinatı) | Renk |
|---|---|
| 250 – 450 | 🟣 Pembe |
| 550 – 750 | 🔵 Mavi |
| 800 – 950 | 🟡 Sarı (Cyan) |
| 1050 – 1200 | ⬛ Silgi (Siyah) |

---

## 📁 Proje Yapısı

```
VirtualPainter/
│
├── virualPainter.py        # Ana uygulama dosyası
├── HandTrackingModule.py   # El takip modülü (MediaPipe tabanlı)
│
├── Header/                 # Araç çubuğu görselleri
│   ├── 1.png               # Pembe renk başlığı
│   ├── 2.png               # Mavi renk başlığı
│   ├── 3.png               # Cyan renk başlığı
│   └── 4.png               # Silgi başlığı
│
├── HandTrackingProject/    # Ek el takip denemeleri
└── venv/                   # Python sanal ortamı
```

---

## ⚙️ Kurulum

### Gereksinimler

- Python 3.7+
- Webcam

### Adımlar

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/Simge333/VirtualPainter.git
   cd VirtualPainter
   ```

2. Sanal ortam oluşturun ve etkinleştirin:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\Activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install opencv-python mediapipe numpy
   ```

4. Uygulamayı başlatın:
   ```bash
   python virualPainter.py
   ```

---

## 🔧 Yapılandırma

`virualPainter.py` dosyasının üst kısmındaki değişkenleri düzenleyerek ayarları özelleştirebilirsiniz:

```python
brushThickness = 15    # Fırça kalınlığı
eraserThickness = 100  # Silgi kalınlığı
```

---

## 🛠 Kullanılan Teknolojiler

| Kütüphane | Kullanım Amacı |
|---|---|
| [OpenCV](https://opencv.org/) | Görüntü işleme ve webcam yönetimi |
| [MediaPipe](https://mediapipe.dev/) | El takibi ve landmark tespiti |
| [NumPy](https://numpy.org/) | Tuval (canvas) matrisi işlemleri |


---
