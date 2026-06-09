from model.account import Account


class AccountRepository:

    @staticmethod
    def create(db, account):

        account_db = Account(
            account_number=account.account_number,
            balance=account.balance,
            customer_id=account.customer_id
        )

        db.add(account_db)
        db.commit()
        db.refresh(account_db)

        return account_db

    @staticmethod
    def get_all(db):

        return db.query(Account).all()