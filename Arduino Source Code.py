import serial
import matplotlib.pyplot as plt

# Configure the serial port (change the port and baud rate as needed)
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino's port

# Create empty lists to store data
time_data = []
oximeter_data = []

try:
    while True:
        # Read data from Arduino
        data = ser.readline().decode('utf-8').strip()
        time_data.append(time_data[-1] + 1 if time_data else 0)  # Assuming 1 second intervals
        oximeter_data.append(float(data))

        # Plot the data
        plt.plot(time_data, oximeter_data, '-b')
        plt.xlabel('Time (s)')
        plt.ylabel('Oxygen Level (%)')
        plt.title('Oxygen Level Monitoring')
        plt.grid(True)
        plt.pause(1)  # Update the plot every 1 second

except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed.")

