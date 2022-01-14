def find_distance(A,B):
    key = 'YourAPIkey'  # Enter Your API Key here 
    geocoder = OpenCageGeocode(key)
    
    result_A = geocoder.geocode(A)
    lat_A = result_A[0]['geometry']['lat']
    lng_A = result_A[0]['geometry']['lng']
    
    result_B = geocoder.geocode(B)
    lat_B = result_B[0]['geometry']['lat']
    lng_B = result_B[0]['geometry']['lng']  
    
    return (geodesic((lat_A,lng_A), (lat_B,lng_B)).kilometers)

city1 = input("Enter the first city : ")
city2 = input("Enter the second city : ")
distance = find_distance(city1, city2)

print(f"The distance between {city1} and {city2} is {distance}")
