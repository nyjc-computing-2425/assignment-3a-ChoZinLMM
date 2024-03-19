nric = input('Enter an NRIC number: ')
nric = nric.strip('')
nric = nric.upper()

prefix = nric[0]
digits = nric[1:8]
suffix = nric[8:]
ST_suffix = "JZIHGFEDCBA"
FG_suffix = "XWUTRQPNMLK"
valid = "NRIC is valid."
invalid = "NRIC is invalid."

if prefix not in "STFG":
  print(invalid)

elif len(digits) != 7:
  print(invalid)

elif not digits.isdecimal():
  print(invalid)

elif len(suffix) != 1:
  print(invalid)

else :
  total = (int(digits[0]) * 2) + (int(digits[1]) * 7) + (int(digits[2]) * 6) + (int(digits[3]) * 5) + (int(digits[4]) * 4) + (int(digits[5]) * 3) + (int(digits[6]) * 2)

  if prefix in "TG":
    total = total + 4

  remainder = total % 11

  check_suffix = ''
  if prefix in "ST":
    check_suffix = ST_suffix[remainder]
  elif prefix in "FG":
    check_suffix = FG_suffix[remainder]

  if suffix == check_suffix :
    print(valid)
  else:
    print(invalid)
