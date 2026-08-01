from sqlmodel import Field, SQLModel


# Generic model
class Message(SQLModel):
    message: str


class DataRow(SQLModel):
    age: int
    Medu: int
    Fedu: int
    traveltime: int
    studytime: int
    failures: int
    famrel: int
    freetime: int
    goout: int
    Dalc: int
    Walc: int
    health: int
    absences: int
    school: str
    sex: str
    address: str
    famsize: str
    Pstatus: str
    Mjob: str
    Fjob: str
    reason: str
    guardian: str
    schoolsup: str
    famsup: str
    paid: str
    activities: str
    nursery: str
    higher: str
    internet: str
    romantic: str


class InputModel(SQLModel):
    rows: list[DataRow] = Field(..., min_length=1)


class OutputModel(SQLModel):
    predictions: list[str]


class UserData(DataRow, table=True):
    id: int | None = Field(default=None, primary_key=True)
    performance_category: int
