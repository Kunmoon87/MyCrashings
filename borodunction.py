#Name: Tevin martin
#Email: Tevin.martin38@myhunter.cuny.edu
#Date: march 15,2024
#This progrsm prints:Boro raction / test brooklyn and test queens

import matplotlib.pyplot as plt
import pandas as pd

# Open the CSV file and store in pop
pop = pd.read_csv('nycHistPop.csv', skiprows=5)

# Function to compute fraction of population for specified borough
def compute_fraction(borough):
    if borough in pop.columns:
        pop['Fraction'] = pop[borough] / pop['Total']
        return True
    else:
        return False

# Create a plot of year versus fraction of pop. in specified borough (with labels)
def plot_borough_fraction(borough):
    pop.plot(x='Year', y='Fraction')
    

# User input for specifying borough and output file name
borough = input("Enter borough name: ")
output_file = input("Enter output file name: ")

# Check if the borough exists in the data
if compute_fraction(borough):
    plot_borough_fraction(borough)
    plt.savefig(output_file)
    print(f"The file {output_file} has been saved.")
else:
    print("Invalid borough name. Please enter a valid borough name from the dataset.")
