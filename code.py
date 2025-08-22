import matplotlib.pyplot as plt
import numpy as np

# --- Data from the Analysis ---
# This data reflects the core narrative of soaring valuation vs. mounting losses.
# The years are aligned to show the trend over the same period.
years = ['2023', '2024', '2025']
# Valuation data in billions USD from key funding rounds.
valuation_values = [29, 86, 300]
# Reported and projected annual losses in billions USD.
losses_values = [-2, -5, -9]

# --- Creating the Dual-Axis Chart ---
fig, ax1 = plt.subplots(figsize=(12, 7))

# --- Primary Y-Axis (Valuation Bars) ---
# This axis will show the valuation in blue bars.
color_valuation = 'royalblue'
ax1.set_title("The OpenAI Paradox: Valuation vs. Losses", fontsize=18, fontweight='bold', pad=20)
bars = ax1.bar(years, valuation_values, color=color_valuation, width=0.6, label='Valuation')
ax1.set_xlabel("Year", fontsize=12, labelpad=10)
ax1.set_ylabel("Valuation (in Billions USD)", fontsize=12, color=color_valuation)
ax1.tick_params(axis='y', labelcolor=color_valuation)
ax1.set_ylim(0, max(valuation_values) * 1.1)

# Add value labels on top of each valuation bar for clarity.
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 5, f'${yval}B', ha='center', va='bottom', fontsize=11, fontweight='medium')

# --- Secondary Y-Axis (Losses Line) ---
# This axis will show the losses as a red line graph.
ax2 = ax1.twinx() # Create a second y-axis that shares the x-axis.
color_losses = 'crimson'
ax2.plot(years, losses_values, color=color_losses, marker='o', linestyle='--', linewidth=2.5, markersize=8, label='Annual Losses')
ax2.set_ylabel("Annual Losses (in Billions USD)", fontsize=12, color=color_losses, labelpad=15)
ax2.tick_params(axis='y', labelcolor=color_losses)

# Invert the y-axis for losses to visually represent a deepening deficit.
ax2.set_ylim(min(losses_values) * 1.3, 0)

# --- Styling, Grid, and Legend ---
# Remove the top and right borders for a modern, clean look.
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)

# Add a light grid to the primary axis for better readability of the bar values.
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.3)

# Create a single, clear legend for both data series.
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=11)

# Ensure the layout is tight and all elements are visible.
fig.tight_layout()

# --- Display the Chart ---
# To save the figure to a file for use in presentations or documents, uncomment the line below:
# plt.savefig('OpenAI_Valuation_vs_Losses_Chart.png', dpi=300, bbox_inches='tight')
plt.show()
