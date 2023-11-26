import os
import itertools
import random

def generate_column_values(num_lines, tableColumnValueTypes):
    generatedValues = []

    # ------------- Generation Specific Values -------------
    genYear = 1000
    genMonth = 1
    genDay = 1

    genYearDateTime = 1000
    genMonthDateTime = 1
    genDayDateTime = 1

    genSecondsTime = 0
    genMinutesTime = 0
    genHoursTime = 0

    tinyintStart = -128

    if (34 in tableColumnValueTypes):
      # Email Generation Config (15625 combos)
      emailUsernameLength = 6
      availableEmailUsernameChars = 'abcde'
      emailUsernameCombos = list(itertools.product(availableEmailUsernameChars, repeat=emailUsernameLength))

    if (0 in tableColumnValueTypes):
      ## CHAR Generation Config (15625 combos)
      charSize = 6
      availableCharsForChar = 'abcde'
      charCombos = list(itertools.product(availableCharsForChar, repeat=charSize))

    if (1 in tableColumnValueTypes):
      ## VARCHAR Generation Config (15625 combos)
      varCharSize = 6
      availableCharsForVarchar = 'abcde'
      varCharCombos = list(itertools.product(availableCharsForVarchar, repeat=varCharSize))

    if (2 in tableColumnValueTypes):
      ## BINARY Generation Config (15625 combos)
      binarySize = 6
      availableCharsForBinary = '01'
      binaryCombos = list(itertools.product(availableCharsForBinary, repeat=binarySize))

    if (3 in tableColumnValueTypes):
      ## VARBINARY Generation Config (15625 combos)
      varbinarySize = 6
      availableCharsForVarbinary = '01'
      varbinaryCombos = list(itertools.product(availableCharsForVarbinary, repeat=varbinarySize))

    if (4 in tableColumnValueTypes):
      # TINYBLOB Generation Config
      tinyblobSize = 5 # in Bytes (255 = 255 bytes)
      tinyblob = bytes(bytearray(random.getrandbits(8) for _ in range(tinyblobSize)))

    if (7 in tableColumnValueTypes):
      # BLOB Generation Config
      blobSize = 5 # in Bytes (300 = 300 bytes)
      blob = bytes(bytearray(random.getrandbits(8) for _ in range(blobSize)))

    if (9 in tableColumnValueTypes):
      # MEDIUMBLOB Generation Config
      mediumblobSize = 5 # in Bytes (300 = 300 bytes)
      mediumblob = bytes(bytearray(random.getrandbits(8) for _ in range(blobSize)))

    if (11 in tableColumnValueTypes):
      # LONGBLOB Generation Config
      longblobSize = 5 # in Bytes (300 = 300 bytes)
      longblob = bytes(bytearray(random.getrandbits(8) for _ in range(blobSize)))

    # ------------- Generation Script -------------
    for i in range(num_lines):
        currentValuesLine = "("
        for columnType in tableColumnValueTypes:
            # Custom String
            if (type(columnType) == str):
                currentValuesLine += "'" + str(columnType) + "-" + str(i) + "', "

            # CHAR(size) (SQL Allows Max 255 characters in CHAR)
            elif (columnType == 0):
                currentValuesLine += "'" + "".join(charCombos[i]) + "', "

            # VARCHAR(size) (SQL Allows Max 65,535 characters in CHAR)
            elif (columnType == 1):
                randomizedLengthString = varCharCombos[i][:random.randint(1, varCharSize)]
                currentValuesLine += "'" + "".join(randomizedLengthString) + "', "
            
            # BINARY(size)
            elif (columnType == 2):
                currentValuesLine += "'" + "".join(binaryCombos[i]) + "', "

            # VARBINARY(size)
            elif (columnType == 3):
                randomizedLengthString = varbinaryCombos[i][:random.randint(1, varbinarySize)]
                currentValuesLine += "'" + "".join(randomizedLengthString) + "', "

            # TINYBLOB (SQL Allows Max 255 bytes in TINYBLOB)
            elif (columnType == 4):
                currentValuesLine += "'" + str(tinyblob) + "', "

            # TINYTEXT (SQL Allows Max 255 characters in TINYTEXT)
            elif (columnType == 5):
                length = 255 # Amount of Characters
                currentValuesLine += "'" + ('s' * length) + "', "
            
            # TEXT (SQL Allows Max 65,535 characters in TEXT)
            elif (columnType == 6):
                length = 300 # Amount of Characters
                currentValuesLine += "'" + ('s' * length) + "', "

            # BLOB (SQL Allows Max 65,535 bytes in BLOB)
            elif (columnType == 7):
                currentValuesLine += "'" + str(blob) + "', "

            # MEDIUMTEXT (SQL Allows Max 16,777,215 characters in MEDIUMTEXT)
            elif (columnType == 8):
                length = 300 # Amount of Characters
                currentValuesLine += "'" + ('s' * length) + "', "

            # MEDIUMBLOB (SQL Allows Max 16,777,215 bytes in MEDIUMBLOB)
            elif (columnType == 9):
                currentValuesLine += "'" + str(mediumblob) + "', "

            # LONGTEXT (SQL Allows Max 4,294,967,295 characters in LONGTEXT)
            elif (columnType == 10):
                length = 300 # Amount of Characters
                currentValuesLine += "'" + ('s' * length) + "', "

            # LONGBLOB (SQL Allows Max 4,294,967,295 bytes in LONGBLOB)
            elif (columnType == 11):
                currentValuesLine += "'" + str(longblob) + "', "

            # BIT(size) (SQL Allows 1-64 bits)
            elif (columnType == 14):
                bitAmount = 64
                currentValuesLine += ('0' * bitAmount) + ", "
            
            # TINYINT(size) (-128 to 127)(size parameter specifies the maximum display width (which is 255))
            elif (columnType == 15):
                if tinyintStart > 127:
                    tinyintStart = -128
                currentValuesLine += str(tinyintStart) + ", "
                tinyintStart += 1

            # BOOL (Zero is considered as false, nonzero values are considered as true.)
            elif (columnType == 16):
                currentValuesLine += str(0) + ", "

            # INT (Signed range is from -2147483648 to 2147483647. Unsigned range is from 0 to 4294967295.)
            elif (columnType == 20):
                currentValuesLine += str(i) + ", "

            # DOUBLE
            elif (columnType == 25):
                currentValuesLine += str(3.1411) + ", "

            # DECIMAL
            elif (columnType == 27):
                currentValuesLine += str(332.000006) + ", "

            # DATE
            elif (columnType == 29):
                genDay += 1
                if (genDay > 30):
                    genMonth += 1
                    genDay = 1
                if (genMonth > 12):
                    genYear += 1
                    genMonth = 1

                extraZeroDay = ""
                extraZeroMonth = ""
                if genDay < 10:
                    extraZeroDay = "0"
                if genMonth < 10:
                    extraZeroMonth = "0"

                currentValuesLine += "'" + str(genYear) + "-" + str(extraZeroMonth) + str(genMonth) + "-" + str(extraZeroDay) + str(genDay) + "', "

            # DATETIME
            elif (columnType == 30):
                genDayDateTime += 1
                if (genDayDateTime > 30):
                    genMonthDateTime += 1
                    genDayDateTime = 1
                if (genMonthDateTime > 12):
                    genYearDateTime += 1
                    genMonthDateTime = 1

                extraZeroDay = ""
                extraZeroMonth = ""
                if genDayDateTime < 10:
                    extraZeroDay = "0"
                if genMonthDateTime < 10:
                    extraZeroMonth = "0"

                currentValuesLine += "'" + str(genYearDateTime) + "-" + str(extraZeroMonth) + str(genMonthDateTime) + "-" + str(extraZeroDay) + str(genDayDateTime) + " 00:00:00', "

            # TIME
            elif (columnType == 32):
                genSecondsTime += 1
                if (genSecondsTime > 59):
                    genMinutesTime += 1
                    genSecondsTime = 0
                if (genMinutesTime > 59):
                    genHoursTime += 1
                    genMinutesTime = 0

                extraZeroSecond = ""
                extraZeroMinute = ""
                extraZeroHour = ""
                if genSecondsTime < 10:
                    extraZeroSecond = "0"
                if genMinutesTime < 10:
                    extraZeroMinute = "0"
                if genHoursTime < 10:
                    extraZeroHour = "0"

                currentValuesLine += "'" + " " + str(extraZeroHour) + str(genHoursTime) + ":" + str(extraZeroMinute) + str(genMinutesTime) + ":" + str(extraZeroSecond) + str(genSecondsTime) + "', "

            # Email
            elif (columnType == 34):              
                currentValuesLine += "".join(emailUsernameCombos[i]) + "@email.com" + ", "
            
        currentValuesLine = currentValuesLine[:-2]
        currentValuesLine += ");"

        generatedValues.append(currentValuesLine)
            
    return generatedValues

def generate_text_file(num_lines, schemaName, tableName, tableColumnHeaders, tableColumnValueTypes):

    folder_name = 'output'
    printColumns = "("
    for header in tableColumnHeaders:
        printColumns += header + ", "
    printColumns = printColumns[:-2]
    printColumns += ")"

    printValues = generate_column_values(num_lines, tableColumnValueTypes)

    # Create the 'output' folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_path = os.path.join(folder_name, 'output.txt')
    with open(file_path, 'w') as file:
        for i in range(num_lines):
            
            file.write(f"INSERT INTO {schemaName}.{tableName} {printColumns} VALUES {printValues[i]}\n")  # Writing lines to the file

    print(f"{num_lines} lines of text generated in '{file_path}'")


# Example: Generate 10 lines of text
num_lines = 15000

schemaName = "VisionVault"
tableName = "Dreams"

# Table Column Headers in Order
tableColumnHeaders = ["DreamID", "email", "DreamDate", "AuraTagID", "TypeTagID", "DreamName", "DreamDescription"]

# Table Column Value Types in Order
tableColumnValueTypes = [20, 34, 29, 20, 20, "Dream", 32]

# Generator Function
generate_text_file(num_lines, schemaName, tableName, tableColumnHeaders, tableColumnValueTypes)