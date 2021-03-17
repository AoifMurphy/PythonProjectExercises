# Open a file: file
file = open("MobyDick.txt", mode = "r")

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)

# Open a file: file
file = open("MobyDick.txt", mode = "r")

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)


# Read & print the first 3 lines
with open('MobyDick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())


    # Assign filename: file
    file = 'Seaslug.txt'

    # Import file: data
    data = np.loadtxt(file, delimiter='\t', dtype=str)

    # Print the first element of data
    print(data[0])

    # Import data as floats and skip the first row: data_float
    data_float = np.loadtxt(file, delimiter='\t', dtype='float', skiprows=1)

    # Print the 10th element of data_float
    print(data_float[9])

    # Plot a scatterplot of the data
    plt.scatter(data_float[:, 0], data_float[:, 1])
    plt.xlabel('time (min.)')
    plt.ylabel('percentage of larvae')
    plt.show()

    # Assign the filename: file
    file = 'Titanic.csv'

    # Import file using np.recfromcsv:
    d = np.recfromcsv(file)

    # Print out first three entries of d
    print(d[:3])

    # Assign filename: file
    file = 'Seaslug.txt'

    # Import file: data
    data = np.loadtxt(file, delimiter='\t', dtype=str)

    # Print the first element of data
    print(data[0])

    # Import data as floats and skip the first row: data_float
    data_float = np.loadtxt(file, delimiter='\t', dtype='float', skiprows=1)

    # Print the 10th element of data_float
    print(data_float[9])

    # Plot a scatterplot of the data
    plt.scatter(data_float[:, 0], data_float[:, 1])
    plt.xlabel('time (min.)')
    plt.ylabel('percentage of larvae')
    plt.show()

    # Assign filename: file
    file = 'Seaslug.txt'

    # Import file: data
    data = np.loadtxt(file, delimiter='\t', dtype=str)

    # Print the first element of data
    print(data[0])

    # Import data as floats and skip the first row: data_float
    data_float = np.loadtxt(file, delimiter='\t', dtype='float', skiprows=1)

    # Print the 10th element of data_float
    print(data_float[9])

    # Plot a scatterplot of the data
    plt.scatter(data_float[:, 0], data_float[:, 1])
    plt.xlabel('time (min.)')
    plt.ylabel('percentage of larvae')
    plt.show()