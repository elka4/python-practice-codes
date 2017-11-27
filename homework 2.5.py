# financial application: calculate tips

subtotal, gratuityrate = input("Enter the subtotal and a gratuity rate: ").split(",")

gratuity = (float(gratuityrate) / 100) * float(subtotal)

total = float(gratuity) + float(subtotal)

print("The gratuity is ", gratuity, "and the total is ", total)

