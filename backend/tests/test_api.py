import random
import requests

BASE = "http://localhost:8000"

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

def test_create_producer_and_duplicate():
    cpf = gen_cpf()
    r = requests.post(f"{BASE}/producers", json={"cpf_cnpj": cpf, "name": "Teste Produtor"})
    assert r.status_code == 201, r.text
    r2 = requests.post(f"{BASE}/producers", json={"cpf_cnpj": cpf, "name": "Teste Produtor"})
    assert r2.status_code == 409

def test_invalid_cpf_422():
    r = requests.post(f"{BASE}/producers", json={"cpf_cnpj": "12345678900", "name": "Invalido"})
    assert r.status_code == 422

def test_farm_validation_and_dashboard():
    cpf = gen_cpf()
    r = requests.post(f"{BASE}/producers", json={"cpf_cnpj": cpf, "name": "Prod Faz"})
    assert r.status_code == 201
    pid = r.json()["id"]

    bad = {"producer_id": pid, "name":"FX", "city":"X", "state":"MT", "area_total":100, "area_agricultavel":80, "area_vegetacao":30}
    rbad = requests.post(f"{BASE}/farms", json=bad)
    assert rbad.status_code == 422

    good = {"producer_id": pid, "name":"FY", "city":"X", "state":"MT", "area_total":100, "area_agricultavel":70, "area_vegetacao":30}
    rgood = requests.post(f"{BASE}/farms", json=good)
    assert rgood.status_code == 201
    farm_id = rgood.json()["id"]

    rfc = requests.post(f"{BASE}/farm-crops", json={"farm_id": farm_id, "season":"Safra 2024/25", "crop":"Soja"})
    assert rfc.status_code == 200

    summ = requests.get(f"{BASE}/dashboard/summary").json()
    assert "total_farms" in summ and "total_hectares" in summ
    pie = requests.get(f"{BASE}/dashboard/pie/crop").json()
    assert isinstance(pie, list)
