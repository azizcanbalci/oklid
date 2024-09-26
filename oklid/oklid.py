import math

# Öklid mesafesi fonksiyonu
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Kullanıcıdan noktaları alma
def getPoints():
    points = []
    n = int(input("Kaç nokta gireceksiniz? "))
    
    for i in range(n):
        x = float(input(f"{i+1}. noktanın x koordinatını girin: "))
        y = float(input(f"{i+1}. noktanın y koordinatını girin: "))
        points.append((x, y))
    
    return points

# Mesafeleri hesaplama ve minimum mesafeyi bulma
def calculate_min_distance(points):
    distances = []
    
    # Tüm nokta çiftlerini kontrol eden döngü
    for i in range(len(points)):
        for j in range(i + 1, len(points)):  # Kendisiyle tekrar eden çiftleri engellemek için
            distance = euclideanDistance(points[i], points[j])
            distances.append(distance)
    
    # Minimum mesafeyi bulma3
    min_distance = min(distances)
    return min_distance

# Ana program
if __name__ == "__main__":
    points = getPoints()  # Kullanıcıdan noktaları al
    min_distance = calculate_min_distance(points)  # Minimum mesafeyi hesapla
    print(f"Noktalar arasındaki minimum Öklid mesafesi: {min_distance}")
