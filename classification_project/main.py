from src.predict import predict_image

# Call the predict_image function with your image data
# Replace 'image_path' with the path to your image file
image_path = 'C:\Users\amalm\Desktop\Git'
predicted_class = predict_image(image_path)
print(f"Predicted class: {predicted_class}")
