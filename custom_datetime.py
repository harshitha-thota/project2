import datetime

class CustomDateTime:
    def __init__(self, year=None, month=None, day=None, hour=0, minute=0, second=0):
        if year is None:
            current_datetime = datetime.datetime.utcnow()
            self._datetime = current_datetime.replace(hour=hour, minute=minute, second=second)
        else:
            self._datetime = datetime.datetime(year, month, day, hour, minute, second)

    @classmethod
    def from_iso_format(cls, iso_string):
        try:
            dt = datetime.datetime.fromisoformat(iso_string)
            return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
        except ValueError as e:
            raise ValueError(f"Invalid ISO format: {iso_string}") from e

    def to_iso_format(self):
        return self._datetime.isoformat()

    def to_human_readable_format(self):
        return self._datetime.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def validate_date(year, month, day):
        try:
            datetime.datetime(year, month, day)
            return True
        except ValueError:
            return False

    @classmethod
    def date_difference(cls, date1, date2, unit='days'):
        if not isinstance(date1, cls) or not isinstance(date2, cls):
            raise ValueError("Both dates must be instances of CustomDateTime")
        
        delta = date1._datetime - date2._datetime

        if unit == 'days':
            return delta.days
        elif unit == 'weeks':
            return delta.days // 7
        elif unit == 'months':
            return (date1.year - date2.year) * 12 + date1.month - date2.month
        else:
            raise ValueError("Invalid unit. Use 'days', 'weeks', or 'months'.")

    @staticmethod
    def date_from_string(date_string):
        try:
            dt = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
            return CustomDateTime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
        except ValueError as e:
            raise ValueError(f"Invalid date string format: {date_string}") from e

    # Properties to access individual parts of the datetime object
    @property
    def year(self):
        return self._datetime.year

    @property
    def month(self):
        return self._datetime.month

    @property
    def day(self):
        return self._datetime.day

    @property
    def hour(self):
        return self._datetime.hour

    @property
    def minute(self):
        return self._datetime.minute

    @property
    def second(self):
        return self._datetime.second
    
# Example usage:
# Creating instances using different methods
dt1 = CustomDateTime(2023, 1, 1, 12, 30, 45)
dt2 = CustomDateTime.from_iso_format("2023-01-01T12:30:45")

# Printing in different formats
print("ISO Format:", dt1.to_iso_format())
print("Human Readable Format:", dt1.to_human_readable_format())

# Accessing individual parts of the datetime object
print("Year:", dt1.year)
print("Month:", dt1.month)
print("Day:", dt1.day)
print("Hour:", dt1.hour)
print("Minute:", dt1.minute)
print("Second:", dt1.second)

# Validating a date
print("Is 2023-01-01 a valid date?", CustomDateTime.validate_date(2023, 1, 1))
print("Is 2023-02-30 a valid date?", CustomDateTime.validate_date(2023, 2, 30))

# Date difference
dt3 = CustomDateTime(2023, 1, 10)
print("Difference in days between dt1 and dt3:", CustomDateTime.date_difference(dt1, dt3, unit='days'))
print("Difference in weeks between dt1 and dt3:", CustomDateTime.date_difference(dt1, dt3, unit='weeks'))
print("Difference in months between dt1 and dt3:", CustomDateTime.date_difference(dt1, dt3, unit='months'))

# Creating a date from a string
dt4 = CustomDateTime.date_from_string("2023-03-15 08:45:30")
print("Date created from string:", dt4.to_human_readable_format())