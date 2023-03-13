import ru_local as ru

days = int(input())
spd_mh = 38241
spd_kmh = spd_mh / 0.62137
spd_kmd = spd_kmh * 24
From_sun = 16637000000 / 0.62137
S_kmd = From_sun - (days * spd_kmd)
StE = 148640000
VtE = StE - S_kmd
print(ru.speed_km_in_day, spd_kmd)
print(ru.days_on_the_way, days)
print(ru.distance_left, S_kmd)
c_ms = 300000000
c_kmh = c_ms * 3.6
air_prmblt = 1
delay = VtE / (24 * c_kmh * air_prmblt)
print(ru.speed_light, c_kmh)
print(ru.wireless_delay, delay)
