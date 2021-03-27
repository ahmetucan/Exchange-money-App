import requests
import json

api_url = "https://api.exchangeratesapi.io/latest?base="


bozdur = input("Bozulan döviz türü: ")
bozulan = input("alınan döviz türü: ")
miktar = int(input(f"Bozdurulmak istenen {bozdur} miktarı: "))

result = requests.get(api_url+bozdur)
result = json.loads(result.text)
alinan_miktar = miktar * result['rates'][bozulan]

print(f"1 {bozdur} = {result['rates'][bozulan]} {bozulan} ")
print(f"{miktar} {bozdur} = {alinan_miktar} {bozulan} ")

