import requests, json

d = requests.get("http://localhost:8000/status").json()

with open("_debug_output.txt", "w", encoding="utf-8") as f:
    f.write("=" * 60 + "\n")
    f.write(f"FINAL LEVEL: {d['final_level']}  (determiner: {d['determiner']})\n")
    f.write("=" * 60 + "\n")

    noaa = d["noaa"]
    f.write(f"\nNOAA Level: {noaa.get('level')}\n")
    f.write(f"  Bz={noaa.get('bz_gsm')} nT, Bt={noaa.get('bt')} nT\n")
    f.write(f"  Speed={noaa.get('speed')} km/s, Density={noaa.get('density')} p/cm3\n")
    f.write(f"  Bz neg duration={noaa.get('bz_neg_duration')} min\n")
    f.write(f"  Message: {noaa.get('message')}\n")

    kp = d["kp"]
    f.write(f"\nKp Level: {kp.get('level')}, Kp value: {kp.get('kp_value')}\n")

    f.write(f"\n--- CME LIST ({len(d['cme_list'])}) ---\n")
    for c in d["cme_list"]:
        tag = "*** EARTH TARGET ***" if c["earth_target"] else ""
        f.write(f"  {c['cme_id']}  level={c['level']}  speed={c.get('speed')}  align={c['alignment']}  {tag}\n")

    f.write(f"\n--- FLARE LIST ({len(d['flr_list'])}) ---\n")
    for fl in d["flr_list"]:
        f.write(f"  {fl['flare_id']}  class={fl['class_type']}  level={fl['level']}\n")

print("Written to _debug_output.txt")
