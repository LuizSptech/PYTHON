import pandas as pd
 
nomes = ["Arthur", "Enzo", "Gabriel", "Leticia", "Luiz", "Sophie"]
 
for nome in nomes:
    df = pd.read_csv(f"roadvizor{nome}.csv", sep=";")
    df = df.rename(columns={"usuariotimestamp": "timestamp"})
    df["timestamp"] = pd.to_datetime(df["timestamp"], format="%d/%m/%Y %H:%M:%S")
 
    fim = df["timestamp"].max()
 
    ram = df[df["timestamp"] >= fim - pd.Timedelta(minutes=60)]
    cpu = df[df["timestamp"] >= fim - pd.Timedelta(minutes=60)]
    disco = df[df["timestamp"] >= fim - pd.Timedelta(minutes=30)]
 
    ram_media = (ram["ram_uso"] / ram["ram_total"] * 100).mean()
    cpu_pico = cpu["cpu_uso_geral"].max()
    disco_media = (disco["disco_uso"] / disco["disco_total"] * 100).mean()
 
    print(f"\n{nome}:\n")
    print(f"RAM   {ram_media:.2f}%")
    print(f"CPU   {cpu_pico:.2f}%")
    print(f"Disco {disco_media:.2f}%")
 
