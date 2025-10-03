import random, time
import requests

BASE = "http://localhost:8000"

# Gera CPF válido (compatível com seu validador)
def gen_cpf():
    nums = [random.randint(0,9) for _ in range(9)]
    s1 = sum((10-i)*nums[i] for i in range(9))
    d1 = (s1*10) % 11
    if d1 == 10: d1 = 0
    nums.append(d1)
    s2 = sum((11-i)*nums[i] for i in range(10))
    d2 = (s2*10) % 11
    if d2 == 10: d2 = 0
    nums.append(d2)
    return "".join(map(str, nums))

UFs = ["MT","GO","PR","RS","SP","MS","BA","MG"]
CIDADES = ["Sorriso","Rondonópolis","Lucas do Rio Verde","Primavera do Leste","Rio Verde","Dourados","Londrina"]
CULTURAS = ["Soja","Milho","Algodão","Café","Cana-de-açúcar"]
SAFRAS = ["Safra 2023/24","Safra 2024/25"]

def cria_produtor():
    payload = {"cpf_cnpj": gen_cpf(), "name": f"Produtor {random.randint(1000,9999)}"}
    r = requests.post(f"{BASE}/producers", json=payload)
    r.raise_for_status()
    return r.json()["id"]

def cria_fazenda(producer_id):
    total = random.randint(300, 3000)
    agri = random.randint(int(total*0.4), int(total*0.8))
    veg  = random.randint(0, total - agri)
    city = random.choice(CIDADES)
    uf   = random.choice(UFs)
    payload = {
        "producer_id": producer_id,
        "name": f"Fazenda {random.randint(100,999)}",
        "city": city,
        "state": uf,
        "area_total": total,
        "area_agricultavel": agri,
        "area_vegetacao": veg
    }
    r = requests.post(f"{BASE}/farms", json=payload)
    r.raise_for_status()
    return r.json()["id"]

def vincula_culturas(farm_id):
    # 1 a 2 culturas por safra, em 1 a 2 safras
    for safra in random.sample(SAFRAS, k=random.randint(1,2)):
        for crop in random.sample(CULTURAS, k=random.randint(1,2)):
            r = requests.post(f"{BASE}/farm-crops", json={"farm_id": farm_id, "season": safra, "crop": crop})
            # pode retornar 200 mesmo se já existir: ok pra seed
            if r.status_code not in (200, 201):
                print("farm-crops warn:", r.status_code, r.text)

def main():
    # Cria n produtores, cada um com 1..3 fazendas
    n = 5
    for _ in range(n):
        pid = cria_produtor()
        for __ in range(random.randint(1,3)):
            fid = cria_fazenda(pid)
            vincula_culturas(fid)
        # evita “rajada” de requisições
        time.sleep(0.1)

    # Mostra um resumo no final
    print(" summary:", requests.get(f"{BASE}/dashboard/summary").json())
    print(" pie/state:", requests.get(f"{BASE}/dashboard/pie/state").json())
    print(" pie/crop:", requests.get(f"{BASE}/dashboard/pie/crop").json())
    print(" pie/landuse:", requests.get(f"{BASE}/dashboard/pie/landuse").json())

if __name__ == "__main__":
    main()
