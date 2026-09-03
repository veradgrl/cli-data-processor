
# CLI Data Processor

JSON formatındaki kullanıcı ve transaction verilerini komut satırı (CLI) üzerinden yükleyip farklı kriterlere göre filtrelemeyi sağlayan Python uygulaması.

## Özellikler

- JSON dosyasından veri okuma
- User ve Transaction modelleri
- Transaction ve User filtreleme
- Birden fazla filtrenin birlikte kullanılabilmesi
- Currency, category, status, amount ve user ID filtreleri
- Hata yönetimi ve özel exception'lar
- Unit testler
- %91 test coverage

## Proje Yapısı

```text
cli-data-processor/
│
├── data/
│   └── sample.json
│
├── src/
│   ├── base.py
│   ├── exceptions.py
│   ├── loaders.py
│   ├── main.py
│   ├── models.py
│   └── processors.py
│
├── tests/
│   ├── conftest.py
│   ├── test_cli.py
│   ├── test_loaders.py
│   └── test_processors.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

### Klasör ve Dosyalar

**`data/`**  
Uygulamanın üzerinde çalıştığı örnek JSON verisini içerir.

**`src/models.py`**  
`User` ve `Transaction` dataclass modellerini içerir.

**`src/loaders.py`**  
JSON dosyasını okur ve verileri `User` ve `Transaction` nesnelerine dönüştürür. Geçersiz veya eksik veriler için hata kontrolü gerçekleştirir.

**`src/base.py`**  
Processor sınıfları için ortak abstract yapıyı tanımlar. `filter_by()` metodu ortak filtreleme mantığını sağlar.

**`src/processors.py`**  
Transaction ve User verileri için filtreleme işlemlerini gerçekleştirir. `TransactionProcessor` ve `UserProcessor` sınıflarını içerir.

**`src/exceptions.py`**  
Veri yükleme ve veri doğrulama sırasında kullanılmak üzere özel exception sınıflarını içerir.

**`src/main.py`**  
CLI uygulamasının giriş noktasıdır. Command-line argument'larını alır, verileri yükler ve seçilen filtreleri uygular.

**`tests/`**  
Loader, processor ve CLI davranışlarını test eden test dosyalarını içerir.

## Örnek Çalışma

Aşağıdaki örnekte uygulama `completed` status'una sahip transaction'ları filtrelemek için kullanılmaktadır.

```bash
python -m src.main --status completed
```

<img width="1033" height="140" alt="image" src="https://github.com/user-attachments/assets/4308676b-a15b-4138-a223-02168f06f19a" />


## Birden Fazla Filtre Kullanımı

Birden fazla filtre aynı komutta kullanılabilir:

```bash
python -m src.main --status completed --category food --user_id 3
```
<img width="945" height="70" alt="image" src="https://github.com/user-attachments/assets/962fa38e-cacf-4b57-8fde-ebcd2f61554a" />

## Kurulum

Projeyi klonladıktan sonra proje klasörüne girin:

```bash
git clone https://github.com/veradgrl/cli-data-processor.git
cd cli-data-processor
```

Virtual environment oluşturun:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Gerekli bağımlılıkları yükleyin:

```bash
pip install -r requirements.txt
```

## Kullanım

Uygulamayı çalıştırmak için:

```bash
python -m src.main
```

Filtrelerle birlikte kullanılabilir:

```bash
python -m src.main --status completed
```

```bash
python -m src.main --currency TRY
```

Birden fazla filtre aynı anda kullanılabilir:

```bash
python -m src.main --status completed --category food --user_id 3
```

## Testler

Testleri çalıştırmak için:

```bash
pytest
```

Test coverage görmek için:

```bash
pytest --cov=src
```

Projenin test coverage oranı **%91**'dir.

**📸 Ekran görüntüsü:**

> Buraya `pytest --cov=src` komutunun ve %91 coverage sonucunun göründüğü ekran görüntüsü eklenecek.

## Kullanılan Teknolojiler

- Python
- pytest
- pytest-cov
- mypy
- ruff
- black
- dacite

## Geliştirici

**Vera Değerli**

[LinkedIn](https://www.linkedin.com/in/vera-de%C4%9Ferli-413330311/)  
[GitHub](https://github.com/veradgrl)
