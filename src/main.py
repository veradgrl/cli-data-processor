import argparse
import logging
from pathlib import Path  # * dosya yolunu oluşturacak

from src.exceptions import DataLoadError, DataValidationError
from src.loaders import load_data  # * json'ı okuyacak
from src.processors import (  # * transaction'ları işleyecek
    TransactionProcessor,
    UserProcessor,
)


def main():

    logger = logging.getLogger(
        __name__
    )  # * __name__ logger'ın hangi modülden geldiğini belirtir
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    parser = (
        argparse.ArgumentParser()
    )  # parser : terminalden gelecek bilgileri okuyacak nesne

    parser.add_argument(
        "--status", choices=["pending", "completed", "cancelled"]
    )  # * terminalden --status yazılırsa onu oku ve args.status içine koy

    parser.add_argument(
        "--category",
        choices=["food", "electronics", "makeup", "clothes", "travel", "entertainment"],
    )

    parser.add_argument(
        "--user_id", type=int
    )  # * string olarak gelen veriyi inte çevirerek args içine koy

    parser.add_argument(
        "--amount", type=float
    )  # * string olarak gelen veriyi floata çevirerek args içine koy

    parser.add_argument(
        "--currency", choices=["TRY", "USD", "EUR"]
    )  # * string olarak gelen veriyi floata çevirerek args içine koy

    parser.add_argument("--id", type=int)

    parser.add_argument("--name")

    parser.add_argument("--email")

    parser.add_argument("--is_active", type=bool)

    args = (
        parser.parse_args()
    )  # args : terminalde kullanıcı ne yazdıysa oku ve args içine koy

    # print(args.status) # args.status : terminalde kullanıcı --status yazdıysa onu oku ve ekrana yaz

    data_path = Path("data/sample.json")
    try:
        logger.info("veriler yükleniyor..")
        users, transactions = load_data(data_path)
        logger.info("veriler başarıyla yüklendi")
    except DataLoadError as e:  # * hata mesajını e değişkeninde saklıyoruz
        logger.error(e)
        raise SystemExit(1)
    except DataValidationError as e:
        logger.error(e)
        raise SystemExit(1)

    processor_transaction = TransactionProcessor(transactions)
    processor_user = UserProcessor(users)

    result_transactions = transactions  # * kullanıcı hangi filtreleri verdiyse result üzerinden sırayla geçecek
    result_users = users
    transaction_filter_used = False
    user_filter_used = False

    #! status # noqa: EXE005
    if args.status:
        transaction_filter_used = True
        result_transactions = processor_transaction.filter_by_status(
            result_transactions, args.status
        )

    #! category # noqa: EXE005
    if args.category:
        transaction_filter_used = True
        result_transactions = processor_transaction.filter_by_category(
            result_transactions, args.category
        )

    #! user_id  # noqa: EXE005
    if args.user_id:
        transaction_filter_used = True
        result_transactions = processor_transaction.filter_by_user_id(
            result_transactions, args.user_id
        )

    #! amount  # noqa: EXE005
    if args.amount:
        transaction_filter_used = True
        result_transactions = processor_transaction.filter_by_amount(
            result_transactions, args.amount
        )

    #! currency # noqa: EXE005
    if args.currency:
        transaction_filter_used = True
        result_transactions = processor_transaction.filter_by_currency(
            result_transactions, args.currency
        )

    #! user_id # noqa: EXE005
    if args.id:
        user_filter_used = True
        result_users = processor_user.filter_by_id(result_users, args.id)

    #! name # noqa: EXE005
    if args.name:
        user_filter_used = True
        result_users = processor_user.filter_by_name(result_users, args.name)

    #! email # noqa: EXE005
    if args.email:
        user_filter_used = True
        result_users = processor_user.filter_by_email(result_users, args.email)

    #! is_active # noqa: EXE005
    if args.is_active is not None:
        user_filter_used = True
        result_users = processor_user.filter_by_is_active(result_users, args.is_active)

    result_users = list(result_users)
    # print(result_users)

    if user_filter_used:
        user_ids = [user.id for user in result_users]

        if transaction_filter_used:
            # Hem user hem transaction filtresi var:
            # transaction'ları hem user_id'ye hem de girilen filtrelere göre daralt
            result_transactions = processor_transaction.filter_by(
                result_transactions, lambda t: t.user_id in user_ids
            )
        else:
            # Sadece user filtresi var: transaction'ları hiç yazdırma
            result_transactions = []

        for user in result_users:
            logger.info(user)

    for transaction in result_transactions:
        logger.info(transaction)


if (
    __name__ == "__main__"
):  # * terminalden bu dosya çalıştırılırsa main() fonksiyonunu çalıştır + test yaparken istediğimiz zaman çağırabiliriz
    main()
