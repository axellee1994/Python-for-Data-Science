import time
import datetime
import locale

# Get the current Unix timestamp as a float (includes microseconds)
unix_timestamp_float = time.time()

# Set locale to enable thousands grouping for numbers.
try:
    locale.setlocale(locale.LC_ALL, '') # Set to user's default locale
except locale.Error:
    pass

# Format the timestamp with commas and scientific notation.
formatted_timestamp_commas = locale.format_string("%.4f", unix_timestamp_float, grouping=True)
formatted_timestamp_scientific = f"{unix_timestamp_float:.2e}"

current_local_date = datetime.date.today()

# Format with abbreviated month, zero-padded day, and full year.
formatted_date_with_padded_day = current_local_date.strftime("%b %d %Y")

day_number = current_local_date.day
if 1 <= day_number <= 9: 
    formatted_date_final = formatted_date_with_padded_day.replace(f" {day_number:02d}",  f" {day_number}")
else:
    formatted_date_final = formatted_date_with_padded_day

print(f"Seconds since January 1, 1970: {formatted_timestamp_commas} or {formatted_timestamp_scientific} in scientific notation")
print(formatted_date_final)