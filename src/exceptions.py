class DataLoadError(Exception):
    pass
    # Veri dosyası okunurken oluşan hatalar


class DataValidationError(Exception):
    pass
    # Verinin beklenen yapıya uygun olmadığı durumlar
