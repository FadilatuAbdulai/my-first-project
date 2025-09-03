try:
    # Ask the user for the filename
    filename = input("Enter the name of the file to read: ")

    # Open the file for reading
    with open(filename, "r") as file:
        content = file.read()
        print("\n✅ File read successfully!")

    # Modify the content (example: make everything uppercase)
    modified_content = content.upper()

    # Write to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)

    print(f"✅ Modified content written to {new_filename}")

except FileNotFoundError:
    print("❌ Error: File not found. Please check the filename and try again.")

except Exception as e:
    print("⚠ An error occurred:", e)
