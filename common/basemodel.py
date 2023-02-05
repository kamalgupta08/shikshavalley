from datetime import datetime
from decimal import Decimal
from shikshavalley.extensions import db

class BaseModel(db.Model):
    """
    synchronize_session- chooses the strategy for the removal of matched objects from the session.
    Valid values are:
    1) False - don’t synchronize the session. This option is the most efficient
        and is reliable once the session is expired, which typically occurs after a commit(),
        or explicitly using expire_all().
    2) 'fetch' - performs a select query before the delete to find objects
        that are matched by the delete query and need to be removed from the session.
        Matched objects are removed from the session.
    3) 'evaluate' - Evaluate the query’s criteria in Python straight on the objects in the session.
        If evaluation of the criteria isn’t implemented, an error is raised.
    """
    __abstract__ = True
    # id = Column(Integer, primary_key=True)
    # created_at = Column(TIMESTAMP, default=get_current_utc_time(), nullable=False)
    # updated_at = Column(TIMESTAMP, default=get_current_utc_time(), onupdate=get_current_utc_time(), nullable=False)

    def __init__(self, sqlachemy_db=db, **kwargs):
        self.db = sqlachemy_db
        super().__init__(**kwargs)

    def __new__(cls, sqlachemy_db=db, *args, **kwargs):
        cls.db = sqlachemy_db
        return super(BaseModel, cls).__new__(cls)

    @classmethod
    def new(cls, **kwargs):
        obj = cls(**kwargs)
        cls.db.session.add(obj)
        return obj

    def as_dict(self, datetime_to_str=True):
        return {c.name: getattr(self, c.name).isoformat() if isinstance(getattr(self, c.name),
                                                                        datetime) and datetime_to_str else float(
            getattr(self, c.name)) if isinstance(getattr(self, c.name), Decimal) else getattr(self, c.name) for c in
                self.__table__.columns}

    @classmethod
    def get_all_records(cls, *args):
        """
        this will return a list of all the items
        :param args:
        :return:
        """
        return db.session.query(cls).filter(*args).all()

    @classmethod
    def get_first_record(cls, *args):
        """
        this will return the first result or ‘None’ if the result doesn’t contain a row.
        :param args:
        :return:
        """
        return db.session.query(cls).filter(*args).first()

    @classmethod
    def update_records(cls, update_query: dict, synchronize_session=False, *args):
        """
        Example - session.query(Engineer).\
                  filter(Engineer.id == Employee.id).\
                  filter(Employee.name == 'dilbert').\
                  update({"engineer_type": "programmer"})

        :param update_query:
        :param synchronize_session:
        :param args:
        :return:
        """
        result = db.session.query(cls).filter(*args).update(update_query,
                                                             synchronize_session=synchronize_session)
        return result

    @classmethod
    def delete_records(cls, synchronize_session=False, *args):
        """
        Perform a bulk delete query.
        Deletes rows matched by this query from the database.
        :param synchronize_session:
        :param args:
        :return: the count of rows matched as returned by the database’s “row count” feature.
        """
        result = db.session.query(cls).filter(*args).delete(synchronize_session=synchronize_session)
        return result
