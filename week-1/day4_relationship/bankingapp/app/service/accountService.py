from repositories.accountRepository import AccountRepository


class AccountService:

    @staticmethod
    def create_account(db, account):

        return AccountRepository.create(
            db,
            account
        )

    @staticmethod
    def get_accounts(db):

        return AccountRepository.get_all(db)