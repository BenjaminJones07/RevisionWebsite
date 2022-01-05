from cs50 import SQL

class SQLWrapper(SQL):
    def _escape(self, value):

        import sqlparse

        if type(value) is None:
            return sqlparse.sql.Token(
                sqlparse.tokens.Keyword,
                "NULL")
            
        return super()._escape(value)