import calendar

def display_calendar(year, month):
    # Uzyskaj kalendarz dla danego roku i miesiąca
    cal = calendar.monthcalendar(year, month)

    # Uzyskaj nazwę miesiąca
    month_name = calendar.month_name[month]

    # Wyświetl nazwę miesiąca i rok
    print(f"{' ' * 10}{month_name} {year}")
    print("-" * 50)

    # Wyświetl nazwy dni tygodnia
    print("  Pon  Wt   Śr   Czw  Pt   Sob  Nd")

    # Wyświetl dni miesiąca
    for week in cal:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "     "
            else:
                week_str += f"{day:2d}   "
        print(week_str)

# Testowanie kalendarza
display_calendar(2023, 5)
