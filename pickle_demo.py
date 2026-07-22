import pickle
data = [10, 20, 30, 40]
student = {
    "name" : "manoj",
    "age" : 22,
    "city" : "hyderabed",
    "course" : "python"
}
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)
with open("data.pkl", "rb") as file:
    print(pickle.load(file))
with open("data.pkl", "wb") as file:
    pickle.dump(student, file)
with open("data.pkl", "rb") as file:
    print(pickle.load(file))
print("Data saved successfully!")