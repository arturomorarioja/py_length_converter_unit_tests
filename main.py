from app.length import Length

length = Length(float(input('Measure to convert:\n')), input('System to convert from - M(etric) or I(mperial):\n'))
print(length.convert())