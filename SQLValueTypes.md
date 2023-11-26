# MySQL Value Types

❌ = Not Supported Yet
✅ = Currently Supported

More info on MySQL data types: https://www.w3schools.com/sql/sql_datatypes.asp

## Populator Custom Types
- **Email** ✅
  - **Type Code for SQL Populator:** 34
  - **Description:** Will generate a random and unique email for each row.

- **Custom Text** ✅
  - **Type Code for SQL Populator:** "text" <- put this instead of code.
  - **Description:** Will put "text_n" as value in column, where n is a the row number.

## String Data Types
- **CHAR(SIZE)** ✅
  - **Type Code for SQL Populator:** 0
  - **Description:** *A FIXED length string (can contain letters, numbers, and special characters). The size parameter specifies the column length in characters - can be from 0 to 255. Default is 1*

- **VARCHAR(SIZE)** ✅
  - **Type Code for SQL Populator:** 1
  - **Description:** *A VARIABLE length string (can contain letters, numbers, and special characters). The size parameter specifies the maximum string length in characters - can be from 0 to 65535*

- **BINARY(SIZE)** ✅
  - **Type Code for SQL Populator:** 2
  - **Description:** *Equal to CHAR(), but stores binary byte strings. The size parameter specifies the column length in bytes. Default is 1*

- **VARBINARY(SIZE)** ✅
  - **Type Code for SQL Populator:** 3
  - **Description:** *Equal to VARCHAR(), but stores binary byte strings. The size parameter specifies the maximum column length in bytes*

- **TINYBLOB** ✅
  - **Type Code for SQL Populator:** 4
  - **Description:** *For BLOBs (Binary Large Objects). Max length: 255 bytes*

- **TINYTEXT** ✅
  - **Type Code for SQL Populator:** 5
  - **Description:** *Holds a string with a maximum length of 255 characters*

- **TEXT(SIZE)** ✅
  - **Type Code for SQL Populator:** 6
  - **Description:** *Holds a string with a maximum length of 65,535 bytes*

- **BLOB(SIZE)** ✅
  - **Type Code for SQL Populator:** 7
  - **Description:** *For BLOBs (Binary Large Objects). Holds up to 65,535 bytes of data*

- **MEDIUMTEXT** ✅
  - **Type Code for SQL Populator:** 8
  - **Description:** *Holds a string with a maximum length of 16,777,215 characters*

- **MEDIUMBLOB** ✅
  - **Type Code for SQL Populator:** 9
  - **Description:** *For BLOBs (Binary Large Objects). Holds up to 16,777,215 bytes of data*

- **LONGTEXT** ✅
  - **Type Code for SQL Populator:** 10
  - **Description:** *Holds a string with a maximum length of 4,294,967,295 characters*

- **LONGBLOB** ✅
  - **Type Code for SQL Populator:** 11
  - **Description:** *For BLOBs (Binary Large Objects). Holds up to 4,294,967,295 bytes of data*

- **ENUM(val1, val2, val3, ...)** ❌
  - **Type Code for SQL Populator:** 12
  - **Description:** *A string object that can have only one value, chosen from a list of possible values. You can list up to 65535 values in an ENUM list. If a value is inserted that is not in the list, a blank value will be inserted. The values are sorted in the order you enter them*

- **SET(val1, val2, val3, ...)** ❌
  - **Type Code for SQL Populator:** 13
  - **Description:** *A string object that can have 0 or more values, chosen from a list of possible values. You can list up to 64 values in a SET list*

## Numeric Data Types
- **BIT(size)** ✅
  - **Type Code for SQL Populator:** 14
  - **Description:** *A bit-value type. The number of bits per value is specified in size. The size parameter can hold a value from 1 to 64. The default value for size is 1.*

- **TINYINT(size)** ✅
  - **Type Code for SQL Populator:** 15
  - **Description:** *A very small integer. Signed range is from -128 to 127. Unsigned range is from 0 to 255. The size parameter specifies the maximum display width (which is 255)*

- **BOOL** ✅
  - **Type Code for SQL Populator:** 16
  - **Description:** *Zero is considered as false, nonzero values are considered as true.*

- **BOOLEAN** ❌
  - **Type Code for SQL Populator:** 17
  - **Description:** *Equal to BOOL*

- **SMALLINT(size)** ❌
  - **Type Code for SQL Populator:** 18
  - **Description:** *A small integer. Signed range is from -32768 to 32767. Unsigned range is from 0 to 65535. The size parameter specifies the maximum display width (which is 255)*

- **MEDIUMINT(size)** ❌
  - **Type Code for SQL Populator:** 19
  - **Description:** *A medium integer. Signed range is from -8388608 to 8388607. Unsigned range is from 0 to 16777215. The size parameter specifies the maximum display width (which is 255)*

- **INT(size)** ✅
  - **Type Code for SQL Populator:** 20
  - **Description:** *A medium integer. Signed range is from -2147483648 to 2147483647. Unsigned range is from 0 to 4294967295. The size parameter specifies the maximum display width (which is 255)*

- **INTEGER(size)** ❌
  - **Type Code for SQL Populator:** 21
  - **Description:** *Equal to INT(size)*

- **BIGINT(size)** ❌
  - **Type Code for SQL Populator:** 22
  - **Description:** *A large integer. Signed range is from -9223372036854775808 to 9223372036854775807. Unsigned range is from 0 to 18446744073709551615. The size parameter specifies the maximum display width (which is 255)*

- **FLOAT(size, d)** ❌
  - **Type Code for SQL Populator:** 23
  - **Description:** *A floating point number. The total number of digits is specified in size. The number of digits after the decimal point is specified in the d parameter. This syntax is deprecated in MySQL 8.0.17, and it will be removed in future MySQL versions*

- **FLOAT(p)** ❌
  - **Type Code for SQL Populator:** 24
  - **Description:** *A floating point number. MySQL uses the p value to determine whether to use FLOAT or DOUBLE for the resulting data type. If p is from 0 to 24, the data type becomes FLOAT(). If p is from 25 to 53, the data type becomes DOUBLE()*

- **DOUBLE(size, d)** ✅
  - **Type Code for SQL Populator:** 25
  - **Description:** *A normal-size floating point number. The total number of digits is specified in size. The number of digits after the decimal point is specified in the d parameter*

- **DOUBLE PRECISION(size, d)** ❌
  - **Type Code for SQL Populator:** 26
  - **Description:** *Empty description. Possibly an incomplete entry.*

- **DECIMAL(size, d)** ✅
  - **Type Code for SQL Populator:** 27
  - **Description:** *An exact fixed-point number. The total number of digits is specified in size. The number of digits after the decimal point is specified in the d parameter. The maximum number for size is 65. The maximum number for d is 30. The default value for size is 10. The default value for d is 0.*

- **DEC(size, d)** ❌
  - **Type Code for SQL Populator:** 28
  - **Description:** *Equal to DECIMAL(size, d)*


## Date and Time Data Types
- **DATE** ✅
  - **Type Code for SQL Populator:** 29
  - **Description:** *A date. Format: YYYY-MM-DD. The supported range is from '1000-01-01' to '9999-12-31'*

- **DATETIME(fsp)** ✅
  - **Type Code for SQL Populator:** 30
  - **Description:** *A date and time combination. Format: YYYY-MM-DD hh:mm:ss. The supported range is from '1000-01-01 00:00:00' to '9999-12-31 23:59:59'. Adding DEFAULT and ON UPDATE in the column definition to get automatic initialization and updating to the current date and time*

- **TIMESTAMP(fsp)** ❌
  - **Type Code for SQL Populator:** 31
  - **Description:** *A timestamp. TIMESTAMP values are stored as the number of seconds since the Unix epoch ('1970-01-01 00:00:00' UTC). Format: YYYY-MM-DD hh:mm:ss. The supported range is from '1970-01-01 00:00:01' UTC to '2038-01-09 03:14:07' UTC. Automatic initialization and updating to the current date and time can be specified using DEFAULT CURRENT_TIMESTAMP and ON UPDATE CURRENT_TIMESTAMP in the column definition*

- **TIME(fsp)** ✅
  - **Type Code for SQL Populator:** 32
  - **Description:** *A time. Format: hh:mm:ss. The supported range is from '-838:59:59' to '838:59:59'*

- **YEAR** ❌
  - **Type Code for SQL Populator:** 33
  - **Description:** *Empty description. Additional details might be required.*