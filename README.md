# Speech-Emotion-Detection-and-Analysis


**Speech-Emotion-Detection-and-Analysis** duygu analizi için ses verisi toplama amacıyla geliştirilmiş bir Python programıdır. Bu program, özellikle YouTube'dan ses verilerini indirir ve verileri sesli duygu analizine uygun formatta işler. Topladığı ses dosyalarını belirli kategorilere ayırarak, daha sonra analiz edebilecek şekilde düzenler.

## Proje Özeti

Bu program, **YouTube** gibi platformlardan konuşma içerikli ses dosyalarını indirip, bu verileri duygusal içeriklerine göre ayırır. Amacı, veri seti oluşturmak ve farklı duygu kategorilerine göre sınıflandırma yapabilmek için doğru ve düzenli ses dosyaları sağlamaktır.

Program ile ayrıca:
- Ses dosyalarını indirir.
- Ses dosyalarında belirli düzenlemeler yaparak, duygu analizine uygun hale getirir.
- Boş (sessiz) ses dosyalarını ayıklayarak temizler.
- Ses dosyalarını kategorilere ayırarak düzenler.

### Şu anki Özellikler

- **Ses Dosyası İndirme**: YouTube'dan ses dosyalarını indirir ve ilgili formata dönüştürür.
- **Boş Ses Dosyaları Ayıklama**: Sessiz olan ses dosyalarını ayıklar ve gereksiz verilerden temizler.
- **Veri Organizasyonu**: Ses dosyalarını duygusal içeriklerine göre düzenler ve kategorize eder.
- **Ses Dosyası İşleme**: İndirilen ses dosyalarını işleyip veriye uygun formatta düzenler.

### Gelecek Planları

- **Duygusal İçerik Sınıflandırması**: Toplanan ses verileri için duygusal içerik sınıflandırması yapılabilir.
- **Daha Fazla Kaynak Ekleme**: YouTube dışında başka platformlardan veri toplamak için yeni kaynaklar eklenebilir.
- **Duygu Etiketleme ve Analiz**: Duygusal içeriklerin etiketlenmesi ve analiz edilmesi üzerinde çalışmalar yapılacaktır.

## Gereksinimler

Programı çalıştırmak için aşağıdaki bağımlılıkların yüklü olması gerekir:

- `yt-dlp`: YouTube ve diğer platformlardan video ve ses dosyalarını indirmek için kullanılır.
- `pydub`: Ses dosyalarını işlemek için kullanılır.
- `spleeter`: Ses kaynağı ayırma aracı, müzikten ses ve konuşma gibi kaynakları ayırmak için kullanılır.
- `shutil`: Dosya ve dizin işlemleri için kullanılır.
- `os`: Dosya yolu işlemleri için kullanılır.
- `selenium` : Web tarayıcısını otomatikleştirmek için kullanılır.
- `beautifulsoup4` : HTML ve XML verilerini işlemek için kullanılır.
### Google Drive Linki: https://drive.google.com/drive/folders/1ND_xq83rLYEkg_mtz7T2H_3nS4CB1Ny8

